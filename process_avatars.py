import os
from PIL import Image

SRC_MARCOS = r"C:\Users\mikaa\.gemini\antigravity-ide\brain\ddbf4aee-d707-4b76-85db-b04896aca68f\avatar_marcos_familia_1789266985520.jpg"
SRC_JULIANA = r"C:\Users\mikaa\.gemini\antigravity-ide\brain\ddbf4aee-d707-4b76-85db-b04896aca68f\avatar_juliana_araguaia_1789266995088.jpg"
SRC_CARLOS = r"C:\Users\mikaa\.gemini\antigravity-ide\brain\ddbf4aee-d707-4b76-85db-b04896aca68f\avatar_carlos_eduardo_pesca_1789267005490.jpg"

DEST_DIR = r"C:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\assets\images\depoimentos"
os.makedirs(DEST_DIR, exist_ok=True)

for src, name in [(SRC_MARCOS, "avatar-marcos.jpg"), (SRC_JULIANA, "avatar-juliana.jpg"), (SRC_CARLOS, "avatar-carlos-eduardo.jpg")]:
    im = Image.open(src)
    # Redimensiona para 240x240 com filtro Lanczos de alta nitidez
    im_thumb = im.resize((240, 240), Image.Resampling.LANCZOS)
    dest_path = os.path.join(DEST_DIR, name)
    im_thumb.save(dest_path, "JPEG", quality=92, optimize=True)
    print("Salvo:", dest_path)
