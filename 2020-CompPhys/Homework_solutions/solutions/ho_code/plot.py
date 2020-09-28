import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

# plot the results of the c++ data too, which are stored in a text file
data=np.genfromtxt('RK_error.txt',delimiter=',')
xvals=data[:,0]
yvals=data[:,1]
plt.scatter(xvals,yvals,color='b',marker=6,label='RK4')
data=np.genfromtxt('verlet_error.txt',delimiter=',')
xvals=data[:,0]
yvals=data[:,1]
plt.scatter(xvals,yvals,color='r',marker=7,label='verlet')

plt.plot(xvals,xvals**2,color='r')

ax=plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
plt.title('RK vs verlet errors ')
plt.xlabel('dt')
plt.ylabel('x(T)')

plt.savefig('accuracy.eps',format='eps')

plt.clf()
