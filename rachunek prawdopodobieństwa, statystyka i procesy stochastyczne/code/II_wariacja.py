from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(404)
N = 2**15
dB = rng.normal(0, np.sqrt(1/N), size=N)
B = np.r_[0., np.cumsum(dB)]
ns = 2**np.arange(4, 16)
qv, tv = [], []
for n in ns:
    przyrosty = np.diff(B[::N//n])
    qv.append(np.sum(przyrosty**2))
    tv.append(np.sum(np.abs(przyrosty)))
fig, ax = plt.subplots(figsize=(7.1, 3.6))
ax.plot(ns, qv, "o-", label="suma kwadratow")
ax.axhline(1, color="black", ls="--", label="granica t = 1")
ax.set_xscale("log", base=2)
ax.set(xlabel="liczba przedzialow n", ylabel="wariacja kwadratowa")
ax2 = ax.twinx()
ax2.plot(ns, tv, "s:", color="tab:orange", label="suma modulow")
ax2.set_ylabel("suma modulow przyrostow")
ax.set_title("Wariacja kwadratowa i zwykla na jednej trajektorii")
ax.grid(alpha=.25)
lines = ax.get_lines() + ax2.get_lines()
ax.legend(lines, [l.get_label() for l in lines], fontsize=8, loc="upper left")
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[1] / "figures/II_wariacja.pdf")
plt.close(fig)
