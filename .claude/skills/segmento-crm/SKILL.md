---
name: segmento-crm
description: 'Camada de SEGMENTO CRM (código CRM) para qualquer produto de gestão de clientes e vendas — CRM, pipeline, funil de vendas, leads, contas, atividades, tarefas comerciais e relatórios de metas. Traz tom eficiente e denso, paleta medida (neutros frios + cor só para ação e estado: Attio, Linear, Pipedrive, HubSpot), Inter + mono, densidade alta, o que nunca animar (reordenar linhas lidas, atrasar atalho), números do funil (soma por etapa, probabilidade, data prevista), histórico auditável, LGPD no registro do contato, 4 templates TPL-CRM e 16 componentes CMP-CRM, diferenças website × desktop × mobile e ponteiros para as skills de plataforma e tema. Use quando falarem em "CRM", "pipeline", "funil de vendas", "kanban de negócios", "deals", "gestão de clientes", "leads", "lead scoring", "contatos", "contas", "oportunidades", "linha do tempo do cliente", "follow-up", "vendas B2B", "time comercial", "SDR" ou "gestão de carteira de clientes".'
---

# segmento-crm (CRM)

Skill de **segmento**: o que muda quando a pessoa usa a ferramenta o dia todo para acompanhar clientes, negócios e
atividades. Vale para qualquer CRM ou módulo comercial; não descreve nenhum app específico. Fonte principal: pesquisa
10B (27/11/2026; hex por `getComputedStyle` em páginas de marketing, nenhum produto logado) e galeria 10C/C2/C4/10A.
**(inferência)** = conclusão da pesquisa, não da fonte.

## Código do segmento
`CRM`. Templates `TPL-CRM-01…04` (`references/templates.md`), componentes `CMP-CRM-01…16`
(`references/componentes.md`), imagens em `assets/visual-refs/` (índice: `references/visual-index.md`).

## Quando usar
- Lista/tabela de registros, pipeline kanban, perfil do contato com linha do tempo, painel lateral de detalhes,
  paleta de comandos, relatórios e metas, captura de lead, app de vendedor em campo, site de produto de CRM.
- Junto com a skill de plataforma (desktop é a superfície principal) e `dashboard-ui` para relatórios.
- Não use para o financeiro do cliente (→ `segmento-financeiro`).

## Prioridade (quando as regras conflitam)
1. Skill de **app específico** (se houver) > 2. **segmento** (esta) > 3. **plataforma** (`desktop-app-ui`,
`mobile-app-ui`, `website-ui`) > 4. **tema** (`dashboard-ui`, `ux-patterns`, `ui-motion`, `design-direction`) >
5. **skills de terceiros** (`ext-*`: só implementação, com os valores acima).
Esta skill decide **cor, densidade, números do funil, o que não animar e o que a LGPD pede**; shell, breakpoints e
teclado vêm de `desktop-app-ui`. Densidade alta **não** reduz alvos: no mobile continuam 44pt/48dp com 8px entre
alvos, e na web o piso de 24px (meta 44px na ação principal) de `ux-patterns`; o que encolhe é padding de linha e texto
secundário, não a área clicável.

## Tom e personalidade
- Eficiente, denso, neutro, rápido, previsível. O usuário quer controle e velocidade em trabalho repetitivo (inferência).
- Confiança = dado correto e **histórico auditável** (quem alterou, quando) (inferência); Salesforce destaca "Trust" no
  rodapé do design system.

## Regras centrais (com números)
**1. Paleta — neutros frios em quase todo o espaço; cor só para ação e estado.** Medidos (10B):
| Produto | Ação/marca | Estado | Texto / neutros |
|---|---|---|---|
| Attio | azul `#266DF0`, roxo `#9B69FF` | verde `#007D53` / `#E0FCED` | `#242629`, `#101112`, `#505155`, `#75777C`, `#CDCED2`, `#ECECED` |
| Linear (escuro) | — | verde `#27A644`, vermelho `#F34E52` | fundos `#0F1011`, `#08090A`; texto `#F7F8F8`, `#D0D6E0`, `#8A8F98`, `#62666D` |
| Pipedrive | roxo `#6861F2`, amarelo `#FFDE00` | verde `#017737`, `#D7F9D3`, `#F3FCF2` | `#192435`, azul-petróleo `#27455C` |
| HubSpot | laranja `#FF4800` | — | `#1F1F1F`; verde-escuro `#061C1D`, `#124548`; fundos `#FCFCFA`, `#F8F5EE` |
- **Evite** (inferência): fundo saturado em tabela; verde/vermelho como único diferenciador de status. Azul Salesforce:
  **não medido**. Hex de marketing podem diferir do produto logado.

**2. Tipografia.** **Inter** domina (Attio `Inter`/`Inter Display`, Linear `Inter Variable`, Pipedrive `Inter` +
`Haffer`; HubSpot `HubSpot Sans` + `HubSpot Serif`) + **mono para IDs e códigos** (`JetBrains Mono`, `Berkeley Mono`).
- Corpo **16px** (escala geral de app, decisão do projeto). Linha de tabela densa **13–14px**, alinhada às células do
  `desktop-app-ui` (decisão do usuário, por legibilidade em uso prolongado), com **modo compacto opcional de 12px**
  (densidade compacta/confortável escolhida pelo usuário; 12px é o piso). Escala **1,2**
  (`desktop-app-ui` regra 3). `tabular-nums` em valores, contagens e datas em coluna; valores alinhados à direita.

**3. Densidade: alta.** Muitos registros por sessão; trocar de contexto custa (inferência). Salesforce SLDS 2: UI
flexível com temas e caminho para dark mode (✅). Abrir registro **sem perder o contexto** (painel lateral, não página
nova) (`desktop-app-ui/references/desktop-patterns.md` §7; NN/g data-tables em `ux-patterns`).

**4. Motion.** Aceitável: arrastar cartão no kanban, abrir painel lateral, destacar linha atualizada (tokens de
`ui-motion`: painel 350 ms, reorder com lift 105%). **Nunca animar** (inferência): reordenar linhas enquanto o usuário
lê; contadores do pipeline ao filtrar; nada que atrase atalho de teclado. Durações nos produtos: não verificado.

**5. Dados e números.**
- Valor de negócio em moeda local; **soma por etapa** + **nº de negócios** no cabeçalho da coluna (Pipedrive:
  "$14,400 · 3 deals"; total do funil "$51,300 · 10 deals"); probabilidade % e **data prevista de fechamento**.
- Datas relativas ("há 3 dias") com data completa no hover; abreviação (R$ 1,2 mi) só com valor exato acessível (inferência).
- Toda métrica de relatório com **período** e **"atualizado em"** (inferência). KPI com variação com sinal (Conceptzilla
  "42 ↗12%").

**6. Confiança e histórico.** Linha do tempo de atividades no contato; "ver histórico de propriedade/associação"
(menu do card HubSpot); exclusão em massa com desfazer; quem alterou o quê (inferência). No site: linha de confiança
sob o CTA (nota de avaliação, "sem cartão", SOC 2 & GDPR — Pipedrive) e selo de prêmio (G2, HubSpot).

**7. Regulação (resumo; detalhe em `references/regulacao.md` — não é aconselhamento jurídico).** LGPD: registrar
**origem, data e texto do consentimento** no contato (art. 8º); aviso de privacidade acessível no formulário de captura
(art. 9º); "exportar dados do contato" e "eliminar/anonimizar" (art. 18); campos opcionais marcados e nada além do
necessário (art. 6º). Marketing por e-mail/WhatsApp: **não verificado**.

**8. Acessibilidade.** Uso prolongado por profissional (inferência): contraste confortável, **foco visível**,
**navegação completa por teclado** com atalhos e ⌘K; tabela com cabeçalho semântico; status com texto + ícone + cor
(`desktop-app-ui` regras 4–6). Verificação nos produtos: não feita.

## Diferenças por plataforma
| Plataforma | Papel no CRM | Abra |
|---|---|---|
| **App desktop** | **superfície principal**: tabela, kanban, atalhos, painéis, relatórios | `../desktop-app-ui/SKILL.md` regras 1, 3–7, 10; `../desktop-app-ui/references/desktop-patterns.md` §3, §6, §7; `../dashboard-ui/references/layout-patterns.md` §1–2 |
| **App mobile** | consulta rápida, registrar atividade, ligação/WhatsApp, tarefas do dia (inferência) | `../mobile-app-ui/SKILL.md` regras 2, 3, 11; `../mobile-app-ui/references/mobile-patterns.md` §4, §16 |
| **Website** | marketing + onboarding: mock do app na 1ª dobra, linha de confiança, preços | `../website-ui/SKILL.md` regras 4, 6, 12; `../website-ui/references/website-patterns.md` §1, §2, §4 |

## Templates (direções visuais) — tokens em `references/templates.md`
| Código | Nome | Base |
|---|---|---|
| `TPL-CRM-01` | Produtividade escura | `#0F1011`, texto `#F7F8F8`/`#D0D6E0`, acento verde `#27A644`, Inter Variable + mono (Linear) |
| `TPL-CRM-02` | Clara e fluida | branco/`#ECECED`, texto `#242629`, azul `#266DF0`, roxo `#9B69FF`, Inter + mono (Attio) |
| `TPL-CRM-03` | Funil amigável | branco, texto `#192435`, roxo `#6861F2`, verde `#017737`, kanban em destaque (Pipedrive) |
| `TPL-CRM-04` | Plataforma corporativa | neutros + laranja `#FF4800` (HubSpot) ou azul Salesforce (não medido); muitos módulos |

## Componentes característicos — detalhe em `references/componentes.md`
| Código | Nome | Código | Nome |
|---|---|---|---|
| `CMP-CRM-01` | Tabela densa com visões salvas | `CMP-CRM-09` | Gerenciador de consentimento LGPD |
| `CMP-CRM-02` | Cartão de negócio | `CMP-CRM-10` | Card de contato com ações rápidas |
| `CMP-CRM-03` | Coluna de pipeline com soma | `CMP-CRM-11` | Pontuação de lead |
| `CMP-CRM-04` | Linha do tempo do contato | `CMP-CRM-12` | Caixa de IA (pergunta, resumo, checklist) |
| `CMP-CRM-05` | Painel lateral de detalhes | `CMP-CRM-13` | Trilho de integrações |
| `CMP-CRM-06` | Badge de etapa/estado | `CMP-CRM-14` | Cartão de tarefa (mobile) |
| `CMP-CRM-07` | Barra de filtros combináveis | `CMP-CRM-15` | Alternância de visão (kanban/lista/gráfico; tabela/cards) |
| `CMP-CRM-08` | Paleta de comandos | `CMP-CRM-16` | Linha de confiança (site) |

## Anti-padrões
- Campos obrigatórios demais; perder o contexto ao abrir registro; filtro que reseta ao navegar (inferência).
- Exclusão em massa sem desfazer; reordenar a tabela sob o cursor; contadores animando a cada filtro.
- Pré-marcar consentimento de marketing (contraria o art. 8º quanto ao ônus da prova — interpretação da 10B).
- Status só por cor; fundo saturado em tabela; número abreviado sem valor exato.
- IA que resume sem mostrar a fonte (atividade, e-mail, ligação) (inferência).

## Workflow
1. Confirme a superfície: desktop (principal), mobile (campo) ou site; abra a skill de plataforma.
2. Escolha um `TPL-CRM` (escuro × claro; funil em destaque × plataforma com módulos) e defina tokens.
3. Mapeie objetos (contato, empresa, negócio, atividade, tarefa) e telas: lista, pipeline, perfil, relatório.
4. Escolha os `CMP-CRM` por tela; defina atalhos (⌘K, navegar linha, abrir painel) antes do visual.
5. Passe por números (regra 5), histórico (regra 6) e `references/regulacao.md` na captura e no perfil do contato.
6. Abra 1–2 imagens do `references/visual-index.md`; adapte sem copiar. Verifique teclado e contraste
   (`design:accessibility-review`, `ext-playwright-cli`).

## Onde está o resto
| Preciso de… | Abra |
|---|---|
| Esqueletos (rail + top nav, sidebar larga, kanban, detalhe) | `../dashboard-ui/references/layout-patterns.md` §1 |
| KPI cards, gráficos, densidade, card de IA | `../dashboard-ui/references/layout-patterns.md` §2–5 |
| Gauge × barras (comparar equipes/canais = barras) | `../dashboard-ui/references/layout-patterns.md` §11 |
| Metas e ranking de vendedores (gamificação, painel gestor × cliente) | `../dashboard-ui/references/layout-patterns.md` §7 |
| Exemplos: vendas de varejo, CRM de estúdio, glassy V30 (deals pipeline), vendas de pequena empresa | `../dashboard-ui/references/domain-examples.md` §1, §10, §12, §15 |
| Tabela de dados, ⌘K, split view, multi-seleção | `../desktop-app-ui/references/desktop-patterns.md` §3, §6, §7; `../desktop-app-ui/SKILL.md` regra 7 |
| Tabelas e painel lateral (NN/g), CASTLE | `../ux-patterns/references/nng-research.md` §7, §10 |
| ⌘K: 6 decisões; toolbar lotada | `../ux-patterns/references/components-checklists.md` §6, §7 |
| Dark patterns | `../ux-patterns/references/dark-patterns.md` |
| Drag para reordenar, toast stack, reduce motion | `../ui-motion/references/css-recipes.md` §9, §10, §13 |
| Paleta 2+1 e contraste | `../design-direction/references/color-palettes.md` |
| Listas com swipe/long press no celular | `../mobile-app-ui/references/mobile-patterns.md` §16 |
| Normas, órgãos e URLs | `references/regulacao.md` |
| Fontes verificadas e da galeria | `references/fontes.md` |
| Quais imagens abrir | `references/visual-index.md` |
