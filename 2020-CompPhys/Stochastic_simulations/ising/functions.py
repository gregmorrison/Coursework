import numpy as np
import math

			
			

		
		
		
#this computes the energy.  Only use this once.  
def get_init_energy(s,J,b,N,PERIODICBOUNDARIES):
	e=0
	for i in range(N-1):
		for j in range(N-1):
			e+=-s[i][j]*s[i+1][j]
			e+=-s[i][j]*s[i][j+1]
	# bulk contribution
	for i in range(N-1):
		e+=-s[i][N-1]*s[i+1][N-1]
		if(PERIODICBOUNDARIES):
			e+=-s[i][N-1]*s[i][0]
	#right side
	
	for j in range(N-1):
		e+=-s[N-1][j]*s[N-1][j+1]
		if(PERIODICBOUNDARIES):
			e+=-s[N-1][j]*s[0][j]
	#bottom
	
	if(PERIODICBOUNDARIES):
		e+=-s[N-1][N-1]*s[N-1][0]
		e+=-s[N-1][N-1]*s[0][N-1]
	return J*e
	
	
	
	
	
#this computes the energy difference due to a spin flip
def energy_difference(s1,s2,spins,J,b,N,PERIODICBOUNDARIES):
	de=0

	evaluate=True
	t1=s1+1
	t2=s2
	if(t1==N):
		if(PERIODICBOUNDARIES):
			t1=0
		else:
			evaluate=False
			
	if evaluate:
		de+=2*spins[s1][s2]*spins[t1][t2]
		
	
	
	evaluate=True
	t1=s1-1
	t2=s2
	if(t1==-1):
		if(PERIODICBOUNDARIES):
			t1=N-1
		else:
			evaluate=False
			
	if evaluate:
		de+=2*spins[s1][s2]*spins[t1][t2]
		
		
	evaluate=True
	t1=s1
	t2=s2+1
	if(t2==N):
		if(PERIODICBOUNDARIES):
			t2=0
		else:
			evaluate=False
			
	if evaluate:
		de+=2*spins[s1][s2]*spins[t1][t2]

	
	
	evaluate=True
	t1=s1
	t2=s2-1
	if(t2==-1):
		if(PERIODICBOUNDARIES):
			t2=N-1
		else:
			evaluate=False
			
	if evaluate:
		de+=2*spins[s1][s2]*spins[t1][t2]
		
	de=de*J;
	
	if spins[s1][s2]>0:
		de+=2*b
	else:
		de-=2*b
	
	return de

#this flips the spin and checks for the change in all of its neighbors.  