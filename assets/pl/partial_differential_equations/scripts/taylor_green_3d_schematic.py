"""Conceptual three-dimensional schematic for a Taylor–Green vortex initial field.

This depicts planar vortex-cell topology at several z slices. It is not a
numerical trajectory integration nor a map of the full vorticity magnitude.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / 'figures'
FIGURES.mkdir(parents=True, exist_ok=True)
pi = np.pi
fig = plt.figure(figsize=(10.6, 6.4), dpi=150)
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect((1, 1, .84))

def cell(cx: float, cy: float, z: float, clockwise: bool, size: float):
    # Stylized ellipses indicate topological vortex cells, not computed trajectories.
    t = np.linspace(0, 2 * pi, 190)
    for r in (.36, .63, .87):
        x = cx + r * size * np.cos(t)
        y = cy + r * size * np.sin(t)
        ax.plot(x, y, np.full_like(x, z), color='#244B6E' if clockwise else '#A04840', lw=1.7, alpha=.93)
    t0 = .20 if clockwise else 2.35
    sign = -1 if clockwise else 1
    for tt in (t0, t0 + 1.0):
        xx = cx + .68 * size * np.cos(tt)
        yy = cy + .68 * size * np.sin(tt)
        tx, ty = -np.sin(tt)*sign, np.cos(tt)*sign
        ax.quiver(xx, yy, z, tx, ty, 0, length=.33, normalize=True,
                  arrow_length_ratio=.48, color='#1C2630', linewidth=1.1)

for z, alpha in [(1.05, .26), (3.14,.16), (5.05,.26)]:
    gx, gy = np.meshgrid(np.linspace(0, 2*pi, 2), np.linspace(0, 2*pi, 2))
    ax.plot_surface(gx, gy, np.full_like(gx,z), color='#D5DBDE', alpha=alpha, shade=False)
    for i,cx in enumerate((pi/2, 3*pi/2)):
      for j,cy in enumerate((pi/2, 3*pi/2)):
        cell(cx,cy,z,clockwise=((i+j+(z>pi))%2==0),size=1.2)
ax.set(xlim=(0,2*pi),ylim=(0,2*pi),zlim=(0,2*pi),xlabel='$x$',ylabel='$y$',zlabel='$z$')
ax.set_xticks([0,pi,2*pi],['0','$\\pi$','$2\\pi$'])
ax.set_yticks([0,pi,2*pi],['0','$\\pi$','$2\\pi$'])
ax.set_zticks([0,pi,2*pi],['0','$\\pi$','$2\\pi$'])
ax.view_init(elev=25,azim=-62)
ax.xaxis.pane.fill=False;ax.yaxis.pane.fill=False;ax.zaxis.pane.fill=False
ax.grid(alpha=.14)
ax.set_title('Schemat komórek wiru Taylora–Greena 3D',pad=16)
fig.text(.13,.065,'Schemat koncepcyjny: przepływ w płaszczyznach $z=\\mathrm{const}$; nie są to trajektorie numeryczne.',fontsize=10)
fig.savefig(FIGURES / 'taylor_green_3d_schematic.png',bbox_inches='tight')
plt.close(fig)
print(FIGURES/'taylor_green_3d_schematic.png')
