import sys, os, re

mid = sys.argv[1]
if not re.fullmatch(r'G-[A-Z0-9]{6,14}', mid):
    raise SystemExit('ID de medicion no valido: ' + mid)

snippet = ('<!-- Google tag (gtag.js) -->\n'
    '<script async src="https://www.googletagmanager.com/gtag/js?id=' + mid + '"></scr' + 'ipt>\n'
    '<scr' + 'ipt>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
    "gtag('js',new Date());gtag('config','" + mid + "');</scr" + 'ipt>')

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for fn in files:
        if not fn.endswith('.html'):
            continue
        p = os.path.join(root, fn)
        t = open(p, encoding='utf-8', errors='ignore').read()
        if 'googletagmanager.com/gtag' in t:
            continue
        m = re.search(r'<head[^>]*>', t)
        if not m:
            continue
        t = t[:m.end()] + '\n' + snippet + t[m.end():]
        open(p, 'w', encoding='utf-8').write(t)
        count += 1
print('Etiqueta GA4 inyectada en', count, 'archivos')
