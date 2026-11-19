"""Quantize the text recognizer (FP32 -> INT8, dynamic quantization) and compare it with the original.

    python scripts/quantize_rec.py              # writes models/rec/<name>_int8/ and prints the table
    python scripts/quantize_rec.py --compare-only

Dynamic quantization stores the weights of MatMul / Gemm layers as 8-bit integers and quantizes the
activations on the fly; convolutions stay in float (quantizing them needs calibration data and hurts
CTC recognizers most). The comparison runs the full pipeline on the dev split, real photos.
"""
import argparse
import copy
import shutil
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from receipt.config import ROOT, load_config  # noqa: E402
from receipt.dataset import load_gt, rows_for  # noqa: E402
from receipt.metrics import field_matches, item_counts, prf, text_counts  # noqa: E402
from receipt.pipeline import load_image, process  # noqa: E402

SRC = ROOT / "models/rec/cyrillic_PP-OCRv5_mobile_rec_onnx"
DST = ROOT / "models/rec/cyrillic_PP-OCRv5_mobile_rec_onnx_int8"


def quantize(op_types=("MatMul", "Gemm")):
    """The PaddleOCR export uses ONNX opset 7; the quantizer upgrades it, and opset >= 9 no longer has the
    BatchNormalization attribute 'spatial' (always 1 here, which is the new default), so it is removed first."""
    import onnx
    from onnxruntime.quantization import QuantType, quantize_dynamic

    DST.mkdir(parents=True, exist_ok=True)
    model = onnx.load(str(SRC / "inference.onnx"))
    for node in model.graph.node:
        if node.op_type == "BatchNormalization":
            assert all(a.i == 1 for a in node.attribute if a.name == "spatial")
            keep = [a for a in node.attribute if a.name != "spatial"]
            del node.attribute[:]
            node.attribute.extend(keep)
    model = onnx.version_converter.convert_version(model, 13)
    # the exporter stores the weights in Constant nodes; the quantizer only sees initializers
    keep_nodes = []
    for node in model.graph.node:
        if node.op_type == "Constant" and len(node.attribute) == 1 and node.attribute[0].name == "value":
            t = onnx.TensorProto()
            t.CopyFrom(node.attribute[0].t)
            t.name = node.output[0]
            model.graph.initializer.append(t)
        else:
            keep_nodes.append(node)
    del model.graph.node[:]
    model.graph.node.extend(keep_nodes)
    model.ir_version = max(model.ir_version, 7)  # IR >= 4: initializers need not be graph inputs
    fixed = DST / "fp32_opset13.onnx"
    onnx.save(model, str(fixed))
    if op_types:
        quantize_dynamic(str(fixed), str(DST / "inference.onnx"),
                         weight_type=QuantType.QInt8, op_types_to_quantize=list(op_types))
        fixed.unlink()
    else:
        fixed.rename(DST / "inference.onnx")
    shutil.copy(SRC / "keys.txt", DST / "keys.txt")


def calibration_lines(n_images=12, per_image=20):
    """Real text-line crops from DEV photos, preprocessed exactly as the recognizer sees them
    (height 48, width scaled, padded to 320, normalised to [-1, 1])."""
    import cv2

    from receipt.ocr import rapidocr_engine
    from receipt.preprocess import preprocess

    cfg = load_config()
    det = rapidocr_engine(cfg["ocr"]["rapidocr"])
    out = []
    rows = [r for r in rows_for(cfg, "dev") if "synthetic" not in r["conditions"] and "partial" not in r["conditions"]]
    for r in rows[:n_images]:
        g = preprocess(load_image(r["path"]), cfg)["final"]
        bgr = cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)
        res, _ = det(bgr)
        for pts, _, _ in (res or [])[:per_image]:
            pts = np.array(pts)
            x0, y0 = pts.min(0).astype(int)
            x1, y1 = pts.max(0).astype(int)
            crop = bgr[max(0, y0):y1, max(0, x0):x1]
            if crop.size == 0:
                continue
            w = min(320, max(1, int(48 * crop.shape[1] / crop.shape[0])))
            im = cv2.resize(crop, (w, 48)).astype(np.float32) / 255
            im = (im - 0.5) / 0.5
            pad = np.zeros((48, 320, 3), np.float32)
            pad[:, :w] = im
            out.append(pad.transpose(2, 0, 1)[None])
    return out


def quantize_static(op_types=("Conv", "MatMul")):
    """Static INT8 (QDQ) quantization of convolutions and MatMuls, calibrated on dev text lines."""
    from onnxruntime.quantization import CalibrationDataReader, QuantFormat, QuantType, quantize_static

    quantize(())  # writes the fixed FP32 model (opset 13, initializers) as DST/inference.onnx, nothing quantized
    fixed = DST / "fp32_fixed.onnx"
    (DST / "inference.onnx").rename(fixed)
    data = calibration_lines()

    class Reader(CalibrationDataReader):
        def __init__(self):
            self.it = iter({"x": d} for d in data)

        def get_next(self):
            return next(self.it, None)

    quantize_static(str(fixed), str(DST / "inference.onnx"), Reader(), quant_format=QuantFormat.QDQ,
                    activation_type=QuantType.QUInt8, weight_type=QuantType.QInt8,
                    op_types_to_quantize=list(op_types), per_channel=True)
    fixed.unlink()
    return len(data)


def rec_speed(model_dir, n=200, seed=0):
    """Recognizer alone: mean ms per text-line crop (48 x 320), same random inputs for both models."""
    import onnxruntime as ort

    opts = ort.SessionOptions()
    opts.intra_op_num_threads, opts.inter_op_num_threads = 4, 1
    sess = ort.InferenceSession(str(model_dir / "inference.onnx"), opts, providers=["CPUExecutionProvider"])
    name = sess.get_inputs()[0].name
    x = np.random.default_rng(seed).random((n, 1, 3, 48, 320), dtype=np.float32)
    for i in range(10):
        sess.run(None, {name: x[i]})
    t = time.perf_counter()
    for i in range(n):
        sess.run(None, {name: x[i]})
    return 1000 * (time.perf_counter() - t) / n


def pipeline_metrics(model_dir, split="dev"):
    cfg = copy.deepcopy(load_config())
    cfg["ocr"]["rapidocr"]["rec_model_path"] = str((model_dir / "inference.onnx").relative_to(ROOT))
    cfg["ocr"]["rapidocr"]["rec_keys_path"] = str((model_dir / "keys.txt").relative_to(ROOT))
    g = dict(n=0, acc=0.0, tp=0, p=0, gt=0, ce=0, cn=0, we=0, wn=0, ocr=0.0)
    for r in rows_for(cfg, split):
        if "partial" in r["conditions"] or "synthetic" in r["conditions"]:
            continue
        gt, txt = load_gt(cfg, r["receipt_id"])
        out = process(load_image(r["path"]), cfg, engine="rapidocr", cache_dir=ROOT / cfg["eval"]["cache_dir"])
        m = field_matches(gt, out["result"])
        g["n"] += 1
        g["acc"] += sum(m.values()) / len(m)
        g["ocr"] += out["timings"]["ocr"]
        tp, p, n = item_counts(gt["items"], out["result"]["items"])
        g["tp"] += tp
        g["p"] += p
        g["gt"] += n
        if txt:
            ce, cn, we, wn = text_counts(txt, out["text"], True)
            g["ce"] += ce
            g["cn"] += cn
            g["we"] += we
            g["wn"] += wn
    return {"field acc %": 100 * g["acc"] / g["n"], "item F1 %": 100 * prf(g["tp"], g["p"], g["gt"])[2],
            "CER %": 100 * g["ce"] / g["cn"], "WER %": 100 * g["we"] / g["wn"], "photos": g["n"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--compare-only", action="store_true")
    ap.add_argument("--split", default="dev")
    args = ap.parse_args()
    if not args.compare_only:
        quantize()
    rows = []
    for label, d in (("FP32 (original)", SRC), ("INT8 (dynamic)", DST)):
        row = {"model": label, "size MB": (d / "inference.onnx").stat().st_size / 2**20,
               "ms per line": rec_speed(d)}
        row.update(pipeline_metrics(d, args.split))
        rows.append(row)
        print(row, flush=True)
    import pandas as pd
    print(pd.DataFrame(rows).set_index("model").to_markdown(floatfmt=".1f"))


if __name__ == "__main__":
    main()
