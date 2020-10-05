#include "NumMeth.h"
#include <random>
#include <chrono>
std::mt19937 rgen(1);
std::uniform_real_distribution<double> uran(0,1);

int main(){
	
	int n=1000;
	
	Matrix A=Matrix(n,n);
	Matrix B=Matrix(n,n);
	Matrix C=Matrix(n,n);
	
	double **D=new double*[n];
	double **E=new double*[n];
	double **F=new double*[n];
	for(int i=0;i<n;i++){
		D[i]=new double[n];
		E[i]=new double[n];
		F[i]=new double[n];
	}
	
	//note:  Garcia indexes from 1, not from zero!
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			A(i,j)=uran(rgen);   //plug in a random number
			B(i,j)=uran(rgen);
		}
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			D[i][j]=uran(rgen);
			E[i][j]=uran(rgen);
		}
	}
	
	
	auto start=std::chrono::steady_clock::now();  //this the start timer
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			for(int k=1;k<=n;k++){
				C(i,j)+=A(i,k)*B(k,j);
			}
		}
	}
	auto end=std::chrono::steady_clock::now();  //this the start timer
	auto timediff=std::chrono::duration_cast<std::chrono::microseconds>(end-start);
	std::cout<<"took "<<timediff.count()/1000000.0<<" s\n";

	
	start=std::chrono::steady_clock::now();  //this the start timer
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			for(int k=0;k<n;k++){
				F[i][j]+=D[i][k]*E[k][j];
			}
		}
	}
	end=std::chrono::steady_clock::now();  //this the start timer
	timediff=std::chrono::duration_cast<std::chrono::microseconds>(end-start);
	std::cout<<"took "<<timediff.count()/1000000.0<<" s\n";
	
	return 0;
}
