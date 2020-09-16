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



void euler(double x[], int nX, double t, double tau,
				void (*derivsRK)(double x[], double t, double param[], double deriv[]),
				double param[]){
	double* dX=new double[nX+1];
	(*derivsRK)(x,t,param,dX);
	x[1]+=tau*dX[1];
	x[2]+=tau*dX[2];
	delete [] dX;
}
//this uses the same indexing and functional form that Garcia uses, implementing euler.


void F(double x[],double t,double param[],double deriv[]){
	deriv[1]=x[2];
	deriv[2]=-sin(x[1]);
}
//the actual function for the pendulum

double pi=2*asin(1);
//pick a value of pi.  This is typo free...
//github example in class.


int main(){
	

	
	double theta=0.1*pi;
	double omega=0.0;
	double t=0;
	double T=30;
	double g=9.81;
	double L=1.0;
	double m=1.0;
	//physical parameters
	
	double dt=0.2;
	int nstep=((int)(T/dt));
	//integrator parameters
	
	int dim=2;
	double* param= new double[dim+1];
	double* X=new double[dim+1];
	double* deriv=new double[dim+1];
	//memory allocation

	
	X[1]=theta;
	X[2]=omega;
	t=0;
	std::ofstream outEuler("euler_cpp.txt");
	outEuler<<t<<","<<X[1]<<"\n";
	for(int i=0;i<nstep;i++){
		euler(X,dim,t,dt,F,param);
		t+=dt;
		outEuler<<t<<","<<X[1]<<"\n";
	}
	outEuler.close();
	
	
	
	X[1]=theta;
	X[2]=omega;
	t=0;
	std::ofstream outRK("RK_cpp.txt");
	outRK<<t<<","<<X[1]<<"\n";
	for(int i=0;i<nstep;i++){
		rk4(X,dim,t,dt,F,param);
		t+=dt;
		outRK<<t<<","<<X[1]<<"\n";
	}
	outRK.close();
	
	
	
	X[1]=theta+omega*dt+dt*dt*(-sin(theta));
	X[2]=theta;
	t=0;
	std::ofstream outVerlet("verlet_cpp.txt");
	outRK<<t<<","<<X[2]<<"\n";
	outRK<<t+dt<<","<<X[1]<<"\n";
	for(int i=0;i<nstep;i++){
		double xcurr=X[1];
		X[1]=2*X[1]-X[2]+dt*dt*(-sin(X[1]));
		X[2]=xcurr;
		t+=dt;
		outVerlet<<t<<","<<X[1]<<"\n";
	}
	outVerlet.close();
	
	
	return 0;
}


