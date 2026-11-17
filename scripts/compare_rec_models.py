"""Compare RapidOCR recognition models on one split.

    python scripts/compare_rec_models.py dev default latin en cyrillic v6small

Models (official PaddlePaddle ONNX exports on Hugging Face, Apache 2.0) go to models/rec/<name>/:
    huggingface.co/PaddlePaddle/{latin,en,cyrillic}_PP-OCRv5_mobile_rec_onnx, PP-OCRv6_small_rec_onnx
keys.txt is the character list from the model's inference.yml (PostProcess.character_dict).
'default' is the recognizer bundled with rapidocr-onnxruntime (ch_PP-OCRv4).
"""
import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from receipt.config import load_config
from receipt.dataset import rows_for, load_gt
from receipt.pipeline import load_image, process
from receipt.metrics import field_matches, item_counts, prf, text_counts
from receipt.normalize import norm_text_for_metric
split=sys.argv[1]; names=sys.argv[2:]
base=load_config()
MODELS={'default':{}}  # empty: the recognizer bundled with RapidOCR
for n in ('latin','en','cyrillic'):
    MODELS[n]={'rec_model_path':f'models/rec/{n}_PP-OCRv5_mobile_rec_onnx/inference.onnx','rec_keys_path':f'models/rec/{n}_PP-OCRv5_mobile_rec_onnx/keys.txt'}
MODELS['v6small']={'rec_model_path':'models/rec/PP-OCRv6_small_rec_onnx/inference.onnx','rec_keys_path':'models/rec/PP-OCRv6_small_rec_onnx/keys.txt'}
for name in names:
    cfg=copy.deepcopy(base); cfg['ocr']['rapidocr']=MODELS[name]
    S={}
    for r in rows_for(cfg,split):
        if 'partial' in r['conditions']: continue
        kind='synthetic' if 'synthetic' in r['conditions'] else 'real'
        gt,txt=load_gt(cfg,r['receipt_id'])
        out=process(load_image(r['path']),cfg,engine='rapidocr',preprocess=True,postprocess=True,cache_dir=Path('.cache/ocr'))
        g=S.setdefault(kind,dict(n=0,acc=0,tp=0,p=0,gt=0,cons=0,ce=0,cn=0,we=0,wn=0,ocr=0))
        res=out['result']; m=field_matches(gt,res); g['n']+=1; g['acc']+=sum(m.values())/len(m)
        tp,p,n=item_counts(gt['items'],res['items']); g['tp']+=tp; g['p']+=p; g['gt']+=n; g['cons']+=out['consistent']; g['ocr']+=out['timings']['ocr']
        if txt:
            ce,cn,we,wn=text_counts(txt,out['text'],True); g['ce']+=ce; g['cn']+=cn; g['we']+=we; g['wn']+=wn
    for k,g in S.items():
        n=g['n']; f1=prf(g['tp'],g['p'],g['gt'])[2]
        cer=f"{100*g['ce']/g['cn']:.1f}" if g['cn'] else '-'; wer=f"{100*g['we']/g['wn']:.1f}" if g['wn'] else '-'
        print(f"{name:9s} {k:9s} n={n:2d} fields {100*g['acc']/n:5.1f} | items F1 {100*f1:5.1f} | consistent {100*g['cons']/n:5.1f} | CER {cer} WER {wer} | OCR {g['ocr']/n:.1f}s", flush=True)
