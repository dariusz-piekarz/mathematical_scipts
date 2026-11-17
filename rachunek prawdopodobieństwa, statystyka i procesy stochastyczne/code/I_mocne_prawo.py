from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(104)
p, n = 0.35, 1000
fig, ax = plt.subplots(figsize=(7.1, 3.6))
for j in range(5):
    x = (rng.random(n) < p).astype(float)
    srednia = np.cumsum(x) / np.arange(1, n + 1)
    ax.plot(np.arange(1, n + 1), srednia, lw=1, label=f"proba {j+1}")
ax.axhline(p, color="black", ls="--", label="E[X_1] = 0.35")
ax.set(xlabel="n", ylabel="srednia z n obserwacji",
       title="Prawo wielkich liczb: piec trajektorii srednich")
ax.grid(alpha=.25); ax.legend(fontsize=8, ncol=2)
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/I_mocne_prawo.pdf")
plt.close(fig)
