import numpy as np
from scipy import integrate
import matplotlib as mp
import matplotlib.pyplot as plt
import time

def deriv(t,X):
	return X*X-X*X*X
	
	
x0=0.00001
t=np.linspace(0, 1.2/x0, 1000);
t0=time.time();
soln=integrate.solve_ivp(deriv,[0,1.2/x0],[x0])
#soln=integrate.solve_ivp(deriv,[0,1.2/x0],[x0],method='RK45',t_eval=t,atol=.001)
tf=time.time();
print('took '+str(tf-t0)+' s')

plt.plot(soln.t,soln.y[0])
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()