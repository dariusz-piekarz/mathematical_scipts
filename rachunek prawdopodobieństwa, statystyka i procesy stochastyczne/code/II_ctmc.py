from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(402)
a, b, T, M = 0.7, 0.4, 6., 10000
czas = np.linspace(0, T, 61)
ilosci = np.zeros_like(czas)
# Stan poczatkowy: 0; naprzemienne skoki 0->1 i 1->0.
for _ in range(M):
    t, stan, skoki = 0., 0, []
    while True:
        t += rng.exponential(1 / (a if stan == 0 else b))
        if t > T:
            break
        skoki.append(t)
        stan = 1 - stan
    ilosci += np.searchsorted(skoki, czas, side="right") % 2
emp = ilosci / M
exact = a/(a+b) * (1-np.exp(-(a+b)*czas))
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.plot(czas, emp, label="symulacja, 10 000 trajektorii")
ax.plot(czas, exact, "k--", label="P_01(t), rozwiazanie rownan")
ax.set(xlabel="t", ylabel="P(X_t = 1 | X_0 = 0)",
       title="Dwustanowy lancuch Markowa w czasie ciaglym")
ax.legend(); ax.grid(alpha=.25); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/II_ctmc.pdf")
plt.close(fig)
