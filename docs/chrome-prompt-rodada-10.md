# Rodada 10: novos links + pesquisa profunda por segmento (prompt único)

**Modelo:** Opus 5.5 (julga relevância, compara setores e lida com regulação). Cole o prompt abaixo num chat novo do Claude no Chrome, com Instagram e Facebook logados. Se a resposta cortar, responda "continue".

```
Você é um pesquisador sênior de Product Design. Trabalhe com VÁRIAS ABAS ao mesmo tempo: abra os links em lotes de 6 a 8 abas, extraia o que for preciso de cada aba, feche o lote e abra o próximo. Só leia: não curta, não comente, não siga, não entre em grupos, não crie conta, não instale nada.

OBJETIVO
Alimentar uma biblioteca de skills de design para o Claude que vai ganhar uma camada nova, POR SEGMENTO: financeiro, CRM, publicidade, marca pessoal, saúde e jurídico. Cada segmento pede um design diferente. Um app financeiro, por exemplo, pede sobriedade, precisão e confiança; um de marca pessoal pede expressão e personalidade. As skills já cobrem fundamentos de UI/UX, motion, dashboards e plataformas (website, app desktop, app mobile). Agora falta o que é ESPECÍFICO DE CADA SETOR.

======================================================================
PARTE 1: LINKS ENVIADOS (filtrar, classificar, extrair)
======================================================================

PRIORIDADE (faça primeiro):
- https://www.instagram.com/p/DgAOxJbjWZs/  (marcado como URGENTE)
- https://www.instagram.com/p/Df4SUQYHWZA/  (lista repositórios: para CADA repositório citado, informe nome, URL do GitHub, o que faz, licença, estrelas e última atualização, e se é skill/plugin do Claude, biblioteca ou ferramenta. NÃO instale nada; só levante as informações)

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

FILTRO DE DESIGN (obrigatório): só analise posts sobre design de interface (UI, UX, motion, dashboards, apps, sites, design visual, tipografia, cor, componentes, ferramentas de design) ou sobre design de um dos 6 segmentos. Se não for de design, escreva só "FORA DO TEMA: <ID> — <assunto em 1 linha>".

Para cada link de design, um bloco:
### <ID> — @<autor>
- Tipo: carrossel (N slides) | reel | vídeo | site
- Segmento: financeiro | CRM | publicidade | marca pessoal | saúde | jurídico | geral (pode ser mais de um)
- Plataforma: website | app desktop/web app | app mobile
- Legenda: <resumo fiel; cite números e termos técnicos>
- Slide a slide / cena a cena: <texto visível, números, cores (hex aproximado), tipografia, layout, componentes, animações>
- Regras/lições práticas: <lista objetiva>

======================================================================
PARTE 2: PESQUISA PROFUNDA POR SEGMENTO (6 segmentos)
======================================================================

Para CADA segmento, abra várias abas em paralelo e pesquise em fontes oficiais e produtos reais. Cada segmento deve ter de 6 a 10 fontes VERIFICADAS (aberta e lida). Tipos de fonte a buscar:
1. Design systems públicos de empresas do setor. Confira se existem e se são públicos.
2. Produtos líderes do setor: telas públicas, páginas de produto, App Store ou Google Play, estudos de caso.
3. Estudos de caso no Behance, no Dribbble ou de agências, com o raciocínio de design explicado.
4. Regras e regulação que afetam a interface (Brasil primeiro, depois internacional).
5. Artigos do Nielsen Norman Group, Baymard ou similares sobre o setor.

Pontos de partida. Verifique se existem e se servem; descarte e substitua o que não servir:
- FINANCEIRO: design systems e produtos de bancos e fintechs (ex.: Stripe, Wise, Revolut, Nubank, Itaú, Inter); exigências de exibição de taxas, CET e rentabilidade (Banco Central, CVM, Anbima); LGPD; NN/g sobre confiança em finanças.
- CRM: Salesforce Lightning Design System, HubSpot Canvas, Pipedrive, Attio, Linear como referência de densidade; padrões de pipeline, kanban, timeline de contato e tabelas densas.
- PUBLICIDADE: interfaces de gestão de anúncios e campanhas (ex.: Meta Ads Manager, Google Ads), agências e estúdios premiados (Awwwards), tamanhos e especificações de criativos, normas do CONAR e regras de rotulagem de conteúdo patrocinado.
- MARCA PESSOAL: Linktree, Bento, Read.cv ou similares, Notion/Framer para portfólio, criadores; padrões de perfil, portfólio, agenda pública e prova social.
- SAÚDE: NHS Design System, design systems de healthtechs, telas de agendamento, prontuário e teleconsulta; LGPD para dados sensíveis, regras do CFM sobre telemedicina e publicidade médica, ANVISA quando se aplicar; acessibilidade para público idoso.
- JURÍDICO: GOV.UK Design System como referência de clareza; produtos jurídicos (ex.: Clio, Jusbrasil, DocuSign, Projuris) e de assinatura eletrônica; o Provimento OAB 205/2021 sobre publicidade da advocacia (o que um site de escritório pode e não pode ter); linguagem simples (plain language).

Para cada segmento, entregue esta FICHA:
## Segmento: <nome>
1. Tom e personalidade visual: 3 a 5 adjetivos e o que o usuário do setor espera sentir.
2. Paleta típica: cores e hex medidos em produtos reais, com a URL de onde mediu, e cores a evitar.
3. Tipografia típica: famílias usadas por produtos do setor, uso de números tabulares e tamanhos mínimos.
4. Densidade: alta ou baixa, e por quê. Diga se é tabela densa ou cards espaçados.
5. Motion: quanto é aceitável e o que nunca animar (ex.: valores monetários, resultados de exame).
6. Padrões de tela essenciais do setor, com exemplos reais (URL).
7. Dados e números: formato, precisão, unidades, fonte e data, e como mostrar variação ou risco.
8. Confiança e credibilidade: selos, transparência, prova social e o que gera desconfiança.
9. Regulação e conformidade que afetam a interface: regra, órgão, URL e o que muda na tela.
10. Acessibilidade específica do público do setor.
11. Anti-padrões do setor: dark patterns e erros comuns.
12. Diferenças por plataforma: o que muda entre website, app desktop e app mobile neste segmento.
13. Referências verificadas: tabela | nome | URL | tipo (design system / produto / caso / regulação / artigo) | o que aproveitar | status ✅/🔒/❌.

No final da Parte 2, uma tabela comparativa: 6 segmentos × (tom, paleta, densidade, motion, tipografia, regulação-chave).

======================================================================
REGRAS
======================================================================
- Abra cada URL antes de citá-la. Não invente nomes, hex, regras nem números. Se não achar, escreva "não verificado".
- Para regulação, cite a norma e a URL oficial. Não interprete além do que o texto diz.
- Marque com "(inferência)" tudo o que for conclusão sua, e não da fonte.
- Feche as abas de cada lote antes de abrir o próximo, para não perder o contexto.
- Se a resposta ficar longa, entregue em partes e termine cada uma com "CONTINUA": primeiro a Parte 1, depois os segmentos, de 2 em 2.

======================================================================
ENTREGA
======================================================================
Gere 2 arquivos:
1. rodada-10A.md: Parte 1 (links), com um resumo de 5 a 10 linhas no topo e a seção "Repositórios do Df4SUQYHWZA".
2. rodada-10B.md: Parte 2 (6 fichas de segmento + tabela comparativa), com um resumo no topo e "Fontes verificadas" no fim.
Prints: tire print só do que tiver valor visual (telas de produto do setor, paletas, tabelas, regras regulatórias em destaque), no máximo 3 por link ou fonte. Nomeie como 10A_<ID>_<n>.png e 10B_<segmento>_<fonte>_<n>.png.
Se conseguir baixar arquivos, baixe os .md e os prints. Se não conseguir, entregue cada .md num ÚNICO bloco de código Markdown, com uma seção "Prints" listando: nome | URL | o que mostra.
```
