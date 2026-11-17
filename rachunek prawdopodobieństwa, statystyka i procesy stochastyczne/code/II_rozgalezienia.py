from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(405)
M, G = 15000, 20
pop = np.ones(M, dtype=np.int64)
q_emp = [0.0]
q_exact = [0.0]
for _ in range(G):
    # Kazdy osobnik ma 0 dzieci z p=0.3 albo 2 z p=0.7.
    pop = 2*rng.binomial(pop, 0.7)
    q_emp.append(np.mean(pop == 0))
    q_exact.append(0.3 + 0.7*q_exact[-1]**2)
q = 3/7  # najmniejszy punkt staly g(s)=0.3+0.7*s^2
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.plot(q_emp, "o", ms=3, label="czestosc wymarcia do pokolenia n")
ax.plot(q_exact, "-", label="iteracja q_(n+1)=g(q_n)")
ax.axhline(q, color="black", ls="--", label="q = 3/7")
ax.set(xlabel="pokolenie n", ylabel="prawdopodobienstwo wymarcia",
       title="Proces Galtona-Watsona: punkty stale")
ax.grid(alpha=.25); ax.legend(fontsize=8); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/II_rozgalezienia.pdf")
plt.close(fig)
