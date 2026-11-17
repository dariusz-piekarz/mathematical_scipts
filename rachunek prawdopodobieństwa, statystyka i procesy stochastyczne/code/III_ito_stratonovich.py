from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(501)
N = 2**15
dB = rng.normal(0, 1/np.sqrt(N), size=N)
B = np.r_[0., np.cumsum(dB)]
ns = 2**np.arange(4, 16)
ito, strat = [], []
for n in ns:
    punkty = B[::N//n]
    d = np.diff(punkty)
    ito.append(np.sum(punkty[:-1]*d))
    strat.append(np.sum((punkty[:-1]+punkty[1:])/2*d))
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.plot(ns, ito, "o-", label="sumy lewe (Ito)")
ax.plot(ns, strat, "s-", label="sumy trapezowe (Stratonovich)")
ax.axhline((B[-1]**2-1)/2, ls="--", color="black",
           label="(B_1^2 - 1)/2")
ax.axhline(B[-1]**2/2, ls=":", color="grey",
           label="B_1^2/2")
ax.set_xscale("log", base=2)
ax.set(xlabel="liczba podprzedzialow n", ylabel="wartosc sumy",
       title="Dwie konwencje calkowania wzgledem B")
ax.legend(fontsize=8); ax.grid(alpha=.25); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/III_ito_stratonovich.pdf")
plt.close(fig)
