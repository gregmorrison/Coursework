import matplotlib
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
T=10
div=10;
n=100000
dist=np.zeros((T-1)*div);
for iter in range(n):
	x=np.random.random();
	r=pow(T,x);
	k=int((r-1)*div)
	dist[k]+=div/n;

t=np.asarray(range((T-1)*div))
t=t/div+1;
plt.scatter(t,dist)
plt.plot(t,1/t/np.log(T))
plt.xlabel('x');
plt.ylabel('p(x)')
plt.show()