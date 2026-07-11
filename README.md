# academia-iso-web — cursosiso.com

Web estática de venta de los cursos ISO de Academia ISO / Isotecnia (ES + PT-BR).
Sin frameworks ni build tools: HTML + CSS inline + JS vanilla. Cada página de
curso termina en el checkout de Hotmart.

**Dominio:** https://cursosiso.com/ (custom domain de GitHub Pages, fichero `CNAME` en la raíz;
comprado en Porkbun el 11/07/2026)

## Estructura

- `/` home ES · `/pt/` home PT-BR
- `/curso-iso-9001|14001|27001|45001|42001/` páginas de venta ES
- `/pt/curso-iso-45001|42001/` páginas de venta PT-BR (adaptación brasileña, no traducción)
- `/blog/` + `/pt/blog/` artículos SEO
- `sitemap.xml`, `robots.txt`, `404.html`, `favicon.svg`, `assets/og/` (imágenes sociales)

## DNS (configurado en Porkbun)

- 4 registros `A` en el apex: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- `CNAME` de `www` → `groguer1.github.io`
- En GitHub → Settings → Pages: custom domain `cursosiso.com` + *Enforce HTTPS*.

## Si algún día cambia el dominio

Todas las URLs absolutas (canonical, hreflang, og:url, sitemap, robots) usan
`https://cursosiso.com` de forma literal. Reemplazo global:
```
grep -rl 'cursosiso.com' . | xargs sed -i '' 's|https://cursosiso.com|https://DOMINIO-NUEVO|g'
```
(en Linux, `sed -i` sin `''`). Actualizar también `CNAME`, y reenviar el sitemap
en Search Console.
