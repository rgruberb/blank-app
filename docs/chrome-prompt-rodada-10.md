# Rodada 10: 3 prompts em paralelo

Rode os 3 prompts **ao mesmo tempo**, cada um num **chat próprio** da extensão Claude in Chrome, numa aba ou janela separada, com Instagram e Facebook logados. Cada chat também abre várias abas para pesquisar. **Modelo: Opus 5.5 nos três.** Se uma resposta cortar, responda "continue" naquele chat.

| Prompt | Faz | Entrega |
|---|---|---|
| 10A | Os 52 links enviados: filtro, classificação e extração | `rodada-10A.md` + imagens `10A_*` |
| 10B | Pesquisa profunda dos 6 segmentos (fichas + regulação) | `rodada-10B.md` |
| 10C | Galeria de referências por segmento + APIs e integrações dos sites de referência | `rodada-10C.md` + imagens `10C_*` |

---

## Prompt 10A: links enviados

```
Você é um pesquisador sênior de Product Design. Este chat faz SÓ a Parte 1 de uma pesquisa em 3 partes. Outros dois chats, rodando ao mesmo tempo, cuidam da pesquisa por segmento e da galeria. Trabalhe com VÁRIAS ABAS: abra os links em lotes de 6 a 8 abas, extraia o que precisar de cada uma, feche o lote e abra o próximo. Só leia: não curta, não comente, não siga, não entre em grupos, não crie conta, não instale nada.

CONTEXTO
Estes links alimentam uma biblioteca de skills de design para o Claude, organizada por SEGMENTO (financeiro, CRM, publicidade, marca pessoal, saúde, jurídico) e por plataforma (website, app desktop, app mobile). Tudo o que for catalogado recebe um nome e entra num catálogo pesquisável.

PRIORIDADE (faça primeiro):
- https://www.instagram.com/p/DgAOxJbjWZs/  (marcado como URGENTE)
- https://www.instagram.com/p/Df4SUQYHWZA/ e https://www.instagram.com/p/DgDhbRvIG-T/  (listam repositórios do GitHub. Para CADA repositório, abra o GitHub numa aba e informe: nome, URL, o que faz, licença, estrelas, última atualização e se é skill/plugin do Claude, biblioteca ou ferramenta. NÃO instale nada.)

DEMAIS LINKS:
https://www.instagram.com/reel/DgAT3fVBJ8B/
https://www.instagram.com/reel/DgAqhGGDBws/
https://www.instagram.com/reel/DgFUOPxtOJK/
https://www.instagram.com/reel/DgEyy8nRybB/
https://www.instagram.com/p/DfkL5N_H4GK/
https://www.facebook.com/share/v/1e6gnFwAJ5/
https://www.facebook.com/share/1A19QTSisE/
https://www.instagram.com/reel/Deq_kvJBI3g/
https://www.instagram.com/reel/DgI3UF_k_-G/
https://www.instagram.com/reel/DgIYTG0xNrM/
https://www.instagram.com/reel/DgH6J4mgMM4/
https://www.instagram.com/reel/DgI9usSyEJG/
https://www.instagram.com/reel/DgDcYitNEbl/
https://www.instagram.com/reel/Df5J3c6EabL/
https://www.instagram.com/reel/DgHo3AxIw75/
https://www.instagram.com/reel/DgKm0dVT8Km/
https://www.instagram.com/reel/Df1WDAnhbtx/
https://www.instagram.com/reel/DgKvBWTz79O/
https://www.instagram.com/reel/DfnS60YTNL4/
https://www.instagram.com/reel/DfxspuNBjye/
https://www.instagram.com/reel/DgLUGlUORly/
https://www.instagram.com/reel/DgCe3izzZVP/
https://www.facebook.com/share/r/1CpkDzwrqg/
https://www.instagram.com/reel/DgDlMjfhNhc/
https://www.instagram.com/reel/DgM5twdsInO/
https://www.instagram.com/reel/DdAojDaxanF/
https://www.instagram.com/reel/DgNL4KizAjL/
https://www.instagram.com/reel/Df5pCOhmYuP/
https://www.instagram.com/reel/De16ULetFoR/
https://www.instagram.com/reel/DgNqsQrz9tT/
https://www.instagram.com/reel/DgNswztzDX4/
https://www.instagram.com/reel/DgN_gLyKKHN/
https://designeer.xyz/
https://www.instagram.com/reel/DfKlT77NrXV/
https://www.instagram.com/p/DfyBOaVDEar/
https://www.instagram.com/reel/DfZsqywtqTW/
https://www.instagram.com/p/DfJaRP4n8e4/
https://www.instagram.com/reel/DgLbB_lNiAd/
https://www.instagram.com/p/DfpBdb0E2JP/
https://www.instagram.com/p/DgDhbRvIG-T/
https://www.instagram.com/p/DfgxgBNlK59/
https://www.instagram.com/p/DgOzQOLk5m9/
https://www.instagram.com/p/DgNTvDZCMNX/
https://www.instagram.com/p/Dft07xmDJkm/
https://www.instagram.com/reel/DgOXXIOtR2O/
https://www.instagram.com/p/DfzcornCO73/
https://www.instagram.com/p/DfkIW6XFJYu/
https://www.instagram.com/p/DgPLR1SDouB/
https://www.instagram.com/reel/DgQYY6OpZMB/
https://www.instagram.com/reel/DfaFIoNBU39/

FILTRO DE DESIGN (obrigatório): só analise posts sobre design de interface (UI, UX, motion, dashboards, apps, sites, design visual, tipografia, cor, componentes, ferramentas de design) ou sobre design de um dos 6 segmentos. Se não for de design, ou se for só isca de "comente X que te mando" sem conteúdo no post, escreva "FORA DO TEMA: <ID> — <assunto em 1 linha>".

Para cada link de design, um bloco:
### <ID> — @<autor>
- Nome sugerido: <nome curto e descritivo, ex.: "Portal de clínica de fisioterapia — guias de convênio">
- Tipo: carrossel (N slides) | reel | vídeo | site
- Segmento: financeiro | CRM | publicidade | marca pessoal | saúde | jurídico | geral (pode ser mais de um)
- Plataforma: website | app desktop/web app | app mobile
- Componentes mostrados: <lista com nome sugerido para cada um, ex.: "Tab bar com indicador que desliza", "Card de valor com variação">
- Legenda: <resumo fiel; cite números e termos técnicos>
- Slide a slide / cena a cena: <texto visível, números, cores (hex aproximado), tipografia, layout, componentes, animações>
- Regras/lições práticas: <lista objetiva>

IMAGENS (são guardadas como referência)
- Abra o post em TAMANHO GRANDE (post aberto, não a grade). Nunca salve miniatura: largura mínima de 900 px e texto legível. Se não der, anote "sem imagem legível".
- Até 3 imagens por link: os slides ou frames que mostram a tela inteira ou a regra ilustrada. Em reel, pause no frame em que a tela aparece inteira.
- Nome: 10A_<ID>_<n>.png
- Não capture dados pessoais reais de terceiros.

REGRAS
- Abra cada URL antes de citar. Não invente nada; se não achar, escreva "não verificado". Marque com "(inferência)" o que for conclusão sua.
- Se a resposta ficar longa, entregue em partes e termine cada uma com "CONTINUA".

ENTREGA
rodada-10A.md com:
1. Resumo de 5 a 10 linhas no topo.
2. Todos os blocos.
3. Seção "Repositórios" (Df4SUQYHWZA e DgDhbRvIG-T).
4. Lista "Fora do tema".
5. Tabela de imagens: | arquivo | ID | segmento | plataforma | autor | URL exata (carrossel com ?img_index=N; reel com o segundo do vídeo) | o que mostra | componentes |
Baixe o .md e as imagens. Se não conseguir baixar, entregue o .md num ÚNICO bloco de código Markdown, com a tabela de imagens completa.
```

---

## Prompt 10B: pesquisa profunda por segmento

```
Você é um pesquisador sênior de Product Design. Este chat faz SÓ a Parte 2 de uma pesquisa em 3 partes. Outros dois chats, rodando ao mesmo tempo, cuidam dos links enviados e da galeria de imagens. Trabalhe com VÁRIAS ABAS: em cada segmento, abra de 6 a 8 fontes em abas paralelas, leia, feche e passe para o próximo segmento. Só leia: não crie conta, não assine nada.

OBJETIVO
Criar uma camada de skills POR SEGMENTO: financeiro, CRM, publicidade, marca pessoal, saúde e jurídico. Cada segmento pede um design diferente. Um app financeiro, por exemplo, pede sobriedade, precisão e confiança; um de marca pessoal pede expressão e personalidade. As skills já cobrem fundamentos de UI/UX, motion, dashboards e plataformas (website, app desktop, app mobile). Agora falta o que é ESPECÍFICO DE CADA SETOR.

FONTES (de 6 a 10 VERIFICADAS por segmento, abertas e lidas)
1. Design systems públicos de empresas do setor. Confira se existem e se são públicos.
2. Produtos líderes: páginas de produto, App Store ou Google Play, estudos de caso.
3. Estudos de caso no Behance, no Dribbble ou de agências, com o raciocínio de design explicado.
4. Regulação que afeta a interface (Brasil primeiro, depois internacional).
5. Nielsen Norman Group, Baymard ou similares sobre o setor.

Pontos de partida. Verifique se existem e se servem; descarte e substitua o que não servir:
- FINANCEIRO: design systems e produtos de bancos e fintechs (ex.: Stripe, Wise, Revolut, Nubank, Itaú, Inter); exibição de taxas, CET e rentabilidade (Banco Central, CVM, Anbima); LGPD; NN/g sobre confiança em finanças.
- CRM: Salesforce Lightning Design System, HubSpot Canvas, Pipedrive, Attio, Linear como referência de densidade; padrões de pipeline, kanban, timeline de contato e tabelas densas.
- PUBLICIDADE: gestão de anúncios e campanhas (ex.: Meta Ads Manager, Google Ads), agências e estúdios premiados (Awwwards), tamanhos e especificações de criativos, normas do CONAR e rotulagem de conteúdo patrocinado.
- MARCA PESSOAL: Linktree, Bento, Read.cv ou similares, Notion/Framer para portfólio, criadores; padrões de perfil, portfólio, agenda pública e prova social.
- SAÚDE: NHS Design System, design systems de healthtechs, agendamento, prontuário e teleconsulta; LGPD para dados sensíveis, CFM (telemedicina e publicidade médica), ANVISA quando se aplicar; acessibilidade para público idoso.
- JURÍDICO: GOV.UK Design System como referência de clareza; produtos jurídicos (ex.: Clio, Jusbrasil, DocuSign, Projuris) e de assinatura eletrônica; Provimento OAB 205/2021 sobre publicidade da advocacia; linguagem simples (plain language).

FICHA POR SEGMENTO
## Segmento: <nome> (código: FIN | CRM | PUB | MPE | SAU | JUR)
1. Tom e personalidade visual: 3 a 5 adjetivos e o que o usuário espera sentir.
2. Paleta típica: hex medidos em produtos reais, com a URL de onde mediu, e cores a evitar.
3. Tipografia típica: famílias, números tabulares e tamanhos mínimos.
4. Densidade: alta ou baixa, e por quê.
5. Motion: quanto é aceitável e o que nunca animar.
6. Padrões de tela essenciais, com exemplos reais (URL).
7. Dados e números: formato, precisão, unidades, fonte e data, variação e risco.
8. Confiança e credibilidade.
9. Regulação e conformidade que afetam a interface: regra, órgão, URL e o que muda na tela.
10. Acessibilidade específica do público.
11. Anti-padrões e dark patterns do setor.
12. Diferenças por plataforma: website × app desktop × app mobile.
13. Direções visuais possíveis: de 2 a 4 "templates" com nome sugerido (ex.: "Sóbrio institucional", "Fintech moderna", "Trading denso"). Cada um com paleta, tipografia, densidade, motion e as fontes que o sustentam.
14. Componentes característicos do setor: lista com nome sugerido e descrição curta (ex.: "Card de saldo com variação", "Linha do tempo do processo").
15. Referências verificadas: | nome | URL | tipo | o que aproveitar | status ✅/🔒/❌ |

No final, uma tabela comparativa: 6 segmentos × (tom, paleta, densidade, motion, tipografia, regulação-chave).

REGRAS
- Abra cada URL antes de citar. Não invente nomes, hex, normas nem números; se não achar, escreva "não verificado".
- Para regulação, cite a norma e a URL oficial, sem interpretar além do texto. Marque com "(inferência)" o que for conclusão sua.
- Entregue em partes, de 2 em 2 segmentos, terminando cada uma com "CONTINUA".

ENTREGA
rodada-10B.md: resumo no topo, as 6 fichas, a tabela comparativa e "Fontes verificadas" no fim. Baixe o arquivo. Se não conseguir, entregue-o num ÚNICO bloco de código Markdown. Não precisa de imagens: a galeria é feita por outro chat.
```

---

## Prompt 10C: galeria de referências + APIs e integrações

```
Você é um pesquisador sênior de Product Design. Este chat faz SÓ a Parte 3 de uma pesquisa em 3 partes: a GALERIA DE REFERÊNCIAS VISUAIS por segmento e o levantamento de APIS E INTEGRAÇÕES dos sites de referência. Outros dois chats, rodando ao mesmo tempo, cuidam dos links enviados e das fichas de segmento. Trabalhe com VÁRIAS ABAS em paralelo. Só leia: não crie conta, não assine plano, não gere chave de API.

PARTE 3.1: GALERIA (as imagens viram referências permanentes de um catálogo pesquisável)
Segmentos: financeiro (FIN), CRM, publicidade (PUB), marca pessoal (MPE), saúde (SAU) e jurídico (JUR).
META: no mínimo 10 telas por segmento (60 no total), cobrindo website, app desktop e app mobile sempre que existir.

Onde buscar: páginas públicas de produtos líderes de cada setor, design systems públicos, estudos de caso (Behance, Dribbble, sites de agências), Awwwards, Land-book, SiteInspire, Mobbin (se houver algo público) e App Store / Google Play (capturas oficiais).

O QUE CAPTURAR
- Telas reais: home, dashboard, lista ou tabela, detalhe, formulário, onboarding, checkout ou pagamento, agenda, mensagens, configurações e estados vazio ou de erro.
- Componentes marcantes: card de valor, gráfico, tabela densa, selo de confiança, aviso regulatório, perfil e portfólio.
- Páginas de design system com tokens de cor, tipografia ou motion.

QUALIDADE
- Abra em TAMANHO GRANDE: shot em tela cheia, página na largura normal ou captura da loja aberta. NUNCA salve miniatura: largura mínima de 900 px e texto legível.
- Um print por tela; recorte só a interface quando der.
- Não capture dados pessoais reais de terceiros.

NOME E FICHA
- Arquivo: 10C_<segmento>_<produto-ou-fonte>_<tela>_<n>.png  (ex.: 10C_FIN_wise_extrato_1.png)
- Ficha de cada imagem:
  | arquivo | nome sugerido | segmento | plataforma | produto/autor | URL exata | tipo de tela | componentes (com nome sugerido) | o que observar | como adaptar sem copiar | data de publicação (se houver) |

PARTE 3.2: APIS E INTEGRAÇÕES DOS SITES DE REFERÊNCIA
Quando um site de referência NÃO mostrar as referências livremente (exige login, mostra só miniatura, bloqueia com anti-bot ou limita sem conta), NÃO contorne o bloqueio. Verifique se o site oferece uma forma oficial de buscar referências por programa. Cubra pelo menos: Mobbin, Dribbble, Behance, Awwwards, Land-book, SiteInspire, Pinterest, Figma Community, Refero, Screenlane, Page Flows, Godly e UI Sources, mais qualquer outro que você encontrar durante a galeria.

Para cada site, abra a documentação oficial (developers, API docs, help center) e informe:
| site | bloqueio encontrado | tem API pública? (link da doc) | tem MCP / conector para IA? | tem RSS ou feed? | tem export ou embed? | autenticação (nenhuma / chave / OAuth) | preço / plano necessário | o que dá para BUSCAR (telas, apps, fluxos, por palavra-chave? por categoria?) | limites e termos de uso relevantes (rate limit, uso permitido) | serve para buscar referências por segmento? (sim / parcial / não) |

No final da Parte 3.2:
- Ranking das 5 melhores opções para buscar referências por programa a partir do Claude Code, com o motivo.
- Para cada uma, o passo mínimo para conectar (ex.: "gerar token em X", "instalar MCP Y"), sem gerar nada.
- Sites sem nenhuma integração oficial: liste e diga qual é o acesso manual mais eficiente.

REGRAS
- Abra cada URL antes de citar. Não invente endpoints, preços nem limites; se não achar, escreva "não verificado".
- Não contorne login, paywall nem anti-bot. Não use APIs não oficiais.
- Marque com "(inferência)" o que for conclusão sua. Se a resposta ficar longa, entregue em partes terminando com "CONTINUA": primeiro a galeria, 2 segmentos por vez, e por último as APIs.

ENTREGA
rodada-10C.md com:
1. Resumo no topo.
2. Galeria por segmento, com as fichas.
3. Tabela de APIs e integrações, ranking e passos.
4. "Fontes verificadas".
Baixe o .md e todas as imagens 10C_*, de preferência numa pasta por segmento. Se não conseguir baixar, entregue o .md num ÚNICO bloco de código Markdown, com a URL exata de cada imagem na ficha.
```
