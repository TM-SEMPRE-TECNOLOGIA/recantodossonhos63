import re

with open(r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Common template English terms
english_patterns = [
    r'\bRoom\b', r'\bRooms\b', r'\bAmenities\b', r'\bDiscover\b', r'\bRead More\b',
    r'\bSubscribe\b', r'\bNewsletter\b', r'\bQuick Links\b', r'\bCheck In\b', r'\bCheck Out\b',
    r'\bLuxury\b', r'\bHotel\b', r'\bOur Services\b', r'\bTestimonials\b', r'\bFollow Us\b',
    r'\bAll Rights Reserved\b', r'\bView More\b', r'\bBook Now\b', r'\bSpecial Offers\b',
    r'\bContact Info\b', r'\bPhone\b', r'\bEmail\b', r'\bAddress\b', r'\bNight\b', r'\bPer Night\b',
    r'\bFacilities\b', r'\bAbout Us\b', r'\bGet In Touch\b', r'\bSend Message\b', r'\bSubmit\b',
    r'\bCleanliness\b', r'\bComfort\b', r'\bLocation\b', r'\bService\b', r'\bRating\b',
    r'\bLatest News\b', r'\bBlog\b', r'\bRecent Posts\b', r'\bComments\b', r'\bBy Admin\b',
    r'\bHome\b', r'\bPages\b', r'\bFeatures\b', r'\bGallery\b', r'\bVideo Tour\b',
    r'\bEnjoy\b', r'\bRelax\b', r'\bExperience\b', r'\bWelcome\b'
]

lines = text.splitlines()
matches = []
for idx, line in enumerate(lines, 1):
    # skip html comments or script/style tags if purely technical
    clean = re.sub(r'<script.*?</script>', '', line, flags=re.DOTALL)
    clean = re.sub(r'<!--.*?-->', '', clean)
    for p in english_patterns:
        m = re.search(p, clean, re.IGNORECASE)
        if m:
            matches.append((idx, line.strip()))
            break

print(f"Total lines with potential English copy: {len(matches)}")
for lnum, lcontent in matches[:60]:
    print(f"L{lnum}: {lcontent[:100]}")
