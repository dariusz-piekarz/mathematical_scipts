from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(304)
p, eps, M = 0.4, 0.15, 120000
ns = np.array([10, 20, 40, 80, 160])
emp = []
for n in ns:
    srednie = rng.binomial(n, p, size=M) / n
    emp.append(np.mean(np.abs(srednie-p) >= eps))
oszacowanie = 2*np.exp(-2*ns*eps**2)
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.semilogy(ns, emp, "o-", label="czestosc empiryczna")
ax.semilogy(ns, oszacowanie, "s--", label="granica Hoeffdinga")
ax.set(xlabel="liczba obserwacji n", ylabel="prawdopodobienstwo / granica",
       title="Ogon sredniej Bernoulliego, |srednia-p| >= 0.15")
ax.grid(alpha=.25, which="both"); ax.legend()
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/I_hoeffding.pdf")
plt.close(fig)
