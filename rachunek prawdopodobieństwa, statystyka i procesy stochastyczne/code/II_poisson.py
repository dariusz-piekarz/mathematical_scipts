from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(401)
lam, T = 2.5, 5.0
skoki = []
t = 0.0
while True:
    t += rng.exponential(scale=1/lam)
    if t > T:
        break
    skoki.append(t)
s = np.array(skoki)  # chwile skokow procesu Poissona
czas = np.linspace(0, T, 500)
N = np.searchsorted(s, czas, side="right")
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.step(czas, N, where="post", label="N_t")
ax.plot(czas, lam*czas, "k--", label="E[N_t] = lambda t")
ax.set(xlabel="t", ylabel="liczba zdarzen",
       title="Proces Poissona i jego srednia")
ax.legend(); ax.grid(alpha=.25); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/II_poisson.pdf")
plt.close(fig)
