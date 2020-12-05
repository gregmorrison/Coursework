import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

from functions import get_init_energy  #compute energies
from functions import energy_difference  #compute energy differences
#these are externally defined, 

#metropolis criterion
def metropolis(e,enew):  
	if(e>enew):
		return True
	else:
		if np.random.random()<math.exp((e-enew)):
			return True
		else:
			return False


N=20  #size of the lattice
nstep=100000	#steps in the simulation
printstep=2000	#steps between printing
nprint=int(nstep/printstep)
nrun=1

t=np.zeros(nprint)
avm=np.zeros(nprint)
ave=np.zeros(nprint)


np.random.seed(2)

J=0.001  #interaction strength (with kT=1)
b=0  #magnetic field.  This is h in class.  

pbc=True  #this flags whether to use PBCs

for run in range(nrun):

		
	spins=[[0 for _ in range(N)] for _ in range(N)]  #define the spins as all down
	m=0  #initial magnetization is all down
	for i in range(N):
		for j in range(N):
			if np.random.random()<.5:
				spins[i][j]=1  
				m+=1
			else:
				spins[i][j]=-1
				m-=1;			
	e=get_init_energy(spins,J,b,N,pbc)
	#compute initial energy


	for step in range(nstep):  #iterate over steps
		s1=np.random.randint(0,N)
		s2=np.random.randint(0,N)
		#randomly choose a spin to flip.  		
		
		
		enew=e+energy_difference(s1,s2,spins,J,b,N,pbc)
		#compute the energy
		if(metropolis(e,enew)):
		#with the metropolis criterion, choose to flip the spin
			spins[s1][s2]=-spins[s1][s2]
			if spins[s1][s2]>0:
				m+=2
			else:
				m-=2
			#update the magnetization due tot he flip
			e=enew
			#update the energy due to the flip
	
		if step%printstep==0:
			t[int(step/printstep)]=step
			#every printstep, we want to print data
			avm[int(step/printstep)]+=abs(m)/N/N
			ave[int(step/printstep)]+=e/J/N/N

s=np.transpose(spins)
for i in range(N):
	y=[j for j,e in enumerate(s[i]) if e==1]
	x=[i for _ in range(len(y))]
	plt.scatter(x,y,color='b')
ax1=plt.axes()
ax1.set_aspect('equal')
plt.show()


plt.plot(t/nrun,avm/nrun)
plt.show()
plt.plot(t/nrun,ave/nrun)
plt.show()