# APIs e integrações das galerias de referência (buscar referências por programa)

Fonte: `docs/achados/rodada-10C.md` §3 e `docs/achados/rodada-C2.md` §3 (27/11/2026, só leitura: nenhuma conta, plano
ou chave foi criado). Use quando o Claude precisar **buscar telas/fluxos de referência sozinho** (por segmento, por
plataforma) em vez de o usuário mandar prints. Galerias para navegação manual e perfis: `learning-sources.md` §5.

Coluna "verificação": **doc** = documentação oficial lida; **página** = só a página pública; **terceiros** = fonte não
oficial (trate como inferência); **não verificado**. Preços e limites mudam: **reconfira antes de assinar**.

## 1. Tabela

| Site | API pública | MCP / conector para IA | RSS / feed | Autenticação | Plano necessário | O que dá para buscar | Serve por segmento? | Verificação |
|---|---|---|---|---|---|---|---|---|
| **Mobbin** | só Team e Enterprise | **Sim**, MCP oficial a partir do **Pro**; o conector já está instalado neste ambiente, mas **as buscas retornam "Mobbin MCP requires a paid plan"** | não verificado | OAuth do conector (claude.ai) | Free sem MCP/API; **Pro US$ 10/mês (anual)**; Team US$ 16/membro/mês (anual) | telas, fluxos e seções por linguagem natural, plataforma iOS/web; URLs de imagem expiram em 30 dias | **sim, com plano pago** | doc (mobbin.com/pricing) + resposta da ferramenta |
| **Refero** | REST não verificado | **Sim**, MCP remoto oficial `https://api.refero.design/mcp` | não verificado | OAuth ou Bearer | Pro, Team ou Lifetime (preços não verificados) | telas e fluxos (125.000+ telas e 8.000+ fluxos, segundo o Product Hunt; não confirmado em doc) | **sim** | doc (doc.refero.design/mcp/getting-started.md) |
| **ScreensDesign** (antigo UI Sources: `uisources.com` redireciona) | não verificado | **Sim**, MCP hospedado `api.screensdesign.com/v1/mcp`, "incluído com o Pro"; cita Claude, Claude Code, Cursor, Codex | não verificado | configurado pelo cliente | Pro (valores não lidos) | apps (2.958+ do topo de faturamento), telas gravadas, fluxos completos, screenshots da App Store, receita e instalações | **sim** (forte em app mobile; cobre melhor financeiro e saúde que marca pessoal e jurídico — inferência da rodada) | página (screensdesign.com/mcp/) |
| **Figma Community** | REST oficial (busca na Community: não encontrada) | **Sim**, MCP oficial `https://mcp.figma.com/mcp` | não verificado | token pessoal ou OAuth 2 | por assento: Enterprise Full/Dev até 600 chamadas/dia; Pro/Org Full/Dev 200/dia; View/Collab 6/mês | **lê o arquivo/frame que você indicar por link**; não busca | parcial | doc (developers.figma.com) |
| **Pinterest** | **Sim**, API v5 (app precisa de aprovação) | não verificado | não verificado | OAuth 2 | gratuita; Trial 1.000 req/dia, Standard 100 req/s | busca de pins por palavra-chave (`GET /v5/search/pins`, segundo terceiros; não confirmada na doc aberta) | parcial (inspiração geral, utilidade para telas de UI incerta) | doc (rate limits) + terceiros |
| **Dribbble** | Sim, API v2 | não verificado | não verificado | OAuth 2 | não verificado | só `/user` e `/user/shots` na doc; **sem busca de shots públicos** | não | doc (developer.dribbble.com/v2/) |
| **Behance** | **Não** ("no longer accepting new clients") | não verificado | não verificado | — | — | — | não | doc (behance.net/dev) |
| **Land-book** | não encontrada | não verificado | **Sim**: `https://land-book.com/rss.xml` e `/feed/` | nenhuma | PRO em promoção (US$ 50/ano na leitura); o que libera: não verificado | novidades (sites), sem filtro por segmento | parcial | página |
| **SiteInspire** | não encontrada | não verificado | **Sim**: `https://www.siteinspire.com/websites/feed` | nenhuma | não verificado | novos sites publicados | parcial | página |
| **Awwwards** | não encontrada | não verificado | não encontrado | — | — | só navegação manual (Latest, Nominees, Collections) | parcial (manual) | página |
| **Page Flows** | não encontrada | não encontrado | não encontrado | login | assinatura (teste "Try 3 Days") | fluxos iOS, Android, web e e-mail em vídeo (manual) | parcial (manual, pago) | página |
| **Godly** (`godly.website` redireciona para **recent.design**) | não verificado | não verificado | não verificado | — | não verificado | galeria com filtros Web, Interface, Branding, Motion, Poster | parcial (manual) | só captura da home |
| **Screenlane** | não verificado | não verificado | não verificado | — | — | — | não verificado | página não abriu |

## 2. Ranking: 5 melhores para buscar referências por programa a partir do Claude Code (rodada C2)
1. **Refero MCP** — único pensado para agentes com busca de telas e fluxos em linguagem natural e suporte declarado ao
   Claude Code. Passo mínimo: assinar (Pro/Team/Lifetime) e
   `claude mcp add --transport http refero https://api.refero.design/mcp --header "Authorization: Bearer <token>"`.
2. **ScreensDesign MCP** — MCP hospedado no Pro; telas reais, fluxos e receita por app. Passo mínimo: assinar o Pro e
   conectar `api.screensdesign.com/v1/mcp` pela página de configuração (~2 min, segundo a página).
3. **Mobbin MCP** — maior acervo de apps reais com busca por plataforma; **já instalado aqui como conector, mas exige
   plano pago (Pro, US$ 10/mês anual)**. Sem o plano, toda busca falha. Passo mínimo: ativar o Pro na conta conectada.
4. **Pinterest API v5** — gratuita, Trial de 1.000 req/dia, precisa de aprovação do app e token OAuth. Inspiração geral.
5. **Land-book / SiteInspire (RSS)** — sem conta; ler os feeds por script. Só novidades, sem filtro por segmento
   (dá para filtrar por palavra-chave no título — inferência).

Fora do ranking: **Figma MCP** não busca, mas lê qualquer arquivo/frame que o usuário apontar por link.
Na 1ª versão do ranking (rodada 10C) o ScreensDesign ainda não aparecia; a ordem acima é a atualizada (C2).
Recomendação da rodada (inferência): assinar **um** dos três MCPs pagos por 1 mês para fechar a galeria por segmento de
uma vez, em vez de captura manual.

## 3. Sem integração: melhor acesso manual
- **Behance** (API fechada), **Dribbble** (API sem busca pública), **Awwwards** (sem feed), **Page Flows** (sem
  API/MCP), **recent.design** e **Screenlane** (não verificados): abrir no navegador e capturar a tela inteira em
  tamanho grande; Page Flows pelo teste de 3 dias.

## 4. Como usar no fluxo (complemento)
1. Antes de chamar um conector, confira se ele responde (no Mobbin, a mensagem "requires a paid plan" significa que a
   conta não tem Pro — não tente de novo; avise o usuário e caia para o acesso manual).
2. Busque por **segmento + plataforma + tela** ("extrato de banco digital iOS", "agenda de clínica web"), 3–5
   resultados, e anote estrutura e decisão, não cor nem logo (`website-ui` → `benchmark-sources.md`, "Como usar sem copiar").
3. Projeto de setor: a skill `segmento-*` correspondente diz quais telas buscar; esta tabela só diz **onde**.
4. Nunca crie conta, assine plano ou gere chave sem o usuário pedir.
