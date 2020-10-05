#include "NumMeth.h"
#include <random>
#include <chrono>
std::mt19937 rgen(1);
std::uniform_real_distribution<double> uran(0,1);
extern double inv(Matrix A, Matrix& Ainv);

int main(){
	int n=500;
	
	Matrix A=Matrix(n,n);
	Matrix Ainv=Matrix(n,n);
	Matrix prod=Matrix(n,n);
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			A(i,j)=uran(rgen);   //plug in a random number
		}
	}
	
	auto start=std::chrono::steady_clock::now();  //this the start timer

	double det=inv(A,Ainv);
	
	
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			prod(i,j)=0;
			for(int k=1;k<=n;k++){
				prod(i,j)+=A(i,k)*Ainv(k,j);
			}
		}
	}
	
	/*
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			std::cout<<Ainv(i,j)<<" ";
		}
		std::cout<<"\n";
	}
	std::cout<<"\n";

	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			std::cout<<prod(i,j)<<" ";
		}
		std::cout<<"\n";
	}
	*/
	
	auto end=std::chrono::steady_clock::now();  //this the start timer
	auto timediff=std::chrono::duration_cast<std::chrono::microseconds>(end-start);
	std::cout<<"took "<<timediff.count()/1000000.0<<" s\n";

	
	return 0;
}
