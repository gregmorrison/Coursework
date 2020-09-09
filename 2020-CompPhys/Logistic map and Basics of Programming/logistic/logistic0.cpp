/*INCLUDES GO FIRST*/
#include <iostream>


/*FUNCTION DEFINITIONS HERE*/


double logistic_calculate(double r,double x){
	return r*x*(1-x);
	//this is the logistic map.  x is not modified.
}

void logistic_update(double r,double & x){
	//r is passed by value, but x is passed by reference.
	//x is modified by this function, but r cannot be modified.
	x=r*x*(1-x);
	//this is the logistic map.  The value of x is updated
}


void logistic_update_by_pointer(double r,double * x){
	//r is passed by value, but x is passed by pointer in the old c style.
	//the pointer is represented by a *, which makes the code tedious to look at:
	(*x)=r*(*x)*(1-(*x));
	//this is the logistic map, the value of x is updated.

}

/*FUNCTION DEFINITIONS FINISHED*/



int main(){
	
	
	//	DEFINE PARAMETERS FOR THE CALCULATION
	int max_iteration=10000;  //how many iterations to do
	int numprint=30;   //how many numbers to print to the screen
	double r=1.4;  //our choice for r.

	//	DEFINE INITIALIZATION FOR THE CALCULATION
	double x=0.001;  //our initial value.
	
	
	
	//	ITERATIVELY UPDATE THE VALUE OF x
	for(int iter=0;iter<max_iteration;iter++){
		
		/*	UPDATE THE VALUE OF x.  WE HAVE 3 POSSIBLE FUNCTIONS WE CAN USE */
		x=logistic_calculate(r,x);
		// x is not updated using logistic_calculate(r,x), so we have to change it by hand.
		
//		logistic_update(r,x);
		//this function updates the value of x, and we don't need to do anything more.
		
//		logistic_update_by_pointer(r,&x);
		//this function takes a reference to x as its argument in the older c style.
		
		/*	x HAS BEEN UPDATED NOW! */

		
		if(max_iteration-iter<numprint){
			std::cout<<x<<"\n";
			//print the data to the terminal once we've waited "long enough"
		}


	}//this is the end of the loop over iterations.
	
	
	
	
	
	
	return 0;
	//c++ code ends with "return 0;", unless you're being clever.
}


