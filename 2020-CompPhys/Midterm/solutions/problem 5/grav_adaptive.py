import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy import integrate


import sys
sys.path.append('./NM4P/Python/nm4p/')  #this is required to import a module from outside of the current directory.
										# you may need to change this to have the code run on your computer!
										
from rk4 import rk4						#this imports rk4 from Garcia's github.  Note the file name 
										# is rk4 (the first "rk4" here), and we import the "rk4" function
										# (the second "rk4")
										
								
										
def deriv(t,X):
	npart=int(len(X)/4);
	Y=np.zeros(len(X))
	for i in range(len(X)):
		if(i%2==0):
			Y[i]=X[i+1];  # dx_i/dt = v_i 
	for i in range(npart):  # is is the particle index we're computing
		x=X[4*i];
		y=X[4*i+2];
		for j in range(npart):  #j is the particle index we're computing force from
			xx=X[4*j];
			yy=X[4*j+2];
			if(i!=j):  #ignoring self forces, we need to compute -r/r^3
				sep=(x-xx)**2+(y-yy)**2;
				sep=np.sqrt(sep);  #this is |r_i-r_j|
				sep=sep**3;  #this is |r_i-r_j|^3
				Y[4*i+1]-=(x-xx)/sep;
				Y[4*i+3]-=(y-yy)/sep;  #force updates
	return Y				
										


def energies(X):
	k=0;
	p=0;
	npart=int(len(X)/4);
	for i in range(npart):
		k=k+X[4*i+1]**2/2+X[4*i+3]**2/2;  #ke = \sum_i v_i^2/2
		for j in range(i+1,npart):
			sep=(X[4*i]-X[4*j])**2+(X[4*i+2]-X[4*j+2])**2;
			p=p-1/np.sqrt(sep);  # pe = \sum_{i>j} 1/|r_i-r_j|
	return [k,p];





t=0.0
T=100
#these are the parameters for our system


dt=0.02
niter=T/dt
#these are the parameters for our integrator

X0=[0,1,1,0,0,0,0,0,0,-1,-1,0];
X0=[0,1,1,0,0.01,0,0,0,0,-1,-1,0];
X=np.array(X0,dtype=float)


tlist=np.linspace(0, T, 10000);
soln=integrate.solve_ivp(deriv,[0,T],X0,method='RK45',atol=1e-6,t_eval=tlist);
		
plt.plot(soln.y[0],soln.y[2],'r')
plt.plot(soln.y[4],soln.y[6],'b')
plt.plot(soln.y[8],soln.y[10],'k')
plt.show()

	
	
