#  schro - Program to solve the Schrodinger equation 
#  for a free particle using the Crank-Nicolson scheme

# Set up configuration options and special features
import numpy as np
import matplotlib.pyplot as plt


N=200;
L=1;
C=1;
T=10;
dx=L/(N-1);
dt=.001;


def CNneutron(D):
	A = np.zeros((N,N))     # Set all elements to zero
	coeff=D*dt/dx/dx;       #this is the factor in front of the 


	A[0,0]=-2*coeff+C*dt;
	A[0,1]=2*coeff;  			#for rho_0^n, there are two contributions from rho_1^n, one real and one virtual
	for i in range(1,N-1) :
		A[i,i-1] = coeff
		A[i,i] = -2*coeff +C*dt  
		A[i,i+1] = coeff
	A[N-1][N-1]=-2*coeff+C*dt;
	A[N-1][N-2]=2*coeff;  		#two contributions

	#* Compute the Crank-Nicolson matrix
	dCN = np.dot( np.linalg.inv(np.identity(N) - A/2),(np.identity(N) + A/2) )

	#initialize density at the middle
	rho = np.zeros(N,dtype=float)
	rho[int(N/2)]=N
	
	#rho=np.ones(N,dtype=float);

	max_iter = int(T/dt)
	#* Loop over desired number of steps (wave circles system once)
	for iter in range(max_iter) :
		rho = np.dot(dCN,rho) 
	return rho

D=.001;
r1=CNneutron(D);
D=.01;
r2=CNneutron(D);
D=.1;
r3=CNneutron(D);










x=np.asarray(range(N))*dx

plt.plot(x,r1,'b')
plt.plot(x,r2,'r')
plt.plot(x,r3,'k')
plt.ylim(0,1.1*max([max(r1),max(r2),max(r3)]))
plt.show()