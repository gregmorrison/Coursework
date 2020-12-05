import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)		


kT=4.1				#kT in pN nm
zeta=20				# friction coefficient (pN us/nm).  
					#  approx value of r a 1um sphere in water
m=4.2				#  approx mass of a 1um sphere of polystyrene
dt=0.02				# timestep
nstep=100000

xvals=np.zeros(nstep)
tvals=np.zeros(nstep)


def externalForce(x,k):
	x0=int(x);
	center=(float(x0))+1.0/2.0
	return -k*(x-center)
	
t=0
x=0
xold=x;
xnew=x;


stiffness=2*zeta*kT
for i in range(nstep):
	f=externalForce(x,stiffness)
	R=np.random.normal(0,1)*np.sqrt(2*zeta*kT/dt)
	xnew=x
	xnew+=(x-xold)*(1-zeta*dt/2/m)/(1+zeta*dt/2/m)
	xnew+=(f+R)*dt*dt/m/(1+zeta*dt/2/m)
	xold=x;
	x=xnew;
	t=t+dt
	
	xvals[i]=x;
	tvals[i]=t;

plt.scatter(tvals,xvals,c='b',s=1)
plt.show()
	