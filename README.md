# academia-iso-web

Web estática de venta de los cursos ISO de Academia ISO (ES + PT-BR). Sin frameworks
ni build tools: HTML + CSS inline + JS vanilla. Cada página de curso termina en el
checkout de Hotmart.

**URL actual (GitHub Pages):** https://groguer1.github.io/academia-iso-web/

## Estructura

- `/` home ES · `/pt/` home PT-BR
- `/curso-iso-9001|14001|27001|45001|42001/` páginas de venta ES
- `/pt/curso-iso-45001|42001/` páginas de venta PT-BR (adaptación brasileña, no traducción)
- `/blog/` + `/pt/blog/` artículos SEO
- `sitemap.xml`, `robots.txt`, `404.html`, `favicon.svg`, `assets/og/` (imágenes sociales)

## Migración a dominio propio (cuando David compre el dominio)

1. Crear el fichero `CNAME` en la raíz del repo con el dominio (una sola línea, ej. `academiaiso.com`):
   ```
   echo "academiaiso.com" > CNAME
   ```
2. En el DNS del dominio: registros `A` de GitHub Pages (185.199.108.153 /109/110/111)
   o un `CNAME` de `www` a `groguer1.github.io`, según se use apex o www.
3. En GitHub → Settings → Pages: poner el custom domain y activar *Enforce HTTPS*.
4. **Actualizar la BASE_URL en todos los ficheros** (canonical, hreflang, og:url, sitemap,
   robots). Todo el sitio usa la constante `https://groguer1.github.io/academia-iso-web` de forma literal, así que basta un
   reemplazo global:
   ```
   grep -rl 'groguer1.github.io/academia-iso-web' . | xargs sed -i '' 's|https://groguer1.github.io/academia-iso-web|https://DOMINIO-NUEVO|g'
   ```
   (en Linux, `sed -i` sin `''`). Tras el cambio, verificar canonical y sitemap y
   reenviar el sitemap en Search Console.

<!-- CNAME pendiente: crear cuando se compre el dominio (paso 1 de arriba). -->
