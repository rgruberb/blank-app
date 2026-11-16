# Atualização diária dos anúncios (Apê Zona Sul)

Uma vez por dia, uma tarefa agendada no Claude lê os e-mails de alerta dos portais
no Gmail e grava os anúncios no Artifact https://claude.ai/artifact/GSWdgsTVFEzMQdHEzfTK9J.
Não manda notificação. Este arquivo é a referência das regras; a tarefa leva uma cópia delas no próprio prompt.

## Fonte

- Só e-mails de: quintoandar.com.br, zapimoveis.com.br, vivareal.com.br, olx.com.br, imovelweb.com.br
- Busca no Gmail: `from:(quintoandar.com.br OR zapimoveis.com.br OR vivareal.com.br OR olx.com.br OR imovelweb.com.br) newer_than:3d`
- Ignora e-mails de marketing sem anúncios.
- Os ids dos e-mails já lidos ficam em `config/coleta.emails_processados` (últimos 300).

## O que entra

- Aluguel de apartamento, 1 ou 2 quartos, num dos 16 bairros da Zona Sul do app.
- Os filtros de orçamento e exigências NÃO são aplicados na coleta: o app filtra na tela.

## Documento `apartamentos/<id>`

- id: `<site>-<id do anúncio na URL>` (ex.: `quintoandar-893456789`, `zap-2712345678`)
- Campos da coleta: titulo, bairro, endereco, quartos, area_m2, aluguel, condominio,
  iptu_anual, seguro_incendio_anual, vaga, aceita_pet, mobiliado (true/false/null),
  perto_metro (≤ 700 m de uma estação), lat, lon, local_aproximado, fonte,
  links [{site, url}], encontrado_em, ultimo_alerta, historico_preco [{data, aluguel}], atualizado_em
- Campos do usuário, que a coleta NUNCA escreve: visto, descartado, observacoes
- Duplicados entre sites (mesmo bairro e quartos, área ±3 m², aluguel ±5 %, mesma rua quando houver)
  viram um só documento com vários links.

## Localização

Nominatim (OpenStreetMap), 1 pedido por segundo, User-Agent genérico. Sem rua no anúncio,
fica sem lat/lon e o app desenha o ponto perto do centro do bairro (pontilhado).
