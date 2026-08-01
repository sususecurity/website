import re, io
p = "index.html"
h = io.open(p, encoding="utf-8").read()
old = (
 '<link rel="icon" type="image/png" href="/icon.png">\n'
 '<link rel="shortcut icon" type="image/png" href="/icon.png">\n'
 '<link rel="apple-touch-icon" href="/icon.png">'
)
new = "\n".join([
 '<link rel="icon" href="/favicon.ico" sizes="any">',
 '<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">',
 '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">',
 '<link rel="icon" type="image/png" sizes="192x192" href="/icon512.png">',
 '<link rel="icon" type="image/png" sizes="512x512" href="/icon512.png">',
 '<link rel="shortcut icon" type="image/png" href="/favicon-32x32.png">',
 '<link rel="apple-touch-icon" sizes="180x180" href="/icon512.png">',
 '<link rel="manifest" href="/site.webmanifest">',
 '<meta name="theme-color" content="#0b2545">',
])
assert old in h, "anchor not found"
io.open(p, "w", encoding="utf-8").write(h.replace(old, new))
print("patched")
