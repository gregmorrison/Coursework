#include <iostream>
#include <vector>
#include <chrono>

#define n 1000
#define m 500


int main(){
	
	double v1[n]={0};  //initialized to zero
	for(int i=0;i<n;i++){
		v1[i]=1;
	}
	double v2[m]={0};
	for(int i=0;i<m;i++){
		v2[i]=i;
	}
	double mat[m][n]={{3}};  //this DOESN'T initialize the matrix to 3.  only 							the first element is = 3
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			mat[j][i]=3;
		}
	}
	
	auto start=std::chrono::steady_clock::now();  //this the start timer
	double product=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			product=product+v2[j]*mat[j][i]*v1[i];
		}
	}
	std::cout<<"The product was "<<product<<" using a static array.\n";
	auto end=std::chrono::steady_clock::now();  //this the start timer
	auto timediff=std::chrono::duration_cast<std::chrono::microseconds>(end-start);
	std::cout<<"Time to compute the product v2.mat.v1 was "<<timediff.count()<<" us\n";
	
	
	
	std::vector<double> u1(n,1);  //initalize a vector to 1
	std::vector<double> u2(m,0);
	for(int i=0;i<m;i++){
		u2[i]=i;
	}
	std::vector<double> tmp(m,3);
	std::vector<std::vector<double> > mat2(n,tmp);
	
	//another way to define the arrays
	//same speed as arrays above, just different initialization.
	
	
	
	
	return 0;
}
