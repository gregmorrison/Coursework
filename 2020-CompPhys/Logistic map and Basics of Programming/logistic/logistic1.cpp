#include <iostream>
#include <fstream>
#include <math.h>

double logistic_calculate(double r, double x);


int main(){
	
	
	//	DEFINE PARAMETERS FOR THE CALCULATION
	
	int max_iteration=10000;  //number of iteration
	int max_period=256; 	//how many values we'll print
	int start_testing=max_iteration-max_period;
	//the iteration where it is time to start printing.
	int numdiv=5000;  //the number of values of r we will print.
	double tolerance=1e-8;  // this is what we mean by a "small" difference.
	
	
	std::ofstream bfile("bifurcations.txt");  //bfile is the file we will print bifurcation data
	std::ofstream pfile("periods.txt");  //outfile is the file we will print period data
	
	
	
	/*  ITERATE OVER DIFFERENT VALUES OF r TO DETERMINE BIFURCATIONS */
	for(int riter=0;riter<numdiv;riter++){
		double r=1.0+3.0*((double)riter)/((double)numdiv);
		// r ranges from 1 to 4, with numdiv values chosen.
		
		
		//now that we have the parameters all chosen, we have to initalize our data.
		
		double x=0.001;  //initial value of x
		double xobs=0; //this is the stored value of x to see if there is a repeat.
		int period=max_period;  //this is the actual period for this system.
		
		for(int iter=0;iter<max_iteration;iter++){
			x=logistic_calculate(r,x);
			
			if(iter==start_testing){
				//if we've waited "long enough", we check for repeats
				xobs=x;
				//	xobs is the observed value of the sequence that we will check for.
				bfile<<r;  //store the value of r for this calculation
			}
			if(iter>start_testing){
				bfile<<","<<x;
				
				
				
				if((fabs(x-xobs)<tolerance) & (period==max_period)){
					//if we see a repeated value within our tolerance,
					period=iter-start_testing;
					//we store the period.
				}
			}
			
			
			
		}//end of the loop over iterations
		bfile<<"\n";
		pfile<<r<<","<<period<<"\n";
		
		
	}//end of loop over values of r.
	
	bfile.close();
	pfile.close();
	
	
	
	return 0;
}

double logistic_calculate(double r, double x){
	return r*x*(1-x);
}
