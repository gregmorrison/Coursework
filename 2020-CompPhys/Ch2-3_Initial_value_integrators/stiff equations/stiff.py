import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import time

import sys
sys.path.append('./NM4P/Python/nm4p/')  #this is required to import a module from outside of the current directory.
										# you may need to change this to have the code run on your computer!
										
from rk4 import rk4						#this imports rk4 from Garcia's github.  Note the file name 
										# is rk4 (the first "rk4" here), and we import the "rk4" function
										# (the second "rk4")
										
								
										
def deriv(x,t,param):
	return X*X-X*X*X
							
										


x0=.0001;
t=0.0
T=2/x0;  #this is a useful timescale, as we will see from the results.
#these are the parameters for our system


dt=0.1
niter=(int)(T/dt)
#these are the parameters for our integrator


X=x0
sampleTimes=np.asarray(range(int(niter)+1))*dt
result=np.asarray([x0])		#where we will store the data for plotting


tm0=time.time();
for titer in range(int(niter)):
	X=rk4(X,t,dt,deriv,[])
	result=np.append(result,[X])  #store the value of theta we saw
	t=t+dt
tmf=time.time();
print("evaluation took:  ");
print(tmf-tm0);

	
plt.plot(sampleTimes,result)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()
	
	
	