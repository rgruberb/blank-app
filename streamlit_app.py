import pandas as pd
import pydeck as pdk
import streamlit as st

import dados

st.set_page_config(page_title="Apê no Rio · Zona Sul", page_icon="🏠", layout="wide")


def brl(valor: float) -> str:
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


# ------------------------------------------------------------------ filtros
with st.sidebar:
    st.header("🔎 O que você procura")
    quartos = st.multiselect("Quartos", [1, 2], default=[1, 2],
                             format_func=lambda q: f"{q} quarto" + ("s" if q > 1 else ""))
    orcamento = st.slider("Orçamento mensal total (aluguel + condomínio + IPTU + seguro)",
                          min_value=1500, max_value=15000, value=5000, step=250,
                          format="R$ %d")
    bairros = st.multiselect("Bairros (Zona Sul)", list(dados.BAIRROS_ZONA_SUL),
                             default=list(dados.BAIRROS_ZONA_SUL))
    st.subheader("Exigências")
    exige_vaga = st.checkbox("Vaga de garagem")
    exige_pet = st.checkbox("Aceita pet")
    exige_mobiliado = st.checkbox("Mobiliado")
    exige_metro = st.checkbox("Perto do metrô")

st.title("🏠 Apê no Rio · Zona Sul")
st.caption(
    f"{' ou '.join(map(str, quartos)) or '—'} quarto(s) · até **{brl(orcamento)}**/mês no total · "
    f"{len(bairros)} bairro(s)"
)

aba_lista, aba_mapa, aba_novo, aba_busca = st.tabs(
    ["📋 Meus apartamentos", "🗺️ Mapa", "➕ Adicionar", "🌐 Buscar nos sites"]
)


def aplicar_filtros(df: pd.DataFrame) -> pd.Series:
    ok = df["quartos"].isin(quartos) & df["bairro"].isin(bairros) & (df["custo_total"] <= orcamento)
    for exige, coluna in [(exige_vaga, "vaga"), (exige_pet, "aceita_pet"),
                          (exige_mobiliado, "mobiliado"), (exige_metro, "perto_metro")]:
        if exige:
            ok &= df[coluna] == 1
    return ok


# ------------------------------------------------------------------ lista + detalhes
with aba_lista:
    df = dados.listar()
    if df.empty:
        st.info("Nenhum apartamento salvo ainda. Use **🌐 Buscar nos sites** para achar anúncios "
                "e **➕ Adicionar** para salvar os que gostar.")
    else:
        df["passa"] = aplicar_filtros(df)
        c1, c2 = st.columns([1, 1])
        mostrar_todos = c1.toggle("Mostrar também os que não passam nos filtros", value=False)
        esconder_descartados = c2.toggle("Esconder descartados", value=True)

        vis = df if mostrar_todos else df[df["passa"]]
        if esconder_descartados:
            vis = vis[vis["status"] != "Descartado"]
        vis = vis.sort_values("custo_total")

        st.write(f"**{len(vis)}** de {len(df)} apartamento(s)")
        tabela = pd.DataFrame({
            "✓": vis["passa"].map({True: "✅", False: "⚠️"}),
            "Título": vis["titulo"],
            "Bairro": vis["bairro"],
            "Quartos": vis["quartos"],
            "m²": vis["area_m2"],
            "Total/mês": vis["custo_total"],
            "R$/m²": vis["custo_m2"],
            "Vaga": vis["vaga"].map({1: "🚗", 0: ""}),
            "Pet": vis["aceita_pet"].map({1: "🐾", 0: ""}),
            "Mobiliado": vis["mobiliado"].map({1: "🛋️", 0: ""}),
            "Metrô": vis["perto_metro"].map({1: "🚇", 0: ""}),
            "Status": vis["status"],
            "Anúncio": vis["link"],
        })
        st.dataframe(
            tabela, hide_index=True, width="stretch",
            column_config={
                "Total/mês": st.column_config.NumberColumn(format="R$ %.0f"),
                "R$/m²": st.column_config.NumberColumn(format="R$ %.0f"),
                "m²": st.column_config.NumberColumn(format="%.0f"),
                "Anúncio": st.column_config.LinkColumn(display_text="abrir"),
            },
        )

        if not vis.empty:
            st.divider()
            st.subheader("🔍 Detalhes")
            opcoes = vis["id"].tolist()
            nomes = dict(zip(vis["id"], vis["titulo"] + " · " + vis["bairro"]))
            apto_id = st.selectbox("Apartamento", opcoes, format_func=nomes.get)
            apto = df[df["id"] == apto_id].iloc[0].to_dict()

            mensal = dados.custo_mensal(apto)
            entrada = dados.custo_entrada(apto)
            total = mensal["Total"]

            col_custo, col_info = st.columns([3, 2])
            with col_custo:
                st.markdown("##### Custo mensal")
                linhas = [(k, v) for k, v in mensal.items() if k != "Total"]
                quebra = pd.DataFrame({
                    "Item": [k for k, _ in linhas] + ["**Total**"],
                    "Valor": [brl(v) for _, v in linhas] + [brl(total)],
                    "% do total": [f"{(v / total * 100 if total else 0):.0f}%" for _, v in linhas] + ["100%"],
                })
                st.table(quebra.set_index("Item"))

                folga = orcamento - total
                st.progress(min(total / orcamento, 1.0),
                            text=f"{total / orcamento * 100:.0f}% do orçamento de {brl(orcamento)}")
                if folga >= 0:
                    st.success(f"Cabe no orçamento, com folga de {brl(folga)}/mês.")
                else:
                    st.error(f"Passa do orçamento em {brl(-folga)}/mês.")

                st.markdown("##### Para entrar no imóvel")
                st.markdown(
                    f"- **Garantia:** {entrada['garantia']} → {brl(entrada['valor_garantia'])} "
                    f"_({entrada['nota']})_\n"
                    f"- **Primeiro mês:** {brl(entrada['primeiro_mes'])}\n"
                    f"- **Total estimado na entrada:** **{brl(entrada['total'])}**"
                )
                st.caption("Também vale considerar o custo anual: "
                           f"{brl(total * 12)} (12 × total mensal).")

            with col_info:
                st.markdown("##### Imóvel")
                area_txt = f"{apto['area_m2']:.0f} m²" if pd.notna(apto["area_m2"]) and apto["area_m2"] else "—"
                st.markdown(
                    f"- **Bairro:** {apto['bairro']}\n"
                    f"- **Endereço:** {apto['endereco'] or '—'}\n"
                    f"- **Quartos:** {apto['quartos']}\n"
                    f"- **Área:** {area_txt}\n"
                    f"- **Custo por m²:** {brl(apto['custo_m2']) if pd.notna(apto['custo_m2']) else '—'}\n"
                    f"- {'🚗 Tem vaga' if apto['vaga'] else '🚫 Sem vaga'} · "
                    f"{'🐾 Aceita pet' if apto['aceita_pet'] else '🚫 Não aceita pet'}\n"
                    f"- {'🛋️ Mobiliado' if apto['mobiliado'] else 'Sem mobília'} · "
                    f"{'🚇 Perto do metrô' if apto['perto_metro'] else 'Longe do metrô'}"
                )
                if apto["link"]:
                    st.link_button("Abrir anúncio", apto["link"])

                with st.form(f"editar_{apto_id}"):
                    status = st.selectbox("Status", dados.STATUS,
                                          index=dados.STATUS.index(apto["status"])
                                          if apto["status"] in dados.STATUS else 0)
                    obs = st.text_area("Observações", value=apto["observacoes"] or "")
                    if st.form_submit_button("Salvar"):
                        dados.atualizar(apto_id, {"status": status, "observacoes": obs})
                        st.rerun()
                if st.button("🗑️ Remover este apartamento", key=f"rm_{apto_id}"):
                    dados.remover(apto_id)
                    st.rerun()


# ------------------------------------------------------------------ adicionar
with aba_novo:
    with st.form("novo", clear_on_submit=True):
        st.markdown("Cole os dados do anúncio. Campos com * são obrigatórios.")
        c1, c2 = st.columns(2)
        titulo = c1.text_input("Título *", placeholder="Ex.: 2 qts reformado perto da praia")
        link = c2.text_input("Link do anúncio")
        bairro = c1.selectbox("Bairro *", list(dados.BAIRROS_ZONA_SUL))
        endereco = c2.text_input("Endereço / rua")
        n_quartos = c1.radio("Quartos *", [1, 2], horizontal=True)
        area = c2.number_input("Área (m²)", min_value=0.0, step=1.0)

        st.markdown("**Valores**")
        v1, v2, v3, v4 = st.columns(4)
        aluguel = v1.number_input("Aluguel (R$/mês) *", min_value=0.0, step=100.0)
        condominio = v2.number_input("Condomínio (R$/mês)", min_value=0.0, step=50.0)
        iptu = v3.number_input("IPTU (R$/ano)", min_value=0.0, step=100.0,
                               help="Se o anúncio mostra o IPTU mensal, multiplique por 12.")
        seguro = v4.number_input("Seguro incêndio (R$/ano)", min_value=0.0, step=50.0)
        garantia = st.selectbox("Garantia exigida", [
            "Caução (3 aluguéis)", "Seguro fiança", "Título de capitalização", "Fiador", "Sem garantia",
        ])

        st.markdown("**Características**")
        k1, k2, k3, k4 = st.columns(4)
        vaga = k1.checkbox("Vaga de garagem")
        pet = k2.checkbox("Aceita pet")
        mobiliado = k3.checkbox("Mobiliado")
        metro = k4.checkbox("Perto do metrô")
        obs = st.text_area("Observações")

        if st.form_submit_button("Salvar apartamento", type="primary"):
            if not titulo or aluguel <= 0:
                st.error("Preencha pelo menos o título e o aluguel.")
            else:
                dados.adicionar({
                    "titulo": titulo, "link": link, "bairro": bairro, "endereco": endereco,
                    "quartos": n_quartos, "area_m2": area or None, "aluguel": aluguel,
                    "condominio": condominio, "iptu_anual": iptu, "seguro_incendio_anual": seguro,
                    "vaga": int(vaga), "aceita_pet": int(pet), "mobiliado": int(mobiliado),
                    "perto_metro": int(metro), "garantia": garantia, "observacoes": obs,
                })
                st.success(f"“{titulo}” salvo! Veja na aba 📋 Meus apartamentos.")


# ------------------------------------------------------------------ busca nos portais
with aba_busca:
    st.markdown(
        "Links de busca já filtrados por bairro, quartos e preço. "
        "Os sites não aplicam todos os filtros pela URL. Confira vaga, pet, mobília e metrô no "
        "próprio site e lembre que o preço que eles filtram costuma ser **só o aluguel**."
    )
    if not bairros:
        st.warning("Escolha pelo menos um bairro na barra lateral.")
    for b in bairros:
        links = dados.links_busca(b, quartos, orcamento)
        cols = st.columns([2] + [1] * len(links))
        cols[0].markdown(f"**{b}**")
        for col, (site, url) in zip(cols[1:], links.items()):
            col.link_button(site, url, width="stretch")


# ------------------------------------------------------------------ mapa
with aba_mapa:
    todos = dados.listar()
    if not todos.empty:
        todos["passa"] = aplicar_filtros(todos)
        ativos = todos[todos["status"] != "Descartado"]
    else:
        ativos = todos

    linhas = []
    for nome, (lat, lon) in dados.COORDS_BAIRROS.items():
        do_bairro = ativos[ativos["bairro"] == nome] if not ativos.empty else ativos
        n_salvos = len(do_bairro)
        n_ok = int(do_bairro["passa"].sum()) if n_salvos else 0
        mediana = do_bairro["custo_total"].median() if n_salvos else None
        escolhido = nome in bairros
        linhas.append({
            "nome": nome, "lat": lat, "lon": lon,
            "raio": 170 + 70 * n_salvos,
            "cor": [214, 69, 65, 120] if escolhido else [140, 140, 140, 60],
            "dica": (f"<b>{nome}</b>" + ("" if escolhido else " (fora da busca)")
                     + f"<br/>{n_salvos} salvo(s), {n_ok} dentro dos filtros"
                     + (f"<br/>Total mediano: {brl(mediana)}/mês" if mediana else "")),
        })
    pontos_bairros = pd.DataFrame(linhas)
    estacoes = pd.DataFrame(
        [{"nome": n, "lat": la, "lon": lo, "dica": f"🚇 Estação {n}"}
         for n, (la, lo) in dados.ESTACOES_METRO.items()]
    )

    mostrar_metro = st.toggle("Mostrar estações de metrô", value=True)
    camadas = [
        pdk.Layer("ScatterplotLayer", pontos_bairros, get_position="[lon, lat]",
                  get_radius="raio", get_fill_color="cor", pickable=True,
                  stroked=True, get_line_color=[255, 255, 255], line_width_min_pixels=1),
    ]
    if mostrar_metro:
        camadas.append(pdk.Layer("ScatterplotLayer", estacoes, get_position="[lon, lat]",
                                 get_radius=70, radius_min_pixels=4,
                                 get_fill_color=[33, 102, 172, 230], pickable=True))

    st.pydeck_chart(pdk.Deck(
        layers=camadas,
        initial_view_state=pdk.ViewState(latitude=-22.958, longitude=-43.212, zoom=12.1),
        tooltip={"html": "{dica}"},
        map_style="light",
    ), height=560)
    st.caption("🔴 bairros da sua busca · ⚪ outros bairros da Zona Sul · 🔵 estações de metrô. "
               "O tamanho do círculo cresce com o número de apartamentos salvos (sem contar os descartados). "
               "As posições são aproximadas (centro do bairro).")

    if not ativos.empty:
        resumo = (ativos.groupby("bairro")
                  .agg(Salvos=("id", "count"), Dentro_dos_filtros=("passa", "sum"),
                       Mais_barato=("custo_total", "min"), Mediana=("custo_total", "median"))
                  .rename(columns={"Dentro_dos_filtros": "Dentro dos filtros",
                                   "Mais_barato": "Mais barato/mês", "Mediana": "Mediana/mês"})
                  .sort_values("Mediana/mês"))
        st.dataframe(resumo, width="stretch", column_config={
            "Mais barato/mês": st.column_config.NumberColumn(format="R$ %.0f"),
            "Mediana/mês": st.column_config.NumberColumn(format="R$ %.0f"),
        })
