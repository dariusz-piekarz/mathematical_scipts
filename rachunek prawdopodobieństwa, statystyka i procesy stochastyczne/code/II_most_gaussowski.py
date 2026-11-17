from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(403)
n = 800
czas = np.linspace(0, 1, n+1)
fig, ax = plt.subplots(figsize=(7.1, 3.6))
for _ in range(6):
    dB = rng.normal(0, np.sqrt(1/n), n)
    B = np.r_[0., np.cumsum(dB)]
    most = B-czas*B[-1]  # most Browna 0->0
    ax.plot(czas, most, alpha=.8, lw=1)
ax.plot(czas, np.zeros_like(czas), "k--", lw=1, label="E[most_t] = 0")
ax.set(xlabel="t", ylabel="most Browna",
       title="Warunkowanie gaussowskie: B_t - t B_1")
ax.legend(); ax.grid(alpha=.25); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/II_most_gaussowski.pdf")
plt.close(fig)
