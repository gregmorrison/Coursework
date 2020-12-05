#include <fstream>
#include <iostream>
#include <random>
#include <math.h>

using namespace std;

mt19937 rgen (2);
//initialize the generator
normal_distribution<double> gran (0.0,1.0);
//normal distribution with 0 mean and 1 variance.

//to get a uniform number between 0 and 1, use uran(rgen);
//to get a normally distributed number, use gran(rgen)


#define kT 1				//room temperature, kT in pN nm
#define zeta 1		  		//friction coefficient in pN us / nm.
//this is an approx value for a 1um sphere
//in water.
#define m 1				//mass in pg of a polystyrene bead of radius 1um.

#define dt 0.01				//timestep in us.   This should be chosen to be
//"small enough" as in the brownian case, but now
//there is a requirement that zeta*dt/m is
// "small enough".


#define nrun 1000
#define nstep 1000  		//number of timesteps to simulate
#define n 2
#define dim 3

void externalForces(vector<vector<double> > & x,vector<vector<double> > & f,double k);
void internalForces(vector<vector<double> > & x,vector<vector<double> > & f,double k);

int main(){
	vector<double> tmp(dim,0);
	vector<vector<double> > x(n,tmp);
	vector<vector<double> > xold(n,tmp);
	vector<vector<double> > xnew(n,tmp);
	
	vector<vector<double> > R(n,tmp);
	vector<vector<double> > f(n,tmp);
	vector<vector<double> > v(n,tmp);

	
	
	
	double k1=.1;
	double k2=1;
	
	ofstream outfile,outfile2,outfile3;
	outfile.open("cpp_R.txt");
	outfile2.open("cpp_sep.txt");
	outfile3.open("cpp_vsq.txt");
	for(int run=0;run<nrun;run++){
		outfile<<run;
		outfile2<<run;
		outfile3<<run;
		
		for(int j=0;j<n;j++){
			for(int k=0;k<dim;k++){
				x[j][k]=0;
				xold[j][k]=0;
				xnew[j][k]=0;
			}
		}
		x[0][0]=-.5;
		xold[0][0]=-.5;
		x[1][0]=.5;
		xold[1][0]=.5;
		
		for(int i=0;i<nstep;i++){
			
			for(int j=0;j<n;j++){
				for(int k=0;k<dim;k++){
					f[j][k]=0;
				}
			}
			externalForces(x,f,k1);
			internalForces(x,f,k2);
			for(int j=0;j<n;j++){
				for(int k=0;k<dim;k++){
					R[j][k]=gran(rgen)*sqrt(2*zeta*kT/dt);
					//random forces
				}
			}
			//compute a random number with gaussian distribution.
			//The factor sqrt(2*\zeta*kT/dt) shifts the random number to have the
			//correct variance.
			
			
			for(int j=0;j<n;j++){
				for(int k=0;k<dim;k++){
					xnew[j][k]=x[j][k];
					xnew[j][k]+=(x[j][k]-xold[j][k])*(1-zeta*dt/2/m)/(1+zeta*dt/2/m);
					xnew[j][k]+=(f[j][k]+R[j][k])*dt*dt/m/(1+zeta*dt/2/m);
				}
			}
			//update the position
			for(int j=0;j<n;j++){
				for(int k=0;k<dim;k++){
					v[j][k]=(xnew[j][k]-xold[j][k])/2/dt;
					xold[j][k]=x[j][k];		//update the old location
					x[j][k]=xnew[j][k];		//update the current location
				}
			}
			
			double avxsq=0;
			double avdist=0;
			double vsq=0;
			for(int k=0;k<dim;k++){
				avxsq+=(x[0][k]+x[1][k])*(x[0][k]+x[1][k])/4;
				avdist+=(x[0][k]-x[1][k])*(x[0][k]-x[1][k]);
				vsq+=v[0][k]*v[0][k];
			}
			outfile<<","<<avxsq;
			//print mean squared position
			outfile2<<","<<avdist;
			outfile3<<","<<vsq;
		}
		
		outfile<<"\n";
		outfile2<<"\n";
		outfile3<<"\n";
	}
	
	outfile.close();
	outfile2.close();
	
	
	return 0;
}

void externalForces(vector<vector<double> > & x,vector<vector<double> > & f,double k){
	
	for(int i=0;i<x.size();i++){
		for(int j=0;j<x[i].size();j++){
			f[i][j]=-k*x[i][j];
		}
	}
	
}

void internalForces(vector<vector<double> > & x,vector<vector<double> > & f,double k){
	if(x.size()<2){
		std::cout<<" check your vector sizes!  your program will probably crash now."<<std::endl;
	}
	for(int i=0;i<x.size();i++){
		for(int i2=i+1;i2<x.size()-1;i2++){
			double dist=0;
			for(int j=0;j<x[i].size();j++){
				dist+=(x[i][j]-x[i][j])*(x[i][j]-x[i][j]);
			}
			dist=sqrt(dist);
			for(int j=0;j<x[i].size();j++){
				f[i][j]+=2*k*(1-1/dist)*(x[i][j]-x[i2][j]);
				f[i][j]-=2*k*(1-1/dist)*(x[i][j]-x[i2][j]);
			}
		}
	}
	
}
