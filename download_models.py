# download_models_fixed.py
from pathlib import Path
from urllib.request import urlretrieve

BASE_URL = "https://cdn.jsdelivr.net/gh/cgarciagl/face-api.js@0.22.2/weights/"
FILES = [
    # Tiny Face Detector
    "tiny_face_detector_model-weights_manifest.json",
    "tiny_face_detector_model-shard1",
    # SSD Mobilenet
    "ssd_mobilenetv1_model-weights_manifest.json",
    "ssd_mobilenetv1_model-shard1",
    "ssd_mobilenetv1_model-shard2",
    # Landmarks
    "face_landmark_68_model-weights_manifest.json",
    "face_landmark_68_model-shard1",
    # Expressions
    "face_expression_model-weights_manifest.json",
    "face_expression_model-shard1",
    # (Opcional) Reconhecimento
    "face_recognition_model-weights_manifest.json",
    "face_recognition_model-shard1",
    "face_recognition_model-shard2",
    # (Opcional) Age/Gender
    "age_gender_model-weights_manifest.json",
    "age_gender_model-shard1",
]

DEST = Path("static/models")
DEST.mkdir(parents=True, exist_ok=True)

for f in FILES:
    url = BASE_URL + f
    dst = DEST / f
    if dst.exists():
        print(f"✅ Já existe: {f}")
        continue
    try:
        print(f"⬇️  Baixando {f} ...")
        urlretrieve(url, dst)
        print(f"   ✔️  Salvo: {dst}")
    except Exception as e:
        print(f"   ⚠️  Falhou {f}: {e}")

print(f"\n✨ Pronto. Modelos em: {DEST.resolve()}")
