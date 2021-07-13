import numpy as np 
import matplotlib.pyplot as plt 
import pylab as pl
#import Datos_Strain
from scipy import signal

#import math

pi = np.pi 

#Velocidad de la luz
c=3*10**(8)

#Constante gravitacional
G=6.67*10**(-11)

#Distancia del evento
r=1850*(3.08*10**(19))
#r = 100*(3.08*10**(74))

#Masa del solecito
m=9.989*10**(30)

m1=39.6*m

#Masa estrella random
m2=29.4*m

#Masa total
M=m1+m2

#Masa reducida
mu=m1*m2/M

#Masa chirp
Mo=(mu**(3)**(1/5))*(M**(2)**(1/5))

#Radio entre la masa reducida y la masa total
nu=mu/M

#Tiempo final del tiempo inspiral 
#tc=124175
tc= 167700.0
#tc=	11875.292565

#Valor de la fase espiral en tc
phic=pi/4

#Tiempo inicial
t_0= 0.0
#t_0 = -Datos_Strain.timeH1[len(Datos_Strain.timeH1)-1]

#Tiempo final
t_f=32.0
#t_f = 10000
#t_f = Datos_Strain.timeH1[len(Datos_Strain.timeH1)-1]

#Frecuencia de sampleo
fs=10.0
#fs = 4096.0 

#Numero de pasos
N=fs*(tc/10)

#Periodo
T=1/fs

#Conjunto de tiempo, empieza en t0, termina en tf, pasitos de tf/fs
time= np.linspace(t_0,t_f,int(N))

#Definir variables
Thet=   [0]*len(time)
phigw=  [0]*len(time)
fgw=    [0]*len(time)
hp=     [0]*len(time)
hc=     [0]*len(time)

#Reescribir variables
for t in range(len(time)):
    Thet[t]     =     ((c**3)*nu/(5*G*M))*np.abs(tc-t)
    phigw[t]    =     -(1/nu)*((Thet[t]**(0.625))+
         ((3715/8064 + 55*(nu)/96)*(Thet[t]**(0.375))) - ((3*pi/4)*(Thet[t]**(0.25))) + 
         ((9275495/14450688 + 284875*(nu)/258048 + 1855*(nu**2)/2048)*(Thet[t]**(0.125))))
    fgw[t]      =     ((c**3)/(8*pi*G*M))*((Thet[t]**(-0.375))+ ((743/2688 + 11*nu/32)*(Thet[t]**(-0.625)))- 
       ((3*pi/10)*(Thet[t]**(-0.75)))+ 
       ((1855099/14450688 + 56975*nu/258048 + (371*(nu**2))/2048)*(Thet[t]**(-0.875))))
    hp[t]       =     (4/r)*((G*Mo/(c**2))**(1.667))*((pi*fgw[t]/c)**(0.667))*np.cos(phigw[t])
    hc[t]       =     (4/r)*((G*Mo/(c**2))**(1.667))*((pi*fgw[t]/c)**(0.667))*np.sin(phigw[t])

#POLARICACION h+
plt.figure()
plt.grid()
plt.plot(time, hp)
plt.plot(time, hc)
#pl.xlim(-5.0,-4.75)
#pl.ylim(-1*10**-18,1*10**-18)
plt.title('Tiempo vs h+')
plt.ylabel('Strain')
plt.xlabel('Time [sec]')
plt.show()

#Transformada rapida
X=      np.fft.fft(hp)
freq=   np.fft.fftfreq(len(hp),T)

plt.figure()
plt.grid()
plt.plot(time, np.abs(X)[:int(N)])
#pl.xlim(time[2261-100],time[2261+100])
plt.title('FFT h+')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time')
plt.show()

#Transformada corta
f, t, Zxx = signal.stft(hp, fs, nperseg=100)
plt.pcolormesh(t, f, np.abs(Zxx))
plt.colorbar()
plt.title('h+ STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#Espectrograma
# =============================================================================
# ff, tt, Sxx =signal.spectrogram(hp, fs, nperseg=100)
# 
# plt.pcolormesh(tt, ff, Sxx)
# plt.title('Espectrograma')
# plt.xlabel('Time [sec]')
# plt.colorbar()
# plt.ylabel('Frequency [Hz]')
# plt.grid()
# plt.show()
# 
# =============================================================================
#POLARIZACION hx
#pl.figure()
#pl.grid()
#pl.plot(time,np.abs(hc))
#pl.plot(time,hp)
#pl.xlim(time[2261-100],time[2261+45])
#pl.xlim(tc-10, tc+10)
#plt.title('Tiempo vs hx')
#plt.ylabel('Strain')
#plt.xlabel('Time [sec]')
#plt.show()

#Transformada rapida
#Y=      np.fft.fft(hc)
#freq=   np.fft.fftfreq(len(hc),T)

#pl.figure()
#pl.grid()
#pl.plot(freq[:int(N/2)],np.abs(Y)[:int(N/2)])
#plt.title('FFT hx')
#plt.ylabel('???')
#plt.xlabel('Frequency [Hz]')
#plt.show()

#Transformada corta
f, t, Zyy = signal.stft(hc, fs, nperseg=100)
plt.pcolormesh(t, f, np.abs(Zyy))
plt.colorbar()
plt.title('hx STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()


#Espectrograma
ff, tt, Syy = signal.spectrogram(time, fs, noverlap=128, nperseg=256, nfft=2048)

plt.pcolormesh(tt, ff[0:513], Syy[0:513])
plt.title('Espectrograma')
plt.xlabel('Time [sec]')
plt.colorbar()
plt.ylabel('Frequency [Hz]')
plt.grid()
plt.show()


#pl.figure()
#pl.grid()
#pl.plot(hc,hp)
#plt.show()

#espectrograma, transformada corta y rapida de fourier
