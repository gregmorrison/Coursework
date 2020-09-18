import numpy as np
import math
import matplotlib as mp
import matplotlib.pyplot as plt

def difference(dt):
	e=9*math.exp(-2)
	f=1/(1+e)
	der=e*f*f
	fnew=1/(1+9*math.exp(-2-dt))
	return abs(der-(fnew-f)/dt)


xvals=[0]*21
yvals=[0]*21
for iter in range(21):
	dt=10**(-iter);
	xvals[iter]=dt;
	yvals[iter]=difference(dt);


# for your solutions, you can export data and plot it in matlab if you want.  
# this gives a sense of hwo to do it it python.

plt.scatter(xvals,yvals,color='k')
ax=plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
plt.title('python error')
plt.xlabel('dt')
plt.ylabel('difference')

plt.loglog(xvals,yvals,color='k')
plt.savefig('python.eps',format='eps')

plt.clf()


# plot the results of the c++ data too, which are stored in a text file
data=np.genfromtxt('c_problem1.txt',delimiter=',')

plt.scatter(xvals,yvals,color='m',marker=6)
ax=plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
plt.title('c++ error')
plt.xlabel('dt')
plt.ylabel('difference')

plt.loglog(xvals,yvals,color='m')
plt.savefig('cpp.eps',format='eps')

plt.clf()



