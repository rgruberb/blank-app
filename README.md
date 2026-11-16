# 🏠 Apê no Rio · Zona Sul

App em Streamlit para organizar a busca de apartamento para alugar na Zona Sul do Rio.

- **Filtros:** 1 ou 2 quartos, orçamento mensal **total** (aluguel + condomínio + IPTU + seguro incêndio), bairros da Zona Sul, vaga, pet, mobiliado e perto do metrô
- **Buscar nos sites:** links já filtrados para QuintoAndar, ZAP, VivaReal e Google
- **Mapa:** bairros da busca, estações de metrô e resumo de preços por bairro
- **Meus apartamentos:** salve os anúncios, compare pelo custo total e por R$/m², e veja nos detalhes o custo destrinchado e quanto custa para entrar no imóvel

Os dados ficam em `data/apartamentos.db` (SQLite local, fora do git).

## Como rodar

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Versão para celular

`artifact/ape-zona-sul.html` é a versão mobile, publicada como Artifact privado no claude.ai.
Os apartamentos e os filtros ficam salvos no armazenamento do Artifact e sincronizam entre celular e computador.
