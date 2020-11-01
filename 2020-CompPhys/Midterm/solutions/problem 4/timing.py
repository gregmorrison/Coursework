import numpy as np
import time

nlist=np.asarray([10,20,50,100,200,500,1000,2000]);
klist=np.asarray([53,99,231,444,862,2084,4077,7994]);
tlist=np.zeros([len(nlist),2]);
for niter in range(len(nlist)):
	n=nlist[niter]
	A=(np.ones(n,n)+np.eye(n))/(n+1);
	B=np.eye(n)-A;
	Bpow=np.eye(n);
	logA=np.zeros([n,n]);
	
	k=1;
	t0=time.time();
	while k<klist[niter]:
		Bpow=Bpow.dot(B);
		logA-=Bpow/k;
		k+=1;
	tf=time.time();
	tlist[niter,0]=n;
	tlist[niter,1]=tf-t0;
	if(niter==1):
		np.savetxt('log_A_10_python.txt',logA,delimiter=',');
np.savetxt('python_times.txt',tlist,delimiter=',')
print(tlist);
print(logA)