# Builds the site and opens it in the browser.
# Run:  python serve.py      (Arabic)
#       python serve.py en   (English)
# Stop with Ctrl+C.
#
# The AI assistant also works locally if the anthropic package is installed
# (pip install -r requirements.txt) and ANTHROPIC_API_KEY is set on your computer.

import http.server
import json
import os
import socketserver
import sys
import webbrowser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "api")

import build

try:
    from chat import get_reply
except ImportError:
    # anthropic isn't installed: the site works, the chat answers "not available"
    def get_reply(messages):
        return 503, {"error": "not_configured"}


class SiteHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="dist", **kwargs)

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            messages = json.loads(self.rfile.read(length) or b"{}").get("messages")
        except ValueError:
            messages = None
        status, body = get_reply(messages)

        payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


build.main()

lang = "en" if "en" in sys.argv else "ar"

# use the first free port starting from 8766
port = 8766
while True:
    try:
        server = socketserver.TCPServer(("127.0.0.1", port), SiteHandler)
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
