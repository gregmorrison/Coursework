import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)		
from collections import Counter

n=100000
dx=.1
vals=-np.log(np.random.random_sample(n));
dist=Counter(dx*(vals/dx//1))
dist=np.array(list(dist.items()))
dist[:,1]/=(n*dx)

plt.scatter(range(0,n),vals)
plt.show()

plt.scatter(dist[:,0],dist[:,1],marker='o')
plt.scatter(dist[:,0],np.exp(-dist[:,0]),marker='*')
plt.show()

plt.scatter(dist[:,0],dist[:,1],marker='o')
plt.scatter(dist[:,0],np.exp(-dist[:,0]),marker='*')
plt.yscale('log')
plt.show()