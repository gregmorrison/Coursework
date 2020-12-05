import matplotlib
import matplotlib.pyplot as plt
import numpy as np

dt=.01;

vdata=np.genfromtxt('cpp_vsq.txt', delimiter=',')
av=sum(vdata);
av=av/len(vdata)
plt.plot(np.asarray(range(1,len(av)))*dt,av[1:len(av)],'b')
plt.plot(np.asarray(range(1,len(av)))*dt,np.ones(len(av)-1)*3,'k')
plt.xlabel('t');
plt.ylabel('<v^2>')
plt.show()



m=1
zeta=1
k=.1
kT=1


t1=m/zeta;
t2=t1/np.sqrt(1-4*k*m/zeta/zeta)
t=np.asarray(range(1,len(av)))*dt



rsq=2*np.exp(-t/t1);
rsq+=t2/(t1-t2)*np.exp(-t/t1+t/t2);
rsq-=t2/(t1+t2)*np.exp(-t/t1-t/t2);
rsq-=2*t1*t1/(t1*t1-t2*t2);

rsq=3*t1*t2*t2*kT*zeta/m/m*rsq;

plt.plot(t,rsq);
rdata=np.genfromtxt('cpp_R.txt', delimiter=',')
av=sum(rdata);
av=av/len(rdata)
plt.plot(t,av[1:len(av)])
plt.xlabel('t')
plt.ylabel('<R^2>')
plt.show()
