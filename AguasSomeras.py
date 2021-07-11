import numpy as np
import pylab as pl

h0 = np.loadtxt('h0.dat')
eta = np.loadtxt('eta.dat')
u = np.loadtxt('u.dat')

i = 100
x= np.linspace(0,2000,101)

frames = []

for i in range(0,np.size(eta, axis=0),10):
    time = ['t=', 2*i, 'segundos']
    texto = "".join(str(e) for e in time)
    pl.figure(i/10)
    pl.plot(x,-h0, 'k',lw=2) 
    pl.ylim([-2,2])
    pl.plot(x,eta[i,:])
    pl.text(80,1.5,texto)
    new_frame= pl.figure(i)
    frames.append(new_frame)
