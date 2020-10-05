import numpy as np
import time

n=2000

A=np.random.rand(n,n)
A=(A+np.transpose(A))/2
t0=time.time()
v,w=np.linalg.eig(A)
print("took "+str(time.time()-t0)+" s")

#print(A.dot(w[:,0])/v[0])
#print(w[:,0])