"""Check built Academic Pages output without browser automation."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
required = ["index.html", "research/index.html", "cv/index.html",
            "files/CV_HyunkyuKang.pdf", "assets/css/main.css",
            "assets/css/personal.css", "images/research/affordance-pipeline.png",
            "images/research/temporal-diagnostics.png"]
errors = [f"Missing required file: {p}" for p in required if not (root / p).is_file()]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

documents = {}
for path in root.rglob("*.html"):
    html = path.read_text(encoding="utf-8")
    parser = Links()
    parser.feed(html)
    documents[path] = parser
    for marker in ("Your Name", "none@example.org", "Red Brick University"):
        if marker in html:
            errors.append(f"Template placeholder in {path.relative_to(root)}: {marker}")

checked = 0
for path, parser in documents.items():
    for link in parser.links:
        url = urlsplit(link)
        if url.scheme and url.scheme not in ("http", "https"):
            continue
        if url.netloc and url.netloc != "khk0606.github.io":
            continue
        if not url.path:
            target = path
        elif url.path.startswith("/"):
            target = root / unquote(url.path).lstrip("/")
        else:
            target = path.parent / unquote(url.path)
        target = target.resolve()
        if target.is_dir():
            target = target / "index.html"
        checked += 1
        if not target.is_file():
            errors.append(f"Broken local link in {path.relative_to(root)}: {link}")
        elif url.fragment and target in documents and unquote(url.fragment) not in documents[target].ids:
            errors.append(f"Missing anchor in {path.relative_to(root)}: {link}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(documents)} HTML pages, {checked} local references, required assets, and placeholder checks.")
