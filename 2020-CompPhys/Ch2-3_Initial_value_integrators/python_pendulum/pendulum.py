import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt


import sys
sys.path.append('./NM4P/Python/nm4p/')  #this is required to import a module from outside of the current directory.
										# you may need to change this to have the code run on your computer!
										
from rk4 import rk4						#this imports rk4 from Garcia's github.  Note the file name 
										# is rk4 (the first "rk4" here), and we import the "rk4" function
										# (the second "rk4")
										
								
										
def deriv(X,t,param):
	return np.array([X[1],-np.sin(X[0])])  # this is dX/dt = deriv(X,t)
											#note that this funny form is chosen to match Garcia's rk4 function
							
										

def euler(X,t,tau,derivs,params):		#this defines the euler update.  Pretty easy to code, but remember it's innacurate
	return X+tau*deriv(X,t,params)		#the function definition matches rk4


def positionVerlet(X,t,tau,derivs,params):
	deriv=derivs(X,t,params)  #this computes dx/dt and 
	X[0]=X[0]+dt*X[1]+dt*dt/2*deriv[1]  #compute the update for position
	deriv2=derivs(X,t,params)
	X[1]=X[0]+dt/2
# we can define a verlet function if we want, but it can't match the rk4 method.  
	




theta=0.1*np.pi
omega=0.0
t=0.0
T=30.0
g=9.81
L=1.0
#these are the parameters for our system


dt=0.01
niter=T/dt
#these are the parameters for our integrator


X=np.array([0.0,0.0],dtype=float)  #where we will store the data at each timestep for euler / rk4
sampleTimes=np.asarray(range(int(niter)+1))*dt
rk4Result=np.asarray([theta])		#where we will store the data for plotting
eulerResult=np.asarray([theta])
verletResult=np.asarray([theta])



X[0]=theta
X[1]=omega
t=0
for titer in range(int(niter)):
	X=euler(X,t,dt,deriv,[])
	eulerResult=np.append(eulerResult,[X[0]])  #store the value of theta we saw
	t=t+dt
	
		
	
	
	
	
X[0]=theta
X[1]=omega
t=0
for titer in range(int(niter)):
	X=rk4(X,t,dt,deriv,[])
	rk4Result=np.append(rk4Result,[X[0]])  #store the value of theta we saw
	t=t+dt

	
	
	
t=0
X[1]=theta  												#initial value of the angle
X[0]=theta+omega*dt+dt*dt*(-np.sin(theta))/2					#next value of the angle (startup)
np.append(verletResult,[X[0]])
for titer in range(int(niter)):
	xcurr=X[0]									#current value of x
	X[0]=2*X[0]-X[1]+dt*dt*(-np.sin(xcurr))		#update the value of the current x
	X[1]=xcurr									#update the value of the old x
	verletResult=np.append(verletResult,[X[0]])  			#store the value of theta we saw
	t=t+dt



fig,(a1,a2)=plt.subplots(1,2)

a1.plot(sampleTimes,eulerResult/2/np.pi,color='b',label='Euler')
a1.plot(sampleTimes,rk4Result/2/np.pi,color='r',label='rk4')
a1.plot(sampleTimes,verletResult/2/np.pi,color='k',label='Verlet')

ax1=a1.axes

a1.legend(loc='lower left')
a1.set_xlabel('t')
a1.set_ylabel('theta/2pi')
a2.plot(sampleTimes,verletResult-rk4Result,color='k',linestyle='-')
a2.set_xlabel('t')
a2.set_ylabel('theta_RK4 - theta_verlet')
plt.tight_layout()
plt.show()	
