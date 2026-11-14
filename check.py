# Checks the built site for broken links and missing images.
# Run after build.py:  python check.py

import os
import re
import sys
from urllib.parse import unquote

problems = []
pages = 0

for folder, _, files in os.walk("dist"):
    for name in files:
        if not name.endswith(".html"):
            continue
        pages += 1
        path = os.path.join(folder, name)
        with open(path, encoding="utf-8") as f:
            html = f.read()

        links = re.findall(r'(?:href|src|data-full|poster)="([^"]+)"', html)
        for link in links:
            if link.startswith(("http", "mailto:", "tel:", "#")):
                continue
            target = os.path.join(folder, unquote(link.split("#")[0]))
            if not os.path.exists(target):
                problems.append(f"{path}: missing {link}")

print(f"Checked {pages} pages.")
if problems:
    print(f"Found {len(problems)} problem(s):")
    for p in problems:
        print("  " + p)
    sys.exit(1)
else:
    print("No problems found.")
