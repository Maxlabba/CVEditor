"""Build index.html: one self-contained file with the fonts and keyword checker inlined.

Usage:  python build.py
Edit src/template.html and src/keywords.js, then rebuild. No packages needed.
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
FONTS = [  # (CSS family used in the page, file, weight, style)
    ("CVSerif", "Lora-Regular", 400, "normal"),
    ("CVSerif", "Lora-Bold", 700, "normal"),
    ("CVSerif", "Lora-Italic", 400, "italic"),
    ("CVSans", "Carlito-Regular", 400, "normal"),
    ("CVSans", "Carlito-Bold", 700, "normal"),
    ("CVHead", "Poppins-Bold", 700, "normal"),
]

def font_css():
    out = []
    for fam, name, weight, style in FONTS:
        data = base64.b64encode((SRC / "fonts" / f"{name}.woff").read_bytes()).decode()
        out.append(f'@font-face{{font-family:"{fam}";src:url(data:font/woff;base64,{data}) format("woff");font-weight:{weight};font-style:{style}}}')
    return "\n".join(out)

html = (SRC / "template.html").read_text(encoding="utf-8")
html = html.replace("/*FONTS*/", font_css()).replace("/*KW*/", (SRC / "keywords.js").read_text(encoding="utf-8"))
(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"index.html written ({len(html) // 1024} KB)")
