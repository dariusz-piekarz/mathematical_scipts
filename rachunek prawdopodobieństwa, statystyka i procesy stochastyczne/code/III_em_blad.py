from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(503)
mu, sigma, T, M, N = 0.3, 0.6, 1., 3000, 1024
dB = rng.normal(0, np.sqrt(T/N), size=(M, N))
W_T = dB.sum(axis=1)
X_T = np.exp((mu-sigma**2/2)*T+sigma*W_T)
ns = np.array([16, 32, 64, 128, 256, 512, 1024])
errors = []
for n in ns:
    dW = dB.reshape(M, n, N//n).sum(axis=2)
    X_em = np.prod(1+mu*(T/n)+sigma*dW, axis=1)
    errors.append(np.sqrt(np.mean((X_em-X_T)**2)))
errors = np.array(errors)
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.loglog(T/ns, errors, "o-", label="blad RMS w chwili T")
ax.loglog(T/ns, errors[0]*np.sqrt((T/ns)/(T/ns[0])),
          "k--", label="wzorzec h^(1/2)")
ax.set(xlabel="krok h", ylabel="(E|X_EM(T)-X(T)|^2)^(1/2)",
       title="Silny blad schematu Eulera-Maruyamy")
ax.grid(alpha=.25, which="both"); ax.legend(); fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/III_em_blad.pdf")
plt.close(fig)
