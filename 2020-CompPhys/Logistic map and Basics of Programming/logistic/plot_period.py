import numpy as np

import matplotlib as mp
import matplotlib.pyplot as plt


pdata=np.genfromtxt('periods.txt',delimiter=',')
## This uses numpy to import the data.

plt.scatter(pdata[:,0],pdata[:,1],color='b')
plt.plot(pdata[:,0],pdata[:,1],color='b')
ax=plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('r')
ax.set_ylabel('period')
ax.set_title('bifurcation period')

plt.show();
#show the plot
plt.savefig('period_python.eps', format='eps')
#save the figure.



plt.cla(); 
#this clears all data in the previous plot.  




