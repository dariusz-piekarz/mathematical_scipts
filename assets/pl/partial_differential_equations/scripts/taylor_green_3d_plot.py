"""Taylor–Green vortex: physically specified initial field in a periodic 3D cube.

u0=(sin(x) cos(y) cos(z), -cos(x) sin(y) cos(z), 0).

The streamlines at t=0 lie on z=constant planes. Colors represent omega_z,
NOT the magnitude of the 3D vorticity vector. This is an initial condition
for the 3D Navier–Stokes equations, not an exact solution for arbitrary t.

Outputs an interactive Plotly HTML file and a Matplotlib PNG for LaTeX.
"""
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
from matplotlib import cm, colors
from matplotlib.ticker import FuncFormatter
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parents[1]
FIGS = ROOT / 'figures'
FIGS.mkdir(exist_ok=True)
PI = np.pi


def field(x,y,z):
    return np.sin(x)*np.cos(y)*np.cos(z), -np.cos(x)*np.sin(y)*np.cos(z), np.zeros_like(np.asarray(x))


def omega_z(x,y,z):
    return 2*np.sin(x)*np.sin(y)*np.cos(z)


def curve(x0,y0,z0, duration=18):
    def rhs(t, xy):
        return (np.sin(xy[0])*np.cos(xy[1])*np.cos(z0),
                -np.cos(xy[0])*np.sin(xy[1])*np.cos(z0))
    sol=solve_ivp(rhs, (0,duration), (x0,y0), t_eval=np.linspace(0,duration,280),rtol=2e-8,atol=2e-10)
    return sol.y[0],sol.y[1],np.full_like(sol.y[0],z0)


levels=[PI/4, 3*PI/4, 5*PI/4]
x=np.linspace(0,2*PI,68)
y=np.linspace(0,2*PI,68)
X,Y=np.meshgrid(x,y)

# Exact, not a pictorial reconstruction: planar streamline slices of the given field.
fig=plt.figure(figsize=(10.8,7.4),dpi=170)
ax=fig.add_subplot(111,projection='3d')
ax.set_box_aspect((1,1,0.78))
cmap=cm.RdBu_r
norm=colors.Normalize(vmin=-1.6,vmax=1.6)
for j,z in enumerate(levels):
    W=omega_z(X,Y,z)
    rgb=cmap(norm(W))
    rgb[...,3]=0.38
    ax.plot_surface(X,Y,np.full_like(X,z),facecolors=rgb,shade=False,
                    rstride=2,cstride=2,antialiased=False,zorder=-10)
    # Contours are exactly level sets of psi = sin(x) sin(y) cos(z).
    psi=np.sin(X)*np.sin(Y)*np.cos(z)
    nonzero=np.r_[np.linspace(-.62,-.16,3),np.linspace(.16,.62,3)]*abs(np.cos(z))
    ax.contour(X,Y,psi,levels=nonzero,zdir='z',offset=z,colors='#272731',linewidths=0.58,alpha=.7)
    # Horizontal vectors confirm u_3 = 0.
    gx=np.linspace(0.40,2*PI-0.40,10)
    gy=np.linspace(0.40,2*PI-0.40,10)
    XX,YY=np.meshgrid(gx,gy)
    U,V,Z=field(XX,YY,z)
    mask=(np.abs(U)+np.abs(V))>0.15
    ax.quiver(XX[mask],YY[mask],z*np.ones(mask.sum()),U[mask],V[mask],Z[mask],
              length=.25,normalize=True,color='#161825',linewidth=.5,arrow_length_ratio=.34,alpha=.70)
ax.set(xlim=(0,2*PI),ylim=(0,2*PI),zlim=(0,2*PI),
       xlabel='$x$',ylabel='$y$',zlabel='$z$')
ax.set_xticks([0,PI,2*PI],['0','$\\pi$','$2\\pi$'])
ax.set_yticks([0,PI,2*PI],['0','$\\pi$','$2\\pi$'])
ax.set_zticks([0,PI,2*PI],['0','$\\pi$','$2\\pi$'])
ax.view_init(elev=25,azim=-62)
ax.xaxis.pane.fill=False;ax.yaxis.pane.fill=False;ax.zaxis.pane.fill=False
ax.grid(alpha=.15)
sm=cm.ScalarMappable(norm=norm,cmap=cmap);sm.set_array([])
cbar=fig.colorbar(sm,ax=ax,shrink=.66,pad=.075)
cbar.set_label('$\\omega_z(x,y,z)$ w chwili $t=0$',fontsize=10)
ax.set_title('Wir Taylora–Greena 3D: przekroje pola początkowego',pad=20,fontsize=15)
fig.text(.10,.045,r'$u_0=(\sin x\cos y\cos z,\,-\cos x\sin y\cos z,\,0)$',fontsize=12)
fig.savefig(FIGS/'taylor_green_3d_slices.png',bbox_inches='tight')
plt.close(fig)

# Interactive Plotly streamlines, computed by numerically integrating the ODE.
P=go.Figure()
for z in levels:
    P.add_trace(go.Surface(x=X,y=Y,z=np.full_like(X,z),
       surfacecolor=omega_z(X,Y,z),colorscale='RdBu',reversescale=False,
       cmin=-1.6,cmax=1.6,opacity=0.26,showscale=(z==levels[0]),
       colorbar=dict(title='omega_z'),name=f'z={z/PI:.2g} pi',showlegend=False))
    for cx in (PI/2,3*PI/2):
        for cy in (PI/2,3*PI/2):
            for r in (.30,.62,.96):
                xx,yy,zz=curve(cx+r,cy,z,duration=15)
                w=omega_z(cx,cy,z)
                col='#bc3339' if w>0 else '#3159b0'
                P.add_trace(go.Scatter3d(x=xx,y=yy,z=zz,mode='lines',
                        line=dict(color=col,width=4),showlegend=False,hoverinfo='skip'))
P.update_layout(title='Wir Taylora–Greena 3D — linie prądu u₀ i składowa wirowości ω_z',
               scene=dict(xaxis_title='x',yaxis_title='y',zaxis_title='z',
                aspectmode='cube',xaxis=dict(range=[0,2*PI]),
                yaxis=dict(range=[0,2*PI]),zaxis=dict(range=[0,2*PI])),
                margin=dict(l=0,r=0,t=50,b=0))
P.write_html(FIGS/'taylor_green_3d_interactive.html',include_plotlyjs=True)

# Analytical verification of incompressibility and energy at t=0:
# div(u0) = cos(x)cos(y)cos(z)-cos(x)cos(y)cos(z)=0.
# int_{[0,2pi]^3} |u0|^2 dx = (2pi)^3/4.
print('PNG:',FIGS/'taylor_green_3d_slices.png')
print('HTML:',FIGS/'taylor_green_3d_interactive.html')
