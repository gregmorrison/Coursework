import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt


def logistic_calculate(r,x):
	return r*x*(1-x)  
	#this returns the new value of x from the logisitic map


# PARAMETERS
max_iterations=50  # how many iterations to do



r=2;
x=0.01    # initial value for x

yaxes=[0]*max_iterations
xaxes=[0]*max_iterations
#here we'll be storing data.  
for iter in range(max_iterations):  
	yaxes[iter]=x
	#here, we are storing the data in a list, rather than printing to a file.
	# it is ok to print to a file if that is your preference
	xaxes[iter]=iter
	# this stores the values for the x axis (which is just the iteration number)
	x=logistic_calculate(r,x)
		
plt.scatter(xaxes,yaxes,facecolors='none',edgecolors='k',label='r = '+str(r))
#this draws the points
#facecolors='none' means an empty symbol.
# color 'k' is black 
# label is for a plot legend (not required in the rpbolem).  
plt.plot(xaxes,yaxes,color='k')
#this draws the lines

	
	
r=2.99;
x=0.01    
yaxes=[0]*max_iterations
xaxes=[0]*max_iterations
for iter in range(max_iterations):  
	yaxes[iter]=x
	xaxes[iter]=iter
	x=logistic_calculate(r,x)
plt.scatter(xaxes,yaxes,marker='o',color='r',label='r = '+str(r))	
plt.plot(xaxes,yaxes,color='r')
#same as above, but red instead of black, and with big circles.  


plt.xlabel('n')
plt.ylabel('r')
#label your axes!  
plt.legend(loc="lower right")
#legend was not required, but this is how to do it.

plt.savefig('logistic_dynamics.png')
plt.show();