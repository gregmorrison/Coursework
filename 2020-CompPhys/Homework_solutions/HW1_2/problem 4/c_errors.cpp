#include <iostream>  //needed to print to the screen

double squared(double x);  //declare the function to compute a square

#define N 10 //size of the array

int main(){
	
	double matrix[10][10]={0}; //create an array
	
	for(int i=0;i<N;i++){  //loop over i
		for(int j=0;j<N;j++){  //loop over j
		//		for(int j=0;j<N;i++){  //loop over j
			//ERROR:  THERE WAS A COPY/PASTE ERROR.  I DIDN'T EDIT ALL OF THE i-->j
			double value=((double)(abs(i-j)));  //compute |i-j|
			matrix[i][j]=squared(value);  // plug |i-j| into the matrix
		}
	}
	
	for(int i=0;i<N;i++){  //loop over i
		for(int j=0;j<N;j++){  //loop over j
			std::cout<<matrix[i][j]<<" ";  //print the matrix to the terminal
		}
		std::cout<<"\n";//print a new line
	}
	return 0;
}

//double squared(int x){  //define the function to compute a square
//ERROR:  THIS SHOULD BE A double x, NOT AN int x.
double squared(double x){  //define the function to compute a square
	return x*x;  //compute x^2 and return it
}
