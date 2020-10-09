import numpy as np
import random
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

wall=60
signal=200

T=1
dt=0.001
noiseScale=.01


npoints=int(T/dt)
tvals=np.linspace(0,T,npoints)
x=np.sin(2*np.pi*tvals*signal)+.5*np.sin(2*np.pi*tvals*wall)+np.random.normal(0,noiseScale,tvals.size);

trans=fft(x)

plt.scatter(tvals,x)
plt.show()


mag=np.abs(trans);
plt.plot(mag)

plt.show()
