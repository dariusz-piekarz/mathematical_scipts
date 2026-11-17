from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(203)
n, M = 30, 30000
# X_i ~ Exp(1): E[X_i] = Var(X_i) = 1
z = (rng.exponential(size=(M, n)).sum(axis=1) - n) / np.sqrt(n)
x = np.linspace(-4, 4, 400)
phi = np.exp(-x*x/2) / np.sqrt(2*np.pi)
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.hist(z, bins=65, range=(-4, 4), density=True, alpha=.55,
        label="symulacja: n = 30")
ax.plot(x, phi, color="black", lw=2, label="gestosc N(0,1)")
ax.set(xlabel="znormalizowana suma", ylabel="gestosc",
       title="Centralne twierdzenie graniczne")
ax.legend(); ax.grid(alpha=.2); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/I_ctg.pdf")
plt.close(fig)
