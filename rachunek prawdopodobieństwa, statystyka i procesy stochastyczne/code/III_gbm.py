from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(502)
mu, sigma, T, n, x0 = 0.25, 0.7, 2., 200, 1.
dt = T/n
dB = rng.normal(0, np.sqrt(dt), n)
B = np.r_[0., np.cumsum(dB)]
czas = np.linspace(0, T, n+1)
sciezka_dokladna = x0*np.exp((mu-sigma**2/2)*czas+sigma*B)
schemat = np.empty(n+1); schemat[0] = x0
for k in range(n):
    schemat[k+1] = schemat[k]*(1+mu*dt+sigma*dB[k])
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.plot(czas, sciezka_dokladna, label="rozwiazanie dokladne")
ax.plot(czas, schemat, "--", label="Euler-Maruyama (ta sama B)")
ax.set(xlabel="t", ylabel="X_t", title="Geometryczny ruch Browna")
ax.grid(alpha=.25); ax.legend(); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/III_gbm.pdf")
plt.close(fig)
