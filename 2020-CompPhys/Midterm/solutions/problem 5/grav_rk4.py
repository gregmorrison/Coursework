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


dt=0.002
niter=T/dt
#these are the parameters for our integrator

#X0=[0,1,1,0,0,0,0,0,0,-1,-1,0];
X0=[0,1,1,0,0.1,0,0,0,0,-1,-1,0];
X=np.array(X0,dtype=float)
E=energies(X);


sampleTimes=np.asarray(range(int(niter)+1))*dt
x1=np.asarray(X[0])		#where we will store the data for plotting
x2=np.asarray(X[4])		
x3=np.asarray(X[8])		
y1=np.asarray(X[2])		
y2=np.asarray(X[6])		
y3=np.asarray(X[10])
tvals=np.asarray([t])		
KE=np.asarray([E[0]])
PE=np.asarray([E[1]])


		
	
	
	
	
t=0
for titer in range(int(niter)):
	X=rk4(X,t,dt,deriv,[])
	t=t+dt
	E=energies(X);
	x1=np.append(x1,[X[0]])  #update our list of positions
	x2=np.append(x2,[X[4]])  
	x3=np.append(x3,[X[8]])  
	y1=np.append(y1,[X[2]])  
	y2=np.append(y2,[X[6]])  
	y3=np.append(y3,[X[10]])  
	KE=np.append(KE,[E[0]])  
	PE=np.append(PE,[E[1]])  #store the value of energies we saw
	tvals=np.append(tvals,[t])
	

np.savetxt("x.txt",x1,delimiter=',');
np.savetxt("y.txt",y1,delimiter=',');



	
plt.plot(x1,y1,color='r',label='star 2')
plt.plot(x2,y2,color='b',label='star 1')
plt.plot(x3,y3,color='k',label='star 3')
plt.xlabel('x_i');
plt.ylabel('y_i');
plt.legend()
plt.show()	

Etot=KE+PE;
plt.plot(sampleTimes,KE);
plt.plot(sampleTimes,PE);
plt.plot(sampleTimes,Etot);
plt.show()