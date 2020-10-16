#include <iostream>
#include <math.h>
#include <fstream>

double bisect(double (*fcn)(double x),double &a,double &b);
double sign(double x);
double F(double x);

int main(){
	
	double a,b,fold,fnew;
	int n;
	double tol=0.00001;
	
	a=8;
	b=10;
	fold=0;
	fnew=2*tol;
	n=0;
	while(abs(fold-fnew)>tol){
		fold=fnew;
		fnew=bisect(F,a,b);
		n+=1;
	}
	std::cout<<"after "<<n<<" steps, the root was bounded within:\n";
	std::cout<<std::setprecision(10)<<a<<","<<b<<", with a function value at the midpoint of "<<fnew<<"\n\n";
	
	a=0;
	b=2;
	fold=0;
	fnew=2*tol;
	n=0;
	while(abs(fold-fnew)>tol){
		fold=fnew;
		fnew=bisect(F,a,b);
		n+=1;
	}
	std::cout<<"after "<<n<<" steps, the root was bounded within:\n";
	std::cout<<std::setprecision(10)<<a<<","<<b<<", with a function value at the midpoint of "<<fnew<<"\n\n";
	
	
	
	a=-2;
	b=0;
	fold=0;
	fnew=2*tol;
	n=0;
	while(abs(fold-fnew)>tol){
		fold=fnew;
		fnew=bisect(F,a,b);
		n+=1;
	}
	std::cout<<"after "<<n<<" steps, the root was bounded within:\n";
	std::cout<<std::setprecision(10)<<a<<","<<b<<", with a function value at the midpoint of "<<fnew<<"\n\n";
	
	return 0;
}

double bisect(double (*fcn)(double x),double &a,double &b){
	double sa=sign((*fcn)(a));
	double sb=sign((*fcn)(b));
	double mid=(a+b)/2;
	double fmid=(*fcn)(mid);
	double sm=sign(fmid);
	if(sm==sa){
		a=mid;
	}
	else{
		b=mid;
	}
	return fmid;
}

double sign(double x){
	if(x>0){
		return 1;
	}
	if(x<0){
		return -1;
	}
	return 0;
}

double F(double x){
	return exp(x)-x*x*x*x;
}
