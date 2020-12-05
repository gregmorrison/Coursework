#include "header.h"

double get_init_energy(double spins[N][N],double J,double b);
//compute the energy once
double energy_difference(int s1,int s2,double spins[N][N],double J,double b);
//energy differences are much faster to compute


double get_init_energy(double spins[N][N],double J,double b){
	double e=0;
	//the boundaries make this somewhat complicated, so we compute bulk
	//and boundaries separately.
	//we only add terms below or to the right.  This avoids doublecounting.

	for(int i=0;i<N-1;i++){
		for(int j=0;j<N-1;j++){
			e-=spins[i][j]*spins[i+1][j];
			e-=spins[i][j]*spins[i][j+1];
		}
	}
	//we have computed the contribution except for the rightmost and
	//bottommost boundary.

	
	for(int j=0;j<N-1;j++){
		e-=spins[N-1][j]*spins[N-1][j+1];
#ifdef PERIODIC_BOUNDARIES
		e-=spins[N-1][j]*spins[0][j];
#endif
	}

#ifdef PERIODIC_BOUNDARIES
	e-=spins[N-1][N-1]*spins[0][N-1];
	e-=spins[N-1][N-1]*spins[N-1][0];
#endif


	
	//we have computed the rightmost boundary now.  All that is left is the bottom.
	for(int i=0;i<N-1;i++){
		e-=spins[i][N-1]*spins[i+1][N-1];
#ifdef PERIODIC_BOUNDARIES
		e-=spins[i][N-1]*spins[i][0];
#endif
	}
	

	//we've computed all of the contributions from the ising interaction.
	e=J*e;
	//scale by J.
	

	double emag=0;
	//we still need the magnetic interaction.  This does not depend on the boundary .
	
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(spins[i][j]>0){
				emag-=1;
			}
			else{
				emag+=1;
			}
		}
	}
	emag=b*emag;
	
	
	return (e+emag);
}






double energy_difference(int s1,int s2,double spins[N][N],double J,double b){
	
	double de=0;
	bool evaluate;
	int t1,t2;
	
	evaluate=true;
	//check whether this link iexists.
	t1=s1-1;
	t2=s2;
	//look to the left
	if(t1==-1){
		//if that is -1, we have to wrap around
#ifdef PERIODIC_BOUNDARIES
		t1=N-1;
		//if we have PBC's , do so
#else
		evaluate=false;
		//if we don't, don't include this term in the energy
#endif
	}
	if(evaluate){
		de+=2*spins[s1][s2]*spins[t1][t2];
		//if the link exists, we subtract (not add!) the equivalent energy twice:
		//we are replacing an up with a down (or down with an up), so it's twice as strong
		// note that in the above energy def, we had a -=.  here, we have a +=.
		// sign errors are easy, because the Hamiltonian has an - sign that is easily
		// forgotten.
	}
//the rest of these terms below are the same, but deal with the other three options.
	
	
	evaluate=true;
	t1=s1+1;
	t2=s2;
	if(t1==N){
#ifdef PERIODIC_BOUNDARIES
		t1=0;
#else
		evaluate=false;
#endif
	}
	if(evaluate){
		de+=2*spins[s1][s2]*spins[t1][t2];
	}
	
	
	evaluate=true;
	t1=s1;
	t2=s2-1;
	if(t2==-1){
#ifdef PERIODIC_BOUNDARIES
		t2=N-1;
#else
		evaluate=false;
#endif
	}
	if(evaluate){
		de+=2*spins[s1][s2]*spins[t1][t2];
	}
	
	
	evaluate=true;
	t1=s1;
	t2=s2+1;
	if(t2==N){
#ifdef PERIODIC_BOUNDARIES
		t2=0;
#else
		evaluate=false;
#endif
	}
	if(evaluate){
		de+=2*spins[s1][s2]*spins[t1][t2];
	}
	
	de=de*J;
	
	
	
	//if the spin was aligned with the field initially, we need to flip it.
	//that INCREASES the energy by 2h

	if(spins[s1][s2]>0){
		de+=2*b;
	}
	else{
		de-=2*b;
	}
	//otherwise it decreases the energy by 2h.
	
	return de;
}





