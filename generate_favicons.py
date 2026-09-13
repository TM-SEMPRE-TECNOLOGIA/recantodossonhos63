from PIL import Image
import os

src_path = r"C:/Users/mikaa/.gemini/antigravity-ide/brain/cfd71cd7-0085-4790-ba5b-3eb9d1d2b837/.user_uploaded/media_1789176914243.png"
base_dir = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos"
img_dir = os.path.join(base_dir, "assets", "images")
os.makedirs(img_dir, exist_ok=True)

im = Image.open(src_path).convert("RGBA")

# Crop to bounding box
bbox = im.getbbox()
cropped = im.crop(bbox)

# Create a square transparent canvas with 6% padding for optimal tab visibility
cw, ch = cropped.size
max_dim = max(cw, ch)
pad = int(max_dim * 0.06)
canvas_size = max_dim + pad * 2

square_im = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
offset_x = (canvas_size - cw) // 2
offset_y = (canvas_size - ch) // 2
square_im.paste(cropped, (offset_x, offset_y), cropped)

# Export standard web favicons
sizes = {
    "fav-icon.png": (56, 56),
    "favicon-32x32.png": (32, 32),
    "favicon-16x16.png": (16, 16),
    "apple-touch-icon.png": (180, 180),
    "favicon-192x192.png": (192, 192),
    "favicon-512x512.png": (512, 512),
}

for filename, sz in sizes.items():
    resized = square_im.resize(sz, Image.Resampling.LANCZOS)
    target = os.path.join(img_dir, filename)
    resized.save(target, "PNG", optimize=True)
    print(f"Generated {filename} ({sz[0]}x{sz[1]}) -> {target}")

# Export multi-res .ico in root and in assets/images/
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
root_ico = os.path.join(base_dir, "favicon.ico")
square_im.save(root_ico, format="ICO", sizes=ico_sizes)
print(f"Generated root favicon.ico -> {root_ico}")

assets_ico = os.path.join(img_dir, "favicon.ico")
square_im.save(assets_ico, format="ICO", sizes=ico_sizes)
print(f"Generated assets/images/favicon.ico -> {assets_ico}")
