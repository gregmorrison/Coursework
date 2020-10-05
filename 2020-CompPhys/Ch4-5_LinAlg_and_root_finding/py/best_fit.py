import numpy as np
import random
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitfunction(t,A,B,omega):
	return A*np.sin(omega*t)+B#*np.cos(omega*t)

x=np.linspace(-10,10,201);
y=2*np.sin(2*np.pi*x/10)+np.random.normal(0,.1,x.size)

#fit to A sin(omega t)+B cos(omega t)
init_vals=[100,0,2*np.pi/10]
fits,cov=curve_fit(fitfunction,x,y,p0=init_vals)
print(fits)

plt.scatter(x,y)
plt.plot(x,fitfunction(x,*fits))
plt.show()