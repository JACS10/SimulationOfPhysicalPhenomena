from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def sistema(y, t, p):
    x1, v1, x2, v2 = y
    m1, m2, k1, k2, L1, L2, b1, b2 = p
    dydt = [v1, (-b1 * v1 - k1 * (x1 - L1) + k2 * (x2 - x1 - L2)) / m1,
            v2, (-b2 * v2 - k2 * (x2 - x1 - L2)) / m2]
    return dydt

# PARAMETROS
# masas:
m1 = 8
m2 = 8
# constantes de los resortes
k1 = 5.0
k2 = 50.0
# longitudes
L1 = 1.0
L2 = 1.0
# coeficientes de friccion
b1 = 5.0
b2 = 5.0

# CONDICIONES INICIALES
x1 = 0.5
v1 = 5.0
x2 = 2.0
v2 = 5.0

# tiempo
t = np.linspace(0,10,50)

p = [m1, m2, k1, k2, L1, L2, b1, b2]
y0 = [x1, v1, x2, v2]

sol = odeint(sistema, y0, t, args=(p,))


fig = plt.figure(10)
ax = fig.add_subplot(211)
bx = fig.add_subplot(212)

lns = []

for i in range(len(sol)):
    p1, = ax.plot(sol[i,0],0,marker = 's',markersize = 10, 
                  color = 'c',ds='steps-pre', label='$m1$')
    p2, = ax.plot(sol[i,2],0,marker = 's',markersize = 10, 
                  color = 'k',ds='steps-post', label='$m2$')
    tm  = ax.text(0.25, 0.4, 'tiempo = %.1fs' % t[i])
    ax.axhline(y=-0.038, color = 'black')
    ax.set_ylim([-0.3,0.3])
    ax.set_yticks([])
    ax.set_title('Sistema masa-resorte con $k1< k2$, $v1=v2$ y $m1=m2$')
    
    bx.plot(t,sol[:,0], color = 'c', label= '$m1$')
    bx.plot(t,sol[:,2], color = 'k', label= '$m2$')
    p3, = bx.plot(t[i],sol[i,0], color = 'c', marker = 'o',ms = 10)
    p4, = bx.plot(t[i],sol[i,2], color = 'k', marker = 'o',ms = 10)
    bx.set_xlabel('tiempo [s]')
    bx.set_ylabel('Posicion')
    bx.legend(["$m1$", "$m2$"])
    
    lns.append([p1, p2, tm, p3,p4])   
    
    
ani = animation.ArtistAnimation(fig, lns, interval=1)

#ani.save('MR28.gif', dpi=80, writer='imagemagick')