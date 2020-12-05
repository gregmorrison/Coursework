import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)		


kT=4.1				#kT in pN nm
zeta=20				# friction coefficient (pN us/nm).  
					#  approx value of r a 1um sphere in water
m=4.2				#  approx mass of a 1um sphere of polystyrene
dt=0.001				# timestep
nstep=10000
nrun=10


xvals=np.zeros(nstep)
xsqvals=np.zeros(nstep)
vsqvals=np.zeros(nstep)
tvals=np.zeros(nstep)

print('predicted timescale:  ')
print(m/zeta)




for i in range(nrun):
	t=0
	x=0
	xold=x;
	xnew=x;  #initialize!

	for i in range(nstep):
		R=np.random.normal(0,1)*np.sqrt(2*zeta*kT/dt)
		xnew=x
		xnew+=(x-xold)*(1-zeta*dt/2/m)/(1+zeta*dt/2/m)
		xnew+=(R)*dt*dt/m/(1+zeta*dt/2/m)
		v=(xnew-xold)/2/dt;
		
		xold=x;
		x=xnew;
		t=t+dt
		
		xvals[i]+=x/nrun;
		xsqvals[i]+=x*x/nrun;
		vsqvals[i]+=v*v/nrun;
		tvals[i]=t;
	
plt.scatter(tvals,xvals)
plt.show()

plt.scatter(tvals,xsqvals)
plt.plot(tvals*1.1,tvals*(2*kT/zeta))
plt.show()

plt.scatter(tvals,vsqvals)
plt.plot(tvals*1.1,np.ones(nstep)*(kT/m))
plt.show()

