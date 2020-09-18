#include <vector>
#include <iostream>
#include <math.h>

							  
						
void GSO(double *a,double *b,double *v1,double *v2,int size){
	

	double magSqA=0;
	double magSqB=0;
	double dotprod=0;

	for(int i=0;i<size;i++){
		magSqA+=a[i]*a[i];
		magSqB+=b[i]*b[i];
		dotprod+=a[i]*b[i];
	}
	for(int i=0;i<size;i++){
		v1[i]=a[i];
		v2[i]=b[i];
	}
	if(magSqA>1e-15){
		for(int i=0;i<size;i++){
			v2[i]-=dotprod*a[i]/magSqA;
		}
	}
	

	double magSqV2=0;
	for(int i=0;i<size;i++){
		magSqV2+=v2[i]*v2[i];
	}
	for(int i=0;i<size;i++){
		v2[i]=v2[i]*sqrt(magSqB)/sqrt(magSqV2);
	}
}

							  

int main(){
	
	int size=3;
	double *a=new double[size];
	double *b=new double[size];
	double *v1=new double[size];
	double *v2=new double[size];
	//declare memory.  vector would work here too, as would static arrays.
	// std::vector<double> v1={1,1,1}
	
	a[0]=1;
	a[1]=1;
	a[2]=1;
	
	b[0]=1;
	b[1]=2;
	b[2]=3;
//assign some values for testing.
	
	GSO(a,b,v1,v2,size);
	//use GSO as defined
	
	
	
	
	std::cout<<"testing results:  \n";
	
	
	double magSqV1=0;
	double magSqA=0;
	for(int i=0;i<size;i++){
		magSqA+=a[i]*a[i];
		magSqV1+=v1[i]*v1[i];
	}
	std::cout<<"mag A:  "<<magSqA<<","<<magSqV1<<"\n";
	//make sure that |v1|=|a|
	
	double magSqV2=0;
	double magSqB=0;
	for(int i=0;i<size;i++){
		magSqB+=b[i]*b[i];
		magSqV2+=v2[i]*v2[i];
	}
	std::cout<<"mag B:  "<<magSqB<<","<<magSqV2<<"\n";
	//make sure that |v2|=|b|
	
	double dp=0;
	for(int i=0;i<size;i++){
		dp+=v1[i]*v2[i];
	}
	std::cout<<"dot prod:  "<<dp<<"\n";
	//make sure that v1.v2=0;
	
	return 0;
}




