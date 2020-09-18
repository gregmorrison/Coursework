#include <iostream>
#include <cmath>


int main(){
	std::cout<<"integer test:  \n";
	int x=1;
	for(int iter=0;iter<32;iter++){
		x=x*2;
		if(iter>28){
			std::cout<<"2^"<<iter<<" = "<<x<<"\n";
		}
	}
	//becomes negative, then zero.
	
	std::cout<<"double test \n";
	double y=1.0;
	for(int iter=0;iter<1025;iter++){
		y=y*2.0;
		if(iter>1021){
			std::cout<<"2^"<<iter+1<<" = "<<y<<"\n";
		}
	}
	//returns inf.

	
	return 0;
}
