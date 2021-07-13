import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.gca(projection='3d')
def atractor(w,t,p):
    x,y,z = w
    a,b,c=p
    dwdt = [a*(y-x),x*(b-z)-y,x*y-c*z]
    return dwdt
t=np.linspace(0,60,10000 )
p=[5,28,2];
w0=[.1,.2,.3]
sol = odeint(atractor, w0, t, args=(p,))
X=sol[:,0];
Y=sol[:,1];
Z=sol[:,2];
ax.plot3D(X, Y,Z,'m')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')