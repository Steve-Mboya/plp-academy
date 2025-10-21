TutorFind — static demo (React + Babel in-browser)

Files created under /mnt/data/tutor_app:
- index.html   (single-file demo; React + Babel from CDN; contains JSX)
- styles.css   (plain CSS used by the demo)
- README.txt   (this file)

How to preview locally (three options):

Option A — Open file directly (quick):
1. Download the index.html and styles.css to your machine (links provided below).
2. Double-click index.html to open it in your browser.
   - Note: direct-opening works for this demo because all assets are CDN links.
   - Some browsers restrict local file access; if something fails, use option B below.

Option B — Serve with a simple local server (recommended):
1. In a terminal, `cd` into the folder containing index.html.
2. Run (Python 3):

   python -m http.server 8000

3. Open http://localhost:8000 in your browser.

Option C — Run from a Jupyter notebook (you are already in one):
Run this in a notebook cell (the server will block that cell while running):

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
os.chdir('/path/to/tutor_app')
HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler()).serve_forever()

Then open http://localhost:8000 in your browser.

Notes:
- This demo uses Babel in the browser for simplicity — it's for development and demos only. For production, use a proper build step (Vite, Webpack, Create React App, etc.).
- The app is intentionally minimal and uses local, in-memory data only.
