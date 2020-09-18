#include <fstream>
#include <math.h>

double diff(double dt){
	double e=9*exp(-2);
	double f=1/(1+e);
	double der=e*f*f;
	double fnew=1/(1+9*exp(-2-dt));
	return fabs(der-(fnew-f)/dt);
}

int main(){
	
	std::ofstream outfile("c_problem1.txt");
	for(int i=0;i<20;i++){
		double dt=pow(10,-((double)i));
		outfile<<dt<<","<<diff(dt)<<"\n";
	}
	outfile.close();
	
	return 0;
}
