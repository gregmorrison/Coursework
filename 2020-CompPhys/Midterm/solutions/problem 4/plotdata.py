import numpy as np;
import matplotlib.pyplot as plt

mdata=np.genfromtxt('matlab_times.txt',delimiter=',');
pdata=np.genfromtxt('python_times.txt',delimiter=',');
cdata=np.genfromtxt('cpp_times.txt',delimiter=',');

nlist=mdata[:,0];
mlist=mdata[:,2];
plist=pdata[:,1];
clist=cdata[:,1];

scale3=np.power(nlist,3)/1e9;
scale4=np.power(nlist,4)/1e10;

fig=plt.figure();
ax=plt.gca();
ax.scatter(nlist,mlist,c='b',label='matlab')
ax.scatter(nlist,plist,c='r',label='python')
ax.scatter(nlist,clist,c='k',label='c++')
ax.plot(nlist,scale3,c='k',linestyle='dashed',label='N^3 scaling');
ax.plot(nlist,scale4,c='k',label='N^4 scaling');
ax.set_xscale('log');
ax.set_yscale('log');
ax.legend(loc='upper left')
ax.set_xlabel('N');
ax.set_ylabel('time (s)');
plt.show();