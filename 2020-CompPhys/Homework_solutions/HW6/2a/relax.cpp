
#include "NumMeth.h"
using namespace std;
int main() {
	
	//* Initialize parameters (system size, grid spacing, etc.)
	int N=100;
	double L = 1;          // System size (length)
	double h = L/(((double)(N))-1);    // Grid spacing
	Matrix x(N), y(N);
	int i,j;
	for( i=1; i<=N; i++ )
	x(i) = (i-1)*h;  // x coordinate
	y = x;             // y coordinate
	
	
	//* Set initial guess as first term in separation of variables soln.
	Matrix phi(N,N);
	Matrix f(N,N);
	for( i=1; i<=N; i++ ){
		for( j=1; j<=N; j++ ){
			phi(i,j) = 1;
		}
	}
	
	int cut=int((double(N)/2.0));
	
	//* Set boundary conditions
	for(i=1;i<=N;i++){
		phi(i,1)=1;  //bottom wall
		phi(i,N)=0;	 //top wall
	}
	for(j=1;j<=N;j++){
		phi(1,j)=0.0;	//left wall
		phi(N,j)=0.0;  //right wall
	}
	for(i=1;i<=cut;i++){
		for(j=cut;j<=N;j++){
			phi(i,j)=0; 	//set the rest to 0.  Unnecessary, but makes plotting easier.
		}
	}

	for( i=1; i<=N; i++ ){
		for( j=1; j<=N; j++ ){
			f(i,j) = phi(i,j);
		}
	}


	
	
	
	//* Loop until desired fractional change per iteration is obtained
	double phiTemp;         // Temporary value used by GS and SOR
	int iterMax = N*N;            // Set max to avoid excessively long runs
	double changeDesired = 1e-4;  // Stop when the change is given fraction
	Matrix change(iterMax); // Record fractional change at each iteration
	int iter, nIter;        // Iterations counters
	for( iter=1; iter<=iterMax; iter++ ) {
		
		double changeSum = 0;
		for( i=2; i<=(N-1); i++ ){  // loop over entire x axis
			for( j=2; j<=cut-1; j++ ) {  //loop over bottom half of the y axis
				phiTemp = 0.25*(phi(i+1,j)+phi(i-1,j)+phi(i,j-1)+phi(i,j+1)); 	//relaxation.  Overrelax is fine too
				changeSum += fabs(1-phi(i,j)/phiTemp);
				f(i,j) = phiTemp;
			}
		}
		for( i=cut+1; i<=(N-1); i++ ){  // Loop right half of x axis
			for( j=cut; j<=N-1; j++ ) {  //loop over top half of the y axis
				phiTemp = 0.25*(phi(i+1,j)+phi(i-1,j)+phi(i,j-1)+phi(i,j+1)); 	//relaxation.  Overrelax is fine too
				changeSum += fabs(1-phi(i,j)/phiTemp);
				f(i,j) = phiTemp;
			}
		}
		for( i=1; i<=N; i++ ){
			for( j=1; j<=N; j++ ){
				phi(i,j) = f(i,j);
			}
		}
		

		change(iter) = changeSum/((N-2)*(N-2));
		if( change(iter) < changeDesired ) {
			cout << "Desired accuracy achieved after " << iter
			<< " iterations" << endl;
			cout << "Breaking out of main loop" << endl;
			nIter = iter;
			iter=iterMax;
			break;	    // Break out of the main loop
		}
	}
	
	
	//* Print out the plotting variables: x, y, phi, change
	ofstream xOut("x.txt"), yOut("y.txt"),phiOut("phi.txt");
	for( i=1; i<=N; i++ ) {
		xOut << x(i) << endl;
		yOut << y(i) << endl;
		for( j=1; j<N; j++ ){
			phiOut << phi(i,j) << ", ";
		}
		phiOut << phi(i,N) << endl;
	}
	
	
	return 0;
}

