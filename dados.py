"""Constantes, cálculo de custos e armazenamento (SQLite) dos apartamentos."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from urllib.parse import urlencode

import pandas as pd

DB_PATH = Path(__file__).parent / "data" / "apartamentos.db"

# Bairros da Zona Sul do Rio de Janeiro: nome -> slug usado nas URLs dos portais
BAIRROS_ZONA_SUL = {
    "Botafogo": "botafogo",
    "Catete": "catete",
    "Copacabana": "copacabana",
    "Cosme Velho": "cosme-velho",
    "Flamengo": "flamengo",
    "Gávea": "gavea",
    "Glória": "gloria",
    "Humaitá": "humaita",
    "Ipanema": "ipanema",
    "Jardim Botânico": "jardim-botanico",
    "Lagoa": "lagoa",
    "Laranjeiras": "laranjeiras",
    "Leblon": "leblon",
    "Leme": "leme",
    "São Conrado": "sao-conrado",
    "Urca": "urca",
}

STATUS = ["Novo", "Visitar", "Visitado", "Proposta enviada", "Descartado"]

COLUNAS = {
    "titulo": "TEXT NOT NULL",
    "link": "TEXT",
    "bairro": "TEXT NOT NULL",
    "endereco": "TEXT",
    "quartos": "INTEGER NOT NULL",
    "area_m2": "REAL",
    "aluguel": "REAL NOT NULL",
    "condominio": "REAL DEFAULT 0",
    "iptu_anual": "REAL DEFAULT 0",
    "seguro_incendio_anual": "REAL DEFAULT 0",
    "vaga": "INTEGER DEFAULT 0",
    "aceita_pet": "INTEGER DEFAULT 0",
    "mobiliado": "INTEGER DEFAULT 0",
    "perto_metro": "INTEGER DEFAULT 0",
    "garantia": "TEXT",
    "status": "TEXT DEFAULT 'Novo'",
    "observacoes": "TEXT",
}


# ---------------------------------------------------------------- custos

def custo_mensal(apto: dict) -> dict:
    """Destrincha o custo mensal de um apartamento."""
    partes = {
        "Aluguel": float(apto.get("aluguel") or 0),
        "Condomínio": float(apto.get("condominio") or 0),
        "IPTU (anual ÷ 12)": float(apto.get("iptu_anual") or 0) / 12,
        "Seguro incêndio (anual ÷ 12)": float(apto.get("seguro_incendio_anual") or 0) / 12,
    }
    partes["Total"] = sum(partes.values())
    return partes


def custo_entrada(apto: dict) -> dict:
    """Estimativa do que sai do bolso para entrar no imóvel."""
    aluguel = float(apto.get("aluguel") or 0)
    garantia = apto.get("garantia") or "Caução (3 aluguéis)"
    if garantia.startswith("Caução"):
        valor_garantia = 3 * aluguel
        nota = "devolvido ao final do contrato (corrigido)"
    elif garantia.startswith("Seguro fiança"):
        # Estimativa de mercado: ~1 a 1,5 aluguel por ano (usamos 1,2)
        valor_garantia = 1.2 * custo_mensal(apto)["Total"]
        nota = "estimativa anual; não é devolvido"
    elif garantia.startswith("Título"):
        valor_garantia = 6 * aluguel
        nota = "estimativa; resgatável ao final"
    else:  # fiador / sem garantia
        valor_garantia = 0.0
        nota = "sem custo direto"
    return {
        "garantia": garantia,
        "valor_garantia": valor_garantia,
        "nota": nota,
        "primeiro_mes": custo_mensal(apto)["Total"],
        "total": valor_garantia + custo_mensal(apto)["Total"],
    }


# ---------------------------------------------------------------- links de busca

def links_busca(bairro: str, quartos: list[int], orcamento: int) -> dict[str, str]:
    """Links de busca nos portais, já filtrados pelo bairro.

    Os portais não têm API pública e mudam o formato das URLs de tempos em
    tempos; se um link parar de filtrar direito, ajuste aqui.
    """
    slug = BAIRROS_ZONA_SUL[bairro]
    q_min = min(quartos) if quartos else 1
    links = {
        "QuintoAndar": (
            f"https://www.quintoandar.com.br/alugar/imovel/"
            f"{slug}-rio-de-janeiro-rj-brasil/apartamento/de-{q_min}-quartos"
            f"/ate-{orcamento}-reais"
        ),
        "ZAP Imóveis": (
            f"https://www.zapimoveis.com.br/aluguel/apartamentos/"
            f"rj+rio-de-janeiro+zona-sul+{slug}/?"
            + urlencode({"quartos": ",".join(map(str, quartos or [1, 2])),
                         "precoMaximo": orcamento})
        ),
        "VivaReal": (
            f"https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/"
            f"{slug}/apartamento_residencial/?"
            + urlencode({"quartos": ",".join(map(str, quartos or [1, 2])),
                         "precoMaximo": orcamento})
        ),
    }
    termo = f"aluguel apartamento {' ou '.join(map(str, quartos or [1, 2]))} quartos {bairro} Rio de Janeiro"
    links["Google (OLX e outros)"] = "https://www.google.com/search?" + urlencode({"q": termo})
    return links


# ---------------------------------------------------------------- banco de dados

def _conn() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cols = ", ".join(f"{nome} {tipo}" for nome, tipo in COLUNAS.items())
    conn.execute(f"CREATE TABLE IF NOT EXISTS apartamentos (id INTEGER PRIMARY KEY AUTOINCREMENT, {cols})")
    return conn


def adicionar(apto: dict) -> int:
    campos = [c for c in COLUNAS if c in apto]
    with _conn() as conn:
        cur = conn.execute(
            f"INSERT INTO apartamentos ({', '.join(campos)}) VALUES ({', '.join('?' * len(campos))})",
            [apto[c] for c in campos],
        )
        return cur.lastrowid


def atualizar(apto_id: int, mudancas: dict) -> None:
    campos = [c for c in COLUNAS if c in mudancas]
    if not campos:
        return
    with _conn() as conn:
        conn.execute(
            f"UPDATE apartamentos SET {', '.join(f'{c} = ?' for c in campos)} WHERE id = ?",
            [mudancas[c] for c in campos] + [apto_id],
        )


def remover(apto_id: int) -> None:
    with _conn() as conn:
        conn.execute("DELETE FROM apartamentos WHERE id = ?", (apto_id,))


def listar() -> pd.DataFrame:
    with _conn() as conn:
        df = pd.read_sql_query("SELECT * FROM apartamentos ORDER BY id DESC", conn)
    if df.empty:
        return df
    df["custo_total"] = df.apply(lambda r: custo_mensal(r.to_dict())["Total"], axis=1)
    df["custo_m2"] = df["custo_total"] / df["area_m2"].where(df["area_m2"] > 0)
    return df
