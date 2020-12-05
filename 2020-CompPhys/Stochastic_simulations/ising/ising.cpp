#include "header.h"

#define nstep 100000
#define printstep 1000
#define nrun 100

bool metropolis(double e,double enew);



double J=.4;
double b=0;



int ranseed=10;
mt19937 rgen (ranseed);
//initialize the generator
uniform_real_distribution<double> uran (0.0, 1.0);
//uniform distribution between 0 and 1


//defined at the bottom of this file!
bool metropolis(double e,double enew);
extern double get_init_energy(double spins[N][N],double J,double b);
//compute the energy once
extern double energy_difference(int s1,int s2,double spins[N][N],double J,double b);
//energy differences are much faster to compute



int main(){
	
	double ave[nstep/printstep]={0};
	double avm[nstep/printstep]={0};
	int t[nstep/printstep]={0};
	
	for(int run=0;run<nrun;run++){
		double spins[N][N]={{0}};
		double m=0;
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				if(uran(rgen)<.5){		//with a 50% chance, flip the spin up
					spins[i][j]=1;
					m+=1;				//adjust the initial magnetization as well.
				}
				else{
					spins[i][j]=-1;
					m-=1;
				}
			}
		}
		//intially the spins are random
		double e=get_init_energy(spins,J,b);

		
		for(int step=0;step<nstep;step++){
			//flip one spin, randomly chosen
			int s1=((int)((N*uran(rgen))));
			int s2=((int)((N*uran(rgen))));
			double enew=e+energy_difference(s1,s2,spins,J,b);
			//get the new energy
			if(metropolis(e,enew)){
				//with metropolis, make the change
				spins[s1][s2]=-spins[s1][s2];//flip spin
				if(spins[s1][s2]>0){
					m+=2;  //count one spin flipped up
				}
				else{
					m-=2;  //count flipped down.
				}
				e=enew;
			}
			if(step%printstep==0){
				ave[step/printstep]+=e;
				avm[step/printstep]+=m;
				t[step/printstep]=step;
			}
		}
		
		cout<<"normalized energy:  "<<e/J/N/N/2<<"\n";
		cout<<"normalized magnetization:  "<<m/((double)(N*N))<<"\n";
		
		

		
	}
	
	ofstream outfile;
	outfile.open("mag_energy.txt");
	for(int i=0;i<nstep/printstep;i++){
		outfile<<t[i]<<","<<avm[i]/nrun<<","<<ave[i]/nrun<<"\n";
	}
	outfile.close();
	
	
	return 0;
}


bool metropolis(double e,double enew){
	if(e>enew){//if the new energy is lower accept
		return true;
	}
	else{
		if(uran(rgen)<exp(e-enew)){//if the new energy is higher, accept with boltzman factor
			return true;
		}
		else{
			return false;
		}
	}
	cout<<"something went wrong, we should never get to this line.  \n";
	return false;
}
