from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(505)
T, b, n = 1., 0.8, 800
czas = np.linspace(0, T, n+1)
fig, ax = plt.subplots(figsize=(7.1, 3.6))
for _ in range(7):
    dB = rng.normal(0, np.sqrt(T/n), n)
    B = np.r_[0., np.cumsum(dB)]
    most = B-(czas/T)*B[-1]+(czas/T)*b
    ax.plot(czas, most, lw=.9)
ax.plot(czas, b*czas/T, "k--", lw=2, label="E[X_t] = bt/T")
ax.scatter([0, T], [0, b], c="black", s=20, zorder=5)
ax.set(xlabel="t", ylabel="X_t", title="Most Browna: X_0=0, X_T=0.8")
ax.legend(); ax.grid(alpha=.25); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/III_most.pdf")
plt.close(fig)
