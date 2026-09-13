import re

with open(r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    m = re.search(r'src=["\']([^"\']+\.(?:jpg|png|jpeg|webp)[^"\']*)["\']', line)
    if m:
        print(f"Line {idx}: {m.group(1)}")
