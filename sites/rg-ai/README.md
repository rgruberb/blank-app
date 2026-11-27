# Site da RG AI (gruberia.com)

Site estático, pronto para Cloudflare Pages (sem build).

- `index.html`: landing page.
- `portfolio/`: o portfólio (cópia do artifact "RG AI · Portfólio", com o e-mail rafael@gruberia.com).
- `404.html`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `_headers` (cache longo para imagens e vídeo).

## Publicar no Cloudflare Pages

1. Workers & Pages → Create → Pages → conectar este repositório (ou "Upload assets" com esta pasta).
2. Build command: vazio. Output directory: `sites/rg-ai`.
3. Custom domains → `gruberia.com` (e `www.gruberia.com` com redirecionamento).
4. E-mail: Email Routing → `rafael@gruberia.com` encaminhando para a caixa pessoal.
