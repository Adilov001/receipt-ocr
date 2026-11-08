"""Web UI: python app.py  (CPU only)."""
import html
import json
import sys
from pathlib import Path

import cv2
import gradio as gr
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from receipt import FIELDS  # noqa: E402
from receipt.config import ROOT, load_config  # noqa: E402
from receipt.dataset import load_gt, load_meta  # noqa: E402
from receipt.metrics import cer, field_matches, item_counts, prf, wer  # noqa: E402
from receipt.ocr import ENGINES  # noqa: E402
from receipt.pipeline import load_image, process  # noqa: E402

CFG = load_config()
CACHE = ROOT / CFG["eval"]["cache_dir"]
COLORS = {"match": "#1a7f37", "mismatch": "#cf222e", "no_data": "#9a6700"}
LABELS = {"match": "совпадает", "mismatch": "не совпадает", "no_data": "нет данных"}


def _conf_color(c):
    return (40, 167, 69) if c >= 0.8 else (255, 165, 0) if c >= 0.5 else (220, 53, 69)  # RGB


def _to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) if img.ndim == 2 else cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def draw(out, original):
    pre = _to_rgb(out["preprocessed"]).copy()
    for l in out["lines"]:
        x0, y0, x1, y1 = l["box"]
        cv2.rectangle(pre, (x0, y0), (x1, y1), _conf_color(l["conf"]), 2)
    orig = cv2.cvtColor(original, cv2.COLOR_BGR2RGB).copy()
    if out["qr_polygon"] is not None:
        target = orig if out["qr_polygon_on"] == "original" else pre
        pts = np.array(out["qr_polygon"], dtype=np.int32).reshape(-1, 1, 2)
        cv2.polylines(target, [pts], True, (0, 102, 255), 6)
    return orig, pre


def field_crops(out):
    img = _to_rgb(out["preprocessed"])
    h, w = img.shape[:2]
    res = out["result"]
    crops = []
    for f, box in out["sources"].items():
        x0, y0, x1, y1 = box
        crop = img[max(0, y0 - 6):min(h, y1 + 6), max(0, x0 - 6):min(w, x1 + 6)]
        if crop.size:
            crops.append((crop, f"{f}: {res.get(f)}"))
    for k, box in enumerate(out["item_sources"], 1):
        if box:
            x0, y0, x1, y1 = box
            crops.append((img[max(0, y0 - 40):min(h, y1 + 6), max(0, x0 - 6):min(w, x1 + 6)], f"item {k}"))
    return crops


def fields_html(out):
    res, src = out["result"], out["field_source"]
    rows = "".join(
        f"<tr><td><b>{f}</b></td><td>{html.escape(str(res.get(f)))}</td>"
        f"<td style='color:#666'>{src.get(f, '')}</td></tr>" for f in FIELDS)
    q = res["qr"]
    qr = (f"<p><b>QR:</b> {'decoded' if q['decoded'] else 'not decoded'}"
          f"{' (' + q['attempt'] + ')' if q['attempt'] else ''}<br><code>{html.escape(str(q['raw']))}</code></p>")
    return f"<table><tr><th>field</th><th>value</th><th>source</th></tr>{rows}</table>{qr}"


def checks_html(out):
    rows = "".join(
        f"<tr><td>{html.escape(c['check'])}</td>"
        f"<td style='color:white;background:{COLORS[c['status']]};padding:2px 8px'>{LABELS[c['status']]}</td>"
        f"<td>{html.escape(str(c['expected']))}</td><td>{html.escape(str(c['actual']))}</td></tr>"
        for c in out["checks"])
    verdict = ("<p style='color:#1a7f37'><b>Чек согласован</b></p>" if out["consistent"]
               else "<p style='color:#cf222e'><b>Чек не согласован</b></p>")
    return f"{verdict}<table><tr><th>проверка</th><th>статус</th><th>ожидалось</th><th>получено</th></tr>{rows}</table>"


def gt_html(out, gt, gt_text):
    if not gt and not gt_text:
        return "<p style='color:#666'>Эталон не найден (загрузите JSON или используйте фото из набора).</p>"
    parts = []
    res = out["result"]
    if gt:
        m = field_matches(gt, res)
        rows = "".join(
            f"<tr style='background:{'#dafbe1' if ok else '#ffebe9'}'><td>{f}</td>"
            f"<td>{html.escape(str(gt.get(f)))}</td><td>{html.escape(str(res.get(f)))}</td></tr>"
            for f, ok in m.items())
        tp, npred, ngt = item_counts(gt.get("items", []), res["items"])
        acc = sum(m.values()) / len(m) if m else 0
        parts.append(f"<p><b>Точность полей:</b> {acc:.0%} &nbsp; <b>F1 по позициям:</b> {prf(tp, npred, ngt)[2]:.0%}</p>"
                     f"<table><tr><th>поле</th><th>эталон</th><th>результат</th></tr>{rows}</table>")
    if gt_text:
        parts.append(f"<p><b>CER:</b> {cer(gt_text, out['text']):.1%} &nbsp; <b>WER:</b> {wer(gt_text, out['text']):.1%}</p>")
    return "".join(parts)


def find_gt(path, gt_file):
    if gt_file:
        return json.loads(Path(gt_file).read_text(encoding="utf-8")), None
    name = Path(path).name
    try:
        for r in load_meta(CFG):
            if r["image"] == name:
                return load_gt(CFG, r["receipt_id"])
    except FileNotFoundError:
        pass
    return None, None


def timings_md(out):
    t = out["timings"]
    cached = " (OCR из кэша, время замерено при первом запуске)" if t.get("ocr_cached") else ""
    return (f"**Время, с:** всего {t['total']:.2f} · предобработка {t['preprocess']:.2f} · QR {t['qr']:.2f} · "
            f"OCR ({out['engine']}) {t['ocr']:.2f} · извлечение {t['extract']:.2f}{cached}  \n"
            f"Предобработка: {out['pre_info']}")


def run(path, engine, pre, post, gt_file):
    if not path:
        raise gr.Error("Загрузите изображение чека")
    img = load_image(path)
    out = process(img, CFG, engine=engine, preprocess=pre, postprocess=post, cache_dir=CACHE)
    orig, pre_img = draw(out, img)
    gt, gt_text = find_gt(path, gt_file)
    items = pd.DataFrame(out["result"]["items"], columns=["name", "quantity", "price", "total"])
    return (orig, pre_img, fields_html(out), items, checks_html(out), gt_html(out, gt, gt_text),
            timings_md(out), field_crops(out), out["result"], out["text"])


def compare(path, pre, post, gt_file):
    if not path:
        raise gr.Error("Загрузите изображение чека")
    img = load_image(path)
    gt, gt_text = find_gt(path, gt_file)
    rows = []
    for engine in ENGINES:
        try:
            out = process(img, CFG, engine=engine, preprocess=pre, postprocess=post, cache_dir=CACHE)
        except Exception as e:  # engine not installed etc.
            rows.append({"engine": engine, "error": str(e)})
            continue
        row = {"engine": engine, "time, s": round(out["timings"]["total"], 2),
               "lines": len(out["lines"]),
               "mean conf": round(float(np.mean([l["conf"] for l in out["lines"]])) if out["lines"] else 0, 2),
               "total": out["result"]["total"], "consistent": out["consistent"]}
        if gt:
            m = field_matches(gt, out["result"])
            row["field acc"] = round(sum(m.values()) / len(m), 2)
        if gt_text:
            row["CER"] = round(cer(gt_text, out["text"]), 3)
        rows.append(row)
    return pd.DataFrame(rows)


with gr.Blocks(title="Распознавание кассовых чеков") as demo:
    gr.Markdown("## Распознавание кассовых чеков (OCR + QR)")
    with gr.Row():
        with gr.Column(scale=1):
            inp = gr.Image(type="filepath", label="Фото чека")
            engine = gr.Dropdown(list(ENGINES), value="tesseract", label="OCR-движок")
            pre = gr.Checkbox(True, label="Предобработка")
            post = gr.Checkbox(True, label="Постобработка")
            gt_file = gr.File(label="Эталон JSON (необязательно)", file_types=[".json"])
            btn = gr.Button("Распознать", variant="primary")
            cmp_btn = gr.Button("Сравнить движки")
            timing = gr.Markdown()
        with gr.Column(scale=2):
            with gr.Row():
                orig_out = gr.Image(label="Исходное изображение (синим — QR)")
                pre_out = gr.Image(label="После предобработки (рамки: зел. ≥0.8, оранж. ≥0.5, красн. <0.5)")
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Извлечённые поля")
            fields_out = gr.HTML()
            items_out = gr.Dataframe(label="Позиции")
        with gr.Column():
            gr.Markdown("### Проверки и сверка с QR")
            checks_out = gr.HTML()
            gr.Markdown("### Сравнение с эталоном")
            gt_out = gr.HTML()
    crops_out = gr.Gallery(label="Фрагменты изображения, из которых извлечены поля", columns=4, height=260)
    cmp_out = gr.Dataframe(label="Сравнение движков на этом изображении")
    with gr.Accordion("JSON и распознанный текст", open=False):
        json_out = gr.JSON()
        text_out = gr.Textbox(lines=15, label="Текст по строкам")

    btn.click(run, [inp, engine, pre, post, gt_file],
              [orig_out, pre_out, fields_out, items_out, checks_out, gt_out, timing, crops_out, json_out, text_out])
    cmp_btn.click(compare, [inp, pre, post, gt_file], cmp_out)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
