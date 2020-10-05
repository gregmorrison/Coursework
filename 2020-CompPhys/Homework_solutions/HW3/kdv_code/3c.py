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
	#kdv is third order equation, with u'''[z]==c*u'[z]-6u[z]u'[z]
	# X = [u,u',u'']
	# the function should return [X[1],X[2],c*X[1]-6*X[0]*X[1]
	return np.array([X[1],X[2],params[0]*X[1]-6*X[0]*X[1]])  
	
def sech(x):
	return 	2/(np.exp(x)+np.exp(-x))						
def exact(x):
	return sech(x/2)*sech(x/2)/2

Zmax=5
c=1
params=[c]

X=np.array([0,0,0],dtype='float')

x0=1/2
xp0=0
xpp0=-1/4





dz=0.1
niter=Zmax/dz
#these are the parameters for our integrator


X=np.array([0.0,0.0,0.0],dtype=float)  #where we will store the data at each timestep for euler / rk4
sampleTimes=np.asarray(range(int(niter)+1))*dz
functionVals=np.asarray(c/2.0*sech(np.sqrt(c)*sampleTimes/2.0)**2)
result=np.asarray([x0])		#where we will store the data for plotting




	
	
	
	
X[0]=x0
X[1]=xp0
X[2]=xpp0
z=0
for titer in range(int(niter)):
	X=rk4(X,z,dz,deriv,[])
	result=np.append(result,[X[0]])  #store the value of theta we saw
	z=z+dz

	
	

plt.scatter(sampleTimes,result,label='numeric')
plt.plot(sampleTimes,exact(sampleTimes),label='exact')
plt.xlabel('z')
plt.ylabel('w(z)')
plt.title('3c')
plt.legend()
plt.savefig('3c.eps',format='eps')
