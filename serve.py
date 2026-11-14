# Builds the site and opens it in the browser.
# Run:  python serve.py      (Arabic)
#       python serve.py en   (English)
# Stop with Ctrl+C.

import http.server
import os
import socketserver
import sys
import webbrowser
from functools import partial

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import build

build.main()

lang = "en" if "en" in sys.argv else "ar"
handler = partial(http.server.SimpleHTTPRequestHandler, directory="dist")

# use the first free port starting from 8766
port = 8766
while True:
    try:
        server = socketserver.TCPServer(("127.0.0.1", port), handler)
        break
    except OSError:
        port += 1

url = f"http://localhost:{port}/{lang}/index.html"
print(f"Site is running at {url}")
print("Press Ctrl+C to stop.")
webbrowser.open(url)

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Stopped.")
    server.server_close()
