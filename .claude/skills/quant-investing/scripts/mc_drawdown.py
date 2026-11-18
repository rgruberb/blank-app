#!/usr/bin/env python3
"""Monte Carlo reshuffle de trades -> distribuicao do max drawdown.

Embaralha a ORDEM dos trades N vezes (mesmos trades, outra sequencia) e mede
o max drawdown de cada curva. Compara o drawdown do backtest original com os
percentis simulados (regra das fontes: dimensionar pelo p95, nao pelo backtest).

Entrada: CSV/TXT; usa a ULTIMA coluna numerica (ou --col N, indice 0-based).
  --mode pct : retornos fracionarios por trade (0.012 = +1.2%), compostos.
  --mode pnl : P&L em dinheiro por trade, somado a --capital.

Uso:
  python mc_drawdown.py trades.csv --mode pct --n 1000
  python mc_drawdown.py --demo            # dados sinteticos
"""
import argparse
import sys

import numpy as np
import pandas as pd


def equity_curve(trades, mode, capital):
    if mode == "pct":
        return capital * np.cumprod(1.0 + trades, axis=-1)
    return capital + np.cumsum(trades, axis=-1)


def max_drawdown(equity, capital):
    # inclui o capital inicial como primeiro pico
    start = np.full(equity.shape[:-1] + (1,), capital, dtype=float)
    eq = np.concatenate([start, equity], axis=-1)
    peak = np.maximum.accumulate(eq, axis=-1)
    dd = 1.0 - eq / peak  # drawdown fracionario relativo ao pico
    return dd.max(axis=-1)


def run(trades, n=1000, mode="pct", capital=10_000.0, seed=42):
    trades = np.asarray(trades, dtype=float)
    rng = np.random.default_rng(seed)
    orig = max_drawdown(equity_curve(trades, mode, capital), capital)
    shuffled = np.array([rng.permutation(trades) for _ in range(n)])
    sims = max_drawdown(equity_curve(shuffled, mode, capital), capital)
    pct = np.percentile(sims, [5, 25, 50, 75, 95, 99])
    return orig, sims, pct


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="CSV/TXT com retornos ou P&L por trade")
    ap.add_argument("--mode", choices=["pct", "pnl"], default="pct")
    ap.add_argument("--n", type=int, default=1000, help="numero de reshuffles")
    ap.add_argument("--capital", type=float, default=10_000.0)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--sep", default=",", help="separador do CSV (padrao ,)")
    ap.add_argument("--col", type=int, default=-1, help="coluna numerica (padrao: ultima)")
    ap.add_argument("--demo", action="store_true", help="usa 300 trades sinteticos")
    a = ap.parse_args()

    if a.demo:
        rng = np.random.default_rng(0)
        trades = rng.normal(0.003, 0.02, 300)  # sintetico, so para teste
        a.mode = "pct"
    elif a.file:
        df = pd.read_csv(a.file, header=None, sep=a.sep)
        col = df.apply(pd.to_numeric, errors="coerce").dropna(axis=1, how="all")
        if col.empty:
            sys.exit("nenhuma coluna numerica encontrada")
        trades = col.iloc[:, a.col].dropna().to_numpy()
    else:
        ap.error("informe um arquivo ou --demo")

    orig, sims, pct = run(trades, a.n, a.mode, a.capital, a.seed)
    exp = trades.mean()
    print(f"trades: {len(trades)} | modo: {a.mode} | reshuffles: {a.n}")
    print(f"expectativa media por trade: {exp:.5f}")
    print(f"max DD do backtest (ordem original): {orig:.2%}")
    for p, v in zip([5, 25, 50, 75, 95, 99], pct):
        print(f"  p{p:<2} max DD simulado: {v:.2%}")
    if orig <= 0:
        print("backtest sem drawdown; compare o p95 com seu limite de risco.")
        return
    ratio = pct[4] / orig
    print(f"p95 / backtest: {ratio:.2f}x")
    print(f"% de ordens com DD >= 2x o do backtest: {(sims >= 2 * orig).mean():.1%}")
    if ratio >= 2:
        print("ALERTA: alguma ordem plausivel dobra o drawdown -> dimensione pelo p95.")


if __name__ == "__main__":
    main()
