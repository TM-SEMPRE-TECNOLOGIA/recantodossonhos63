import re

with open(r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
for m in pattern.finditer(html):
    src = m.group(1)
    start = max(0, m.start() - 300)
    end = min(len(html), m.end() + 300)
    context = html[start:end]
    clean = ' '.join(re.sub(r'<[^>]+>', ' ', context).split())
    if any(k in clean.lower() for k in ['travessia', 'barco', 'rio', 'praia']) or any(k in src.lower() for k in ['acomodacoes', 'quarto', 'suite', 'chale']):
        print(f"SRC: {src}")
        print(f"TEXT: {clean[:140]}...\n")
