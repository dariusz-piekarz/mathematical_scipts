from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(506)
T, n, lam = 3., 1200, 3.
t = np.linspace(0, T, n+1)
dB = rng.normal(0, np.sqrt(T/n), n)
B = np.r_[0., np.cumsum(dB)]
czasy = np.cumsum(rng.exponential(scale=1/lam, size=80))
czasy = czasy[czasy <= T]
rozmiary = rng.normal(0, 0.65, len(czasy))
J = np.r_[0., np.cumsum(rozmiary)]
L = B + J[np.searchsorted(czasy, t, side="right")]
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.plot(t, B, lw=1, label="czesc ciagla B_t")
ax.plot(t, L, lw=1, label="L_t=B_t+skoki")
for s in czasy:
    ax.axvline(s, color="grey", alpha=.13)
ax.set(xlabel="t", ylabel="wartosc procesu",
       title="Suma ruchu Browna i zlozonego procesu Poissona")
ax.grid(alpha=.25); ax.legend(); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/III_levy.pdf")
plt.close(fig)
