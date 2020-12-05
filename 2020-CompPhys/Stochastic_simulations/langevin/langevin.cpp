#include <fstream>
#include <random>
#include <math.h>

using namespace std;

mt19937 rgen (2);
//initialize the generator
uniform_real_distribution<double> uran (0.0, 1.0);
//uniform distribution between 0 and 1
normal_distribution<double> gran (0.0,1.0);
//normal distribution with 0 mean and 1 variance.

//to get a uniform number between 0 and 1, use uran(rgen);
//to get a normally distributed number, use gran(rgen)


#define kT 4.1				//room temperature, kT in pN nm
#define zeta 20		  		//friction coefficient in pN us / nm.
							//this is an approx value for a 1um sphere
							//in water.
#define m 4.2				//mass in pg of a polystyrene bead of radius 1um.

#define dt 0.02				//timestep in us.   This should be chosen to be
							//"small enough" as in the brownian case, but now
							//there is a requirement that zeta*dt/m is
							// "small enough".



#define nstep 100000  		//number of timesteps to simulate


double externalForce(double x, double k);

int main(){
	
	double x=0;			//current position
	//here, we're starting initially at the origin, with v0=0.
	
	double xold=x;			//position at previous timestep
	double xnew=x;			//updated position

	
	double stiffness=0.5*2*zeta*kT;
	//double stiffness=2*zeta*kT;
	//double stiffness=8*zeta*kT;

	
	ofstream outfile;
	outfile.open("cpp_pos.txt");
	for(int i=0;i<nstep;i++){
		double f=externalForce(x,stiffness);
		//compute the external forces due to the current position
		double R=gran(rgen)*sqrt(2*zeta*kT/dt);
		//compute a random number with gaussian distribution.
		//The factor sqrt(2*\zeta*kT/dt) shifts the random number to have the
		//correct variance.
		
		xnew=x;  //start at position
		xnew+=(x-xold)*(1-zeta*dt/2/m)/(1+zeta*dt/2/m); //update location based on velocity
		xnew+=(f+R)*dt*dt/m/(1+zeta*dt/2/m);  //update location based on forces
		
		xold=x;		//update the old location
		x=xnew;		//update the current location
		
		outfile<<((double)(i+1))*dt<<","<<x<<"\n";
		//print mean squared position
	}
	outfile.close();
	
	
	return 0;
}

double externalForce(double x,double k){
	int center=((int)x);  //remove decimal part of x
	double xattr=((double)center)+1/2.0;
	//center is at integer part, +1/2.
	return -k*(x-xattr);
}
