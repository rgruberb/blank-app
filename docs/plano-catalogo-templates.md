# Plano: catálogo de templates por segmento (Artifact)

Status: **aguardando a Rodada 10** (`rodada-10A.md`, `rodada-10B.md` + imagens). Depois que ela chegar, o catálogo é construído.

## Decisões do usuário (27/11/2026)
- **Conteúdo:** o catálogo COMPLETO de referências disponíveis. Os templates não têm número fixo: entram todas as direções visuais relevantes que as referências sustentarem.
- **Ordem:** por data em que a referência foi adicionada, se possível.
- **Saída ao escolher:** um prompt / `CLAUDE.md` pronto para colar no projeto.
- **Prévias:** o próprio usuário escolhe quais plataformas ver: app mobile, app desktop/painel e website/landing (filtro, várias ao mesmo tempo).
- **Quando:** só depois da Rodada 10.

## Estrutura planejada
1. **Navegação:** 6 segmentos (financeiro, CRM, publicidade, marca pessoal, saúde, jurídico) + "Geral".
2. **Referências:** todas as imagens das skills (`assets/visual-refs`) e da galeria da Rodada 10. Cada referência traz:
   - segmento(s), plataforma, autor e fonte (link);
   - data de adição;
   - o que observar.
3. **Filtros e ordem:** filtros por segmento, plataforma e tipo de tela; ordenação por data (mais novas primeiro) ou por segmento.
4. **Templates (direções visuais) por segmento:** derivados das referências e das fichas da Rodada 10. Cada um tem:
   - tokens: paleta com hex, par tipográfico, escala, raio, sombra, densidade e motion;
   - prévias ao vivo, desenhadas a partir dos tokens (mockups originais, não cópia), nas plataformas que o usuário marcar;
   - regras do segmento: tom, o que nunca animar, números, regulação e anti-padrões;
   - as referências que o inspiraram.
5. **Escolha → kit:** botão que gera o prompt / `CLAUDE.md` com a direção escolhida, as plataformas, os tokens em CSS, as regras de UI/UX e quais skills usar (`segmento-*`, plataforma, temas), com "Copiar" e "Baixar .md".
6. **Persistência leve:** lembrar a última escolha e os filtros no navegador. Opcional; a página funciona sem isso.

## Data de adição (como calcular)
1. Data em que o link foi enviado, pelos exports do WhatsApp, quando houver.
2. Senão, a data do commit que adicionou a imagem na repo (`git log --diff-filter=A`).
3. Referências sem data vão para o fim.

## Cuidados técnicos
- **Tamanho:** são centenas de imagens, o que passa do limite de 16 MB da página. Usar o armazenamento de assets do Artifact ou miniaturas otimizadas (~400 px, WebP) com link para a imagem grande.
- **Privacidade:** as imagens são de terceiros. O Artifact fica privado; se for compartilhado, a página avisa que é referência pessoal.
- **Fonte única:** a página lê um `catalogo.json` gerado a partir dos `visual-index.md` e das fichas, para não ficar dessincronizada das skills.
