import re
import os

site_dir = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos"
index_path = os.path.join(site_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

print("=== 1. IMAGES IN INDEX.HTML ===")
imgs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', content)
for i, img in enumerate(imgs, 1):
    print(f"{i}: {img}")

print("\n=== 2. BACKGROUND IMAGES IN INDEX.HTML ===")
bg_imgs = re.findall(r'url\(([^)]+)\)', content)
for i, bg in enumerate(bg_imgs, 1):
    print(f"BG {i}: {bg}")

print("\n=== 3. ICON TAGS (<i>) IN INDEX.HTML ===")
icons = re.findall(r'<i\s+class=["\']([^"\']+)["\']', content)
unique_icons = sorted(list(set(icons)))
print(f"Total icon occurrences: {len(icons)}")
print("Unique icon classes:")
for u in unique_icons:
    print(f"  - {u}")

print("\n=== 4. SECTION COMMENTS AND HEADINGS ===")
sections = re.findall(r'(<!--.*?-->|<section[^>]*>|<h[1-4][^>]*>.*?</h[1-4]>)', content, re.DOTALL)
for s in sections[:40]:
    s_clean = s.strip()
    if len(s_clean) < 120 and ("section" in s_clean.lower() or "h" in s_clean.lower() or "====" in s_clean):
        print(s_clean)
