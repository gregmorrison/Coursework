import numpy
import random
import math
import matplotlib.pyplot as plt

def U(r,c):
	x=numpy.linalg.norm(r);  #compute |r|
	x2=x*x
	x3=x*x2
	x4=x2*x2	
	return x4/4-(c+1)*x3+(c*c+3*c+1.5)*x2-(2*c*c+3*c+1)*x
	#that quanity is \int dx (x-1)(x-c-1)(x-2c-1)
	
	
def metropolis(r,rnew,c):
	e=U(r,c)
	enew=U(rnew,c)
	if e>enew:
		return True
	else:
		if random.random()<math.exp((e-enew)/kT):
			return True
		else:
			return False
			


nstep=10000 	 #number of steps 
dim=1			#dimensionality
kT=4.1			
dx=0.2			#changes to the state are dx*R, with R a normally distrib number.

rlist=[0] * nstep		#where we store |r(t)|
tlist=[0] * nstep
r=[0]*dim				#where we store instantaneous r
c=2						#parameter for the energy

t=0;
for step in range(nstep):
	rnew=r+dx*numpy.random.normal(0, 1, dim)  
	# new position is old position plus gaussian random step with dx
	if metropolis(r,rnew,c):
		r=rnew
	x=numpy.linalg.norm(r)
	rlist[step]=x*x
	t+=1;
	tlist[step]=t;
	




plt.plot(tlist,rlist);
plt.show()


