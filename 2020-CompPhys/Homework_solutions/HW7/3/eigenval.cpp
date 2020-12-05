#include "NumMeth.h"
using namespace std;
double param[]={0};

extern void rk4(double x[], int nX, double t, double tau,
				void (*derivsRK)(double x[], double t, double param[], double deriv[]),
				double param[]);

void DerivsFcn(double x[],double t,double param[],double deriv[]);
double boundary_value(double E,bool doPrint);





int main(){

	double dE=.01;
	double E=.01;
	
	double tol=1e-6;
	while(true){
		double b1=boundary_value(E,false);
		double b2=boundary_value(E+dE,false);
		cout<<b1<<","<<b2<<"\n";
		double der=(b2-b1)/dE;
		//std::cout<<E<<","<<b1<<","<<b2<<","<<der<<"\n";
		if(fabs(b1)<tol){
			break;
		}
		E-=b1/der;
	}
	std::cout<<"eigenvalue is "<<E<<"\n";
	double b1=boundary_value(E,true);  //print the function

	
	
	return 0;
}

double boundary_value(double E,bool doPrint){

	std::ofstream outfile;
	if(doPrint){
		outfile.open("x.txt");
	}
	double dt=.001;  //rk integration size
	double t=0;  //time
	int nstep=((int)(2*asin(1)/dt));  //number of steps to the boundary
	int nx=2;  //dimension of vector x
	double x[]={0,0,1};  //x (note x[0] is ignored in Garcia's code)
	double param[]={E};  //parameter passed to the function
	for(int iter=0;iter<nstep;iter++){
		rk4(x,nx,t,dt,&DerivsFcn,param);  //integration
		t+=dt;
		if(doPrint){
			outfile<<t<<","<<x[1]<<"\n";
		}
	}
	dt=2*asin(1)-t;
	rk4(x,nx,t,dt,&DerivsFcn,param);  //integration
	t+=dt;
	if(doPrint){
		outfile<<t<<","<<x[1]<<"\n";
	}

	if(doPrint){
		outfile.close();
	}
	
	return x[1];  //return the value of x after integration to the boundary.
}


void DerivsFcn(double x[],double t,double param[],double deriv[]){
	deriv[1]=x[2];
	if(x[1]<0){  //we want to choose the real root for the 1/3 power.  
		deriv[2]=param[0]*pow(fabs(x[1]),1/3.0);  // E=param[0]
	}
	else{
		deriv[2]=-param[0]*pow(fabs(x[1]),1/3.0);  // E=param[0]
	}
}
