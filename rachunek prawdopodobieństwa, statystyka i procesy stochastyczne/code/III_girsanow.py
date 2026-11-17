from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(504)
T, theta, M = 1., 1., 60000
B_T = rng.normal(0, np.sqrt(T), M)
# Z = dQ/dP: wartosci B_T pod Q maja rozklad N(theta*T, T).
w = np.exp(theta*B_T-0.5*theta**2*T)
x = np.linspace(-3.5, 5, 400)
phi_Q = np.exp(-(x-theta*T)**2/(2*T))/np.sqrt(2*np.pi*T)
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.hist(B_T, bins=65, range=(-3.5, 5), density=True,
        weights=w, alpha=.5, label="histogram wazony przez Z")
ax.plot(x, phi_Q, "k-", lw=2, label="gestosc N(theta*T, T)")
ax.set(xlabel="x", ylabel="gestosc", title="Zmiana miary: przesuniecie dryfu")
ax.legend(); ax.grid(alpha=.25); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/III_girsanow.pdf")
plt.close(fig)
