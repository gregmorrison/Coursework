import numpy as np

N=7;

M=np.zeros((N,N));
for i in range(N):
	for j in range(N):
		if(np.abs(i-j)<3):
			M[i,j]=1
b=np.ones(N);
v,w=np.linalg.eig(M)
#numpy orders the eivenvalues from smallest to largest, so we can just pick the first element.  
#however, you can search for the largest element if you want!  



lambda_max=max(abs(v))
maxIndex=(np.where(v==lambda_max))[0]; #this is the list of the indices with max eigenvalue.  
vmax=np.array([w[:,i] for i in maxIndex])
if((vmax.shape)[0]==1):
	vmax=vmax[0]
else:
	print("multiple eigenvectors with the same eigenvalue.  Power method will not work!")
	
# for our example, the eigenvalues are distinct so this is a list of one vector only.  
# if two eigenvectors share an eigenvalue, we won't find M^nb=v_max (since it will be some 
# linear combination of those two eigenvectors.  )





tol=1e-6
while True:  #this while loop will run forever
	bold=b

	mag=np.sqrt(b.dot(b))
	magold=mag;
	b=M.dot(b)/mag

	bold=bold-b   #b_{k-1}-b_{k}
	mag=np.sqrt(bold.dot(bold))  #|b_{k-1}-b_{k}|
	
	if(mag/magold<tol):  #this condition halts the infinite loop.
		break

b=b/np.sqrt(b.dot(b));
c=vmax/(np.sqrt(vmax.dot(vmax)))
if c[0]*b[0]<0:
	c=-c;
	
print("")
	
print("max value of b-c (in absolute value):")
print(max(abs(b-c)))
print("")

print("max value of lambda b-c (in absolute value):")
print(max(abs(lambda_max*b-M.dot(b))))
print("")
