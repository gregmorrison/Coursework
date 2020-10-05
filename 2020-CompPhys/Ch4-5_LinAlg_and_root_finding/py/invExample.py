import numpy as np
import time

n=5

A=np.random.rand(n,n)
y=np.random.rand(n,1)

t0=time.time();
Ainv=np.linalg.inv(A)
x=Ainv.dot(y)
print("took "+str(time.time()-t0)+" s")

t0=time.time()
z=np.linalg.solve(A,y)
print("took "+str(time.time()-t0)+" s")

print(max(abs(x-z)))

print(A.dot(Ainv))