from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

P = np.array([[0.85, 0.15], [0.25, 0.75]])
pi = np.array([0.625, 0.375])  # pi P = pi
p = np.array([1.0, 0.0])
values = [p.copy()]
for _ in range(30):
    p = p @ P
    values.append(p.copy())
values = np.array(values)
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.plot(values[:, 0], "o-", ms=3, label="P(X_n = 0 | X_0=0)")
ax.axhline(pi[0], color="black", ls="--", label="pi_0 = 0.625")
ax.set(xlabel="n", ylabel="prawdopodobienstwo", ylim=(.55, 1.02),
       title="Zbieznosc rozkladu lancucha dwustanowego")
ax.grid(alpha=.25); ax.legend(); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/I_markow.pdf")
plt.close(fig)
