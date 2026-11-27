# Templates SAU (direções visuais)

Base: "Direções visuais possíveis" da ficha SAU (rodada 10B, 27/11/2026). Hex medidos por `getComputedStyle` nas
páginas públicas; **raio, sombra e durações não foram medidos** em nenhum produto de saúde — os valores dessas linhas
são sugestão nossa (inferência) e devem ser ajustados ao projeto. Escala tipográfica: NHS (14→64px).

## TPL-SAU-01 — Sistema público claro
| token | valor |
|---|---|
| Paleta | fundo `#FFFFFF`, superfície `#F0F4F5`, borda `#D8DDE0`, texto `#212B32`, ação/link `#005EB8`, ação pressionada/título `#003087`, sucesso/confirmação `#007F3B` (NHS, medidos) |
| Par tipográfico | Frutiger (marca NHS) → **Arial** fora do NHS; uma família só |
| Escala | corpo **19px (≥ tela grande) / 16px (tela pequena)**; pequeno ~16/14px com moderação; títulos até 64px (NHS) |
| Raio | 0–4px, cantos quase retos (inferência; não medido) |
| Sombra | nenhuma ou borda inferior sólida no botão (inferência; não medido) |
| Densidade | baixa; uma pergunta por tela em formulário |
| Motion | mínimo; só foco/carregamento; nada em resultado/dose |
| Quando usar | serviço público ou quase público, triagem, formulário longo de paciente, público idoso |
| Fontes | https://service-manual.nhs.uk/design-system · /styles/typography |
| Imagens | nenhuma própria do NHS capturada; ver `9B_formularios_slack-forca-senha_1.jpg` (ux-patterns) para rótulo fora do campo |

## TPL-SAU-02 — Marketplace acolhedor
| token | valor |
|---|---|
| Paleta | hero `#006A59` (verde), fundos `#DFF9F2` e `#EEE8E3`, neutro quente `#B6AEA5`, texto `#2A2623` / `#35495E`, apoio `#27455C` (Doctoralia, medidos) |
| Par tipográfico | `system-ui` (Doctoralia); se quiser personalidade, 1 sans humanista + mesma sans no corpo (inferência) |
| Escala | corpo 16px mínimo; adotar 19px em desktop para paciente (regra NHS) |
| Raio | médio, cartões e campo de busca arredondados (observado na imagem; valor não medido) |
| Sombra | leve, só no bloco de busca (observado; valor não medido) |
| Densidade | média; lista de especialidades e convênios em texto corrido com "Mais" |
| Motion | leve (hover, abertura de lista); nunca no preço ou no horário |
| Quando usar | busca e agendamento de profissionais, rede de clínicas, site de clínica com agenda online |
| Fontes | https://www.doctoralia.com.br/ |
| Imagens | `10C_SAU_doctoralia_home-busca-especialista_1.jpg`, `10C_SAU_zocdoc_home-busca-seguro-saude_1.jpg` |

## TPL-SAU-03 — Clínico profissional
| token | valor |
|---|---|
| Paleta | neutros frios + azul-petróleo `#27455C` (medido na Doctoralia) como cor de estrutura; ação `#005EB8`; alerta vermelho só para fora da faixa (inferência — **sem fonte de produto logado**) |
| Par tipográfico | sans de sistema/Inter + `tabular-nums` em agenda e exames (complemento) |
| Escala | corpo 16px (escala geral de app); 13–14px só em célula e rótulo (inferência); nunca dado clínico < 14px |
| Raio | 6–8px (inferência) |
| Sombra | bordas 1px em vez de sombra (inferência) |
| Densidade | média-alta (agenda, prontuário) — não verificado |
| Motion | funcional: abrir painel lateral, salvar; nada em valores clínicos |
| Quando usar | prontuário, agenda do consultório, recepção, laboratório |
| Fontes | ficha 10B (direção 3, inferência); padrões de app em `desktop-app-ui` |
| Imagens | `10C_SAU_dribbble-phenomenon-lably_dashboard-exames-ia_1.jpg` (conceito claro) |

## TPL-SAU-04 — Operação clínica escura
| token | valor |
|---|---|
| Paleta | fundo `~#0b0c0e`, cards `~#151618`, acento mint `~#2fb58f`, âmbar para prazo, vermelho para negado (valores aproximados descritos em `dashboard-ui/references/domain-examples.md` §7, não medidos por código) |
| Par tipográfico | sans geométrica; números grandes em peso leve (dashboard-ui §7) |
| Escala | ver `dashboard-ui` (KPI strip, tabela "Needs attention") |
| Raio | cards ~16px (dashboard-ui §7) |
| Sombra | borda sutil + glow verde muito leve (dashboard-ui §7) |
| Densidade | alta (operação: autorização prévia, convênio, fila) |
| Motion | entrada da sidebar e conteúdo; gráfico troca estado; nada piscando em prazo |
| Quando usar | back-office de autorização prévia, faturamento de convênio, central de agendamento — **não** para paciente |
| Fontes | reel `DfV39ohhwAC` (@ui.iliasmiah000), conceito |
| Imagens | `../../dashboard-ui/assets/visual-refs/DfV39ohhwAC.jpg`, `../../dashboard-ui/assets/visual-refs/DfUvP_ulPC6_2.jpg`; portal de fisioterapia `10A_DgAqhGGDBws_1.jpg` |

## Como escolher
- Paciente idoso ou fluxo regulado → 01. Busca/agendamento com marca acolhedora → 02.
- Profissional em tela cheia o dia todo → 03 (claro) ou 04 (escuro, operação). Bem-estar → 02 com o tom de Calm
  (`10C_SAU_calm_home-ajuda-categorias_1.jpg`), sem hex medido (inferência).
