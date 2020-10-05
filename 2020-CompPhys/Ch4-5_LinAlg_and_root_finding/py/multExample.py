import numpy as np
import time

n=200

A=np.random.rand(n,n)
B=np.random.rand(n,n)
C=np.zeros((n,n))


t0=time.time();
for i in range(n):
	for j in range(n):
		for k in range(n):
			C[i,j]=C[i,j]+A[i,k]*B[k,j]
print("took "+str(time.time()-t0)+" s")


t0=time.time();
C=np.matmul(A,B)
print("took "+str(time.time()-t0)+" s")


