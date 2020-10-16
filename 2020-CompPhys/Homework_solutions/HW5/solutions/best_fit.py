import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

np.random.seed(4);

def exponFit(t,A,t1):
	return A*np.exp(-t/t1)
def biExponFit(t,A,B,t1,t2):
	return A*np.exp(-t/t1)+B*np.exp(-t/t2)


#x=np.linspace(0,100,100);

#y=.5*np.exp(-x/2)+.5*np.exp(-x/20)+np.random.normal(0,.01,x.size)
#np.savetxt("data_1.csv",np.transpose(np.array([x,y])),delimiter=",", fmt='%f')

#y=.5*np.exp(-x/2)+.5*np.exp(-x/20)+np.random.normal(0,.08,x.size)
#np.savetxt("data_2.csv",np.transpose(np.array([x,y])),delimiter=",", fmt='%f')

#y=.5*np.exp(-x/15)+np.random.normal(0,.08,x.size)
#np.savetxt("data_3.csv",np.transpose(np.array([x,y])),delimiter=",", fmt='%f')


dat=np.genfromtxt('data_3.csv',delimiter=',')
x=dat[:,0];
y=dat[:,1];



init_vals=[1,1]
#init_vals=[1,.1]
#init_vals=[1,10]

fits,cov=curve_fit(exponFit,x,y,p0=init_vals)
print("epxonential paramter fits were:")
print(fits)
print("mean squared error was:")
print(sum((y-exponFit(x,*fits))**2)/len(x))
print(" ");

plt.scatter(x,y)
plt.plot(x,exponFit(x,*fits))
plt.show()




init_vals=[1,1,1,1]
#init_vals=[1,1,1,.1]
#init_vals=[1,1,1,10]

fits,cov=curve_fit(biExponFit,x,y,p0=init_vals)
print("biexponential paramter fits were:")
print(fits)
print("mean squared error was:")
print(sum((y-biExponFit(x,*fits))**2)/len(x))
print(" ");

plt.scatter(x,y)
plt.plot(x,biExponFit(x,*fits))
plt.show()