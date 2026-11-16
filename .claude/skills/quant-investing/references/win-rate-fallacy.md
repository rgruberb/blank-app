# A falácia da alta taxa de acerto

Fonte: @tradionquant, reel `DfVf0L-AIkP`. Simulação própria do autor, em preços que se movem como **cara ou coroa**; todos os traders são simulados.

> Conteúdo educacional, não recomendação de investimento.

## A simulação (como descrita na fonte)

- **10.000 traders simulados por lado**, preços tipo coin flip.
- **500 trades** cada, **$10.000** de capital inicial.
- Mesma taxa em todo trade: **5% do valor arriscado**.
- **Lado A — acerta 90%:** ganhos minúsculos; uma perda do tamanho de **nove** ganhos ("nine tiny wins cover one loss"). Alvo perto, stop longe.
- **Lado B — acerta 35%:** ganhos quase **2x** o tamanho das perdas.
- **Antes das taxas:** ambos fazem **$0 por trade** em média.
- **Depois das taxas:** ambos perdem cerca de **$5 por trade** no início.

## Resultado

| Lado | Taxa de acerto | Resultado em 10.000 traders |
|---|---|---|
| A | 90% | **9.999 de 10.000** perderam dinheiro (1 "got lucky") |
| B | 35% | A maioria perdeu; **1.641** terminaram no lucro — por swings maiores e **sorte**, não edge |

Frames: um trader de 35% chega a **+$2.936** no trade 71 (curva bonita que é ruído); a taxa "come quase metade de cada ganho minúsculo"; o lado 90% precisaria de **94,5%** de acerto só para parar de perder. Placar final: "Rules that beat holding: **0 of 1**" — "holding = doing nothing: still $10,000".

Mensagem: "Here, a 90% win rate wasn't skill. It was where we put the target." A taxa de acerto só mostrou **onde o alvo estava**.

**Pergunta única:** *depois das taxas, o trade médio ganha dinheiro?* ("average trade, after fees: above $0?")

## A matemática (expectativa)

Notação: `p` = taxa de acerto, `W` = ganho médio, `L` = perda média (positiva), `c` = custo por trade.

```
Expectativa por trade  E = p·W − (1−p)·L − c
Payoff ratio           R = W / L
Breakeven sem custo    p* = L / (W + L) = 1 / (1 + R)
Breakeven com custo    p* = (L + c) / (W + L)
Profit factor          PF = (p·W) / ((1−p)·L)      (complemento)
```

**Lado A** (L = 9W): sem custo, `E = 0,9W − 0,1·9W = 0` ✔ (bate com "$0 a trade").
Com custo `c`: `p* = (9W + c) / (10W)`. O reel diz que a taxa é "quase metade de cada ganho" e que o breakeven é **94,5%** → isso corresponde a `c = 0,45W`: `p* = 9,45W / 10W = 94,5%` ✔.
(complemento, derivação) Se a taxa é 5% do valor arriscado e o risco é a perda `L = 9W`, então `c = 0,05·9W = 0,45W`, consistente com a fonte. Com E ≈ −$5 → W ≈ $11, risco ≈ $100 (≈1% de $10.000). Esses tamanhos absolutos são inferência, não estão explícitos no reel.

**Lado B** (R ≈ 1,86): sem custo `p* = 1/(1+1,86) ≈ 35%` → E ≈ 0. Com custo, E < 0. A variância maior deixa ~16% terminarem no azul por sorte.

## Regras práticas

1. **Nunca** avalie estratégia por taxa de acerto isolada. Reporte sempre: `p`, `W`, `L`, `R`, `E` **após custos**, max drawdown.
2. Taxa de acerto alta + payoff baixo = extremamente sensível a custos: um custo pequeno vira expectativa negativa.
3. Compare `p` observado com `p*` (breakeven com custos). A margem `p − p*` é o edge real; se é pequena, o erro amostral pode apagá-la. (complemento) Erro-padrão de `p` ≈ `sqrt(p(1−p)/n)`.
4. Lucro de alguns traders/backtests numa população grande pode ser **sorte** (1.641 de 10.000 com E < 0). Um bom resultado isolado não prova edge — rode Monte Carlo (ver `validation-tests.md`).
5. Compare sempre contra **segurar o ativo** (buy and hold).

## Reproduzir (complemento)

```python
import numpy as np
rng = np.random.default_rng(0)
def sim(p, W, L, c, n_tr=500, n=10_000, cap=10_000):
    win = rng.random((n, n_tr)) < p
    pnl = np.where(win, W, -L) - c
    return cap + pnl.sum(1)
a = sim(0.90, 11.1, 100, 5)      # lado A: L = 9W, c = 0,45W
print((a < 10_000).mean())       # ~ quase todos perdem
```
Esse sorteio Bernoulli simplifica o "preço coin flip" do reel; os números exatos (9.999, 1.641) vêm da simulação do autor e não serão reproduzidos à risca.
