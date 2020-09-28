#include "NumMeth.h"
#include <vector>
#include <fstream>


extern void rk4(double x[], int nX, double t, double tau,
				void (*derivsRK)(double x[], double t, double param[], double deriv[]),
				double param[]);
//for reasons I cannot understand, Garcia has chosen to index his functions
//starting at i=1.  x[0] is not updated using is rk4 function, so our vectors will have
//the first element as a null value.  I will keep that notation in this script.
//it is possible he intended the first element to be the time, but this is not
//clear in his function definition.





void F(double x[],double t,double param[],double deriv[]){
	deriv[1]=x[2];
	deriv[2]=-x[1];
}
//the actual function for the pendulum

double pi=2*asin(1);
//pick a value of pi.  This is typo free...
//github example in class.


int main(){
	

	
	double x=0.0;
	double v=1.0;
	double t=0;
	double T=5;
	//physical parameters
	
	
	double dtList[]={0.5,0.1,0.05,0.01,0.005,0.001};//specified values of dt
	int numdt=6;  //number of specified values

	int dim=2;
	double* param= new double[dim+1];
	double* X=new double[dim+1];
	double* deriv=new double[dim+1];
	//memory allocation

	
	std::ofstream outRK("RK_error.txt");
	std::ofstream outVerlet("Verlet_error.txt");
	

	for(int i=0;i<numdt;i++){  //here we're looping over the timestep dt
		double dt=dtList[i];
		int nstep=((int)(T/dt));
		//integrator parameters
		
		X[1]=x;
		X[2]=v;
		t=0;
		for(int i=0;i<nstep;i++){
			rk4(X,dim,t,dt,F,param);
			t+=dt;
		}
		outRK<<dt<<","<<fabs(sin(t)-X[1])<<"\n";

		
		X[1]=x+v*dt-dt*dt*x/2;
		X[2]=x;
		t=dt;  //we've approximately integrated one  step
		for(int i=0;i<nstep-1;i++){
			double xcurr=X[1];
			X[1]=2*X[1]-X[2]+dt*dt*(-X[1]);
			X[2]=xcurr;
			t+=dt;
		}
		outVerlet<<dt<<","<<fabs(sin(t)-X[1])<<"\n";
	}
	
	outRK.close();
	outVerlet.close();

	
	
	
	
	
	
	
	
	
	
	return 0;
}


