from pathlib import Path
import math
import numpy as np
import matplotlib.pyplot as plt

lam = 3.0
k = np.arange(13)
poisson = np.array([math.exp(-lam) * lam**int(j)
                    / math.factorial(int(j)) for j in k])
fig, ax = plt.subplots(figsize=(7.1, 3.7))
ax.plot(k, poisson, "ko-", label="Poisson(3)", linewidth=2)
for n in (10, 30, 150):
    p = lam / n
    pmf = np.array([math.comb(n, int(j)) * p**j *
                    (1-p)**(n-j) for j in k])
    ax.plot(k, pmf, "o--", label=f"Bin({n}, {p:.3g})")
ax.set(xlabel="k", ylabel="P(X = k)", title="Przyblizenie Poissona")
ax.set_xticks(k[::2]); ax.legend(fontsize=8); ax.grid(alpha=.25)
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/I_poisson.pdf")
plt.close(fig)
