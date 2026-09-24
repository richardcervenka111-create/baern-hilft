#!/usr/bin/env python3
"""Write dist/artifact.html: index.html without the document skeleton.

The claude.ai Artifact publisher wraps a page in its own <!doctype>/<head>/<body>,
so it gets only the fragment between the two ARTIFACT FRAGMENT markers.
GitHub Pages serves index.html itself, which stays a complete document.
"""
import re, sys, pathlib
src = pathlib.Path(__file__).resolve().parent.parent / "index.html"
s = src.read_text(encoding="utf-8")
m = re.search(r"<!-- BEGIN ARTIFACT FRAGMENT.*?-->\n(.*)\n<!-- END ARTIFACT FRAGMENT -->", s, re.S)
if not m:
    sys.exit("markers not found in index.html")
frag = m.group(1).replace("</head>\n<body>\n", "", 1)
out = src.parent / "dist" / "artifact.html"
out.parent.mkdir(exist_ok=True)
out.write_text(frag, encoding="utf-8")
print(f"wrote {out} ({len(frag)} bytes)")
