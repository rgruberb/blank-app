# Plano: catálogo de templates por segmento (Artifact)

Status: **aguardando a Rodada 10**. Plano atualizado em 27/11 com componentes avulsos, nomes e busca. (`rodada-10A.md`, `rodada-10B.md` + imagens). Depois que ela chegar, o catálogo é construído.

## Decisões do usuário (27/11/2026)
- **Conteúdo:** o catálogo COMPLETO de referências disponíveis. Os templates não têm número fixo: entram todas as direções visuais relevantes que as referências sustentarem.
- **Ordem:** por data em que a referência foi adicionada, se possível.
- **Saída ao escolher:** um prompt / `CLAUDE.md` pronto para colar no projeto.
- **Prévias:** o próprio usuário escolhe quais plataformas ver: app mobile, app desktop/painel e website/landing (filtro, várias ao mesmo tempo).
- **Quando:** só depois da Rodada 10.
- **Componentes avulsos (27/11):** além de um template inteiro, o usuário pode escolher componentes soltos (ex.: um card de valor, uma tab bar, um toast, um padrão de tabela) e misturar com o template ou usar sem ele.
- **Nomes e busca (27/11):** TUDO tem nome único e pesquisável (segmentos, templates, componentes e referências).

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
5. **Componentes avulsos:** uma aba "Componentes" com todos os componentes catalogados (vindos dos templates, das skills e das referências). Cada um tem:
   - nome, categoria (navegação, dados, formulário, feedback, motion, layout…), segmentos e plataformas;
   - prévia ao vivo;
   - regras de UI/UX: alvos, estados, motion, acessibilidade, anti-padrões;
   - tokens que usa e referências de origem.
   O usuário marca vários ("carrinho de seleção"), e eles entram no kit junto com o template, ou sozinhos.
6. **Escolha → kit:** botão que gera o prompt / `CLAUDE.md` com a direção escolhida, as plataformas, os tokens em CSS, as regras de UI/UX e quais skills usar (`segmento-*`, plataforma, temas), com "Copiar" e "Baixar .md".
7. **Persistência leve:** lembrar a última escolha e os filtros no navegador. Opcional; a página funciona sem isso.

## Nomes e busca
- **Todo item tem um nome legível e um código estável**, usado no prompt gerado para o Claude saber exatamente o que foi escolhido:
  - Segmento: `FIN` financeiro, `CRM`, `PUB` publicidade, `MPE` marca pessoal, `SAU` saúde, `JUR` jurídico, `GER` geral.
  - Template: `TPL-FIN-01 · Sóbrio institucional`.
  - Componente: `CMP-NAV-03 · Tab bar com indicador que desliza`.
  - Referência: `REF-0123 · Vaulto, finance dashboard (@shohan.designs)`.
- **Busca única** (campo no topo, atalho `/` ou `⌘K`) por nome, código, segmento, plataforma, categoria, autor, cor (hex) e tag.
- **Filtros combinados** com a busca. Resultados agrupados por tipo: templates, componentes e referências.
- **Os nomes ficam registrados no `catalogo.json`.** Se o mesmo nome for usado nas skills, o prompt gerado pode citar `TPL-…`/`CMP-…`/`REF-…` e o Claude acha a regra correspondente.

## Data de adição (como calcular)
1. Data em que o link foi enviado, pelos exports do WhatsApp, quando houver.
2. Senão, a data do commit que adicionou a imagem na repo (`git log --diff-filter=A`).
3. Referências sem data vão para o fim.

## Cuidados técnicos
- **Tamanho:** são centenas de imagens, o que passa do limite de 16 MB da página. Usar o armazenamento de assets do Artifact ou miniaturas otimizadas (~400 px, WebP) com link para a imagem grande.
- **Privacidade:** as imagens são de terceiros. O Artifact fica privado; se for compartilhado, a página avisa que é referência pessoal.
- **Fonte única:** a página lê um `catalogo.json` gerado a partir dos `visual-index.md` e das fichas, para não ficar dessincronizada das skills. O `catalogo.json` também guarda códigos, nomes, tags e datas dos templates, componentes e referências, e é versionado na repo.

## Interface aprovada (27/11/2026)
- **Topo:** busca única (`⌘K` / `/`) em nomes, códigos, segmento, autor, hex e tags, com resultados agrupados por tipo. À direita, o ícone do kit com o contador.
- **Coluna esquerda:** segmentos (FIN, CRM, PUB, MPE, SAU, JUR, Geral) com a contagem de itens; filtros por tipo de tela e por categoria de componente.
- **Centro:**
  - abas Templates · Componentes · Referências;
  - botões de plataforma (Mobile, Desktop, Website), vários ao mesmo tempo;
  - ordenação: mais recentes (padrão), segmento ou nome;
  - cards com prévia ao vivo, código, nome, faixa de cores e botão "+".
- **Coluna direita, o kit:** 1 template + N componentes; avisa quando há conflito entre segmentos; botão "Gerar prompt".
- **Detalhe:** painel lateral com prévia grande alternável, tokens copiáveis, regras do segmento e as referências que inspiraram.
- **Gerar prompt:** modal com o `CLAUDE.md` (segmento, plataformas, template, componentes por código, tokens CSS, regras, skills a abrir), com Copiar e Baixar .md.
- **Comportamento:**
  - kit e filtros salvos no navegador;
  - prévias são mockups originais a partir dos tokens; imagens reais só na aba Referências, em miniatura com link;
  - motion pelas nossas regras (1 momento: a entrada da prévia; reduced motion respeitado).
- **Visual do catálogo:** neutro, claro/escuro seguindo o sistema, para não competir com as cores dos templates.
- **Mobile:** filtros numa folha deslizante, kit numa barra fixa embaixo, busca no topo.
