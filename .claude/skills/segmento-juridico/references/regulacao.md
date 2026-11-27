# Regulação que afeta a interface — Jurídico (JUR)

> **Aviso:** isto não é aconselhamento jurídico. É um resumo de pesquisa de design (rodada 10B, 27/11/2026) para
> orientar telas. **Confira a norma vigente** e valide com o advogado/jurídico responsável pelo projeto antes de
> publicar. Legenda: ✅ texto oficial lido · 🔒 não verificado (só visto em busca ou página não abriu) ·
> "(inferência)" = aplicação nossa.

## Provimento CFOAB 205/2021 (publicidade e informação da advocacia), de 15/07/2021
Fonte: https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021 ✅

| Dispositivo | O que diz (resumo da leitura) | O que muda na tela |
|---|---|---|
| Art. 3º, caput | publicidade não pode configurar captação de clientela ou mercantilização | Site informativo, sem funil agressivo (inferência). |
| Art. 3º, I | vedada referência a honorários para captar | Sem preço/desconto como gancho. |
| Art. 3º, §1º | publicidade "sóbria, discreta e informativa" | Tom e visual sóbrios. |
| Art. 4º, §1º | títulos "verdadeiros e comprováveis" | Só títulos reais na página do advogado. |
| Art. 4º, §2º | vedada menção a decisões judiciais e resultados | Sem "casos ganhos", "% de êxito", vitórias. |
| Art. 5º, §2º | vedado logotipo e símbolos oficiais da OAB | Inscrição na OAB em texto, sem logo. |
| Art. 5º, §3º | vedados casos concretos e resultados em vídeos/palestras | Conteúdo educativo sem caso concreto. |
| Art. 6º | vedada promessa de resultados; parágrafo único: ostentação | Sem "resultado garantido"; sem imagens de luxo. |

- **Depoimentos:** o texto lido **não os menciona expressamente**; as regras próximas são os arts. 4º §2º e 5º §3º
  (decida com o jurídico).
- Resumo comercial da Projuris (https://www.projuris.com.br/provimento-205-2021/): 🔒 só trecho em busca.

## Lei 14.063/2020 (assinaturas eletrônicas)
Fonte: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14063.htm ✅

| Tipo (art. 4º) | Definição resumida | Na tela |
|---|---|---|
| Simples | identifica o signatário | Explicar que é o nível básico. |
| Avançada | certificados não ICP-Brasil ou outro meio, vinculada ao signatário, detecta alteração | Explicar vínculo e detecção de alteração. |
| Qualificada | certificado digital ICP-Brasil; nível mais alto | Pedir certificado; explicar que é o nível mais alto. |

- Ementa: uso de assinaturas eletrônicas **em interações com entes públicos**. Aplicar a classificação em contratos
  privados é **inferência** de UX (mostrar o tipo aplicado), não conclusão jurídica.
- **MP 2.200-2/2001 (ICP-Brasil):** não aberta — 🔒 não verificada.

## LGPD — Lei 13.709/2018
Fonte: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm ✅ (arts. 5º, 6º, 8º, 9º, 11, 18 lidos
na pesquisa)
- Dados de clientes e partes em processos: aviso e consentimento onde houver dado pessoal (10B). Se o processo envolver
  dado de saúde, é dado sensível (art. 5º II) — ver `segmento-saude/references/regulacao.md`.
- Busca de pessoa por CPF/nome: mostrar finalidade e base do dado (inferência).

## Linguagem simples
- Diretrizes de escrita do GOV.UK (https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/tone-of-voice/):
  redirecionaram, **texto não lido** 🔒. Plain language: não verificado como norma.
- O que se apoia em fonte lida: NN/g recomenda linguagem de nível 6º–8º ano em formulários
  (`ux-patterns/references/nng-research.md` §5); Jusbrasil promete "sem juridiquês" (imagem C2).

## Não verificado
- Formato oficial do número de processo (CNJ); regras de tribunais para peticionamento; Código de Ética da OAB além do
  Provimento; normas de outros países (as ordens estaduais citadas pela Clio são dos EUA).

## Checklist de tela (inferência sobre o que foi lido)
- [ ] Site de escritório: sem preço como gancho, sem resultado/caso, sem logo da OAB, sem ostentação, títulos reais.
- [ ] Assinatura: tipo mostrado e explicado, revisão antes de assinar, trilha de auditoria.
- [ ] Dado pessoal de parte/cliente com aviso de finalidade.
- [ ] Termos técnicos explicados.
