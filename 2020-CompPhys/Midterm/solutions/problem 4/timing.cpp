#include<iostream>
#include<fstream>
#include<chrono>

int main(){
	
	int nlist[8]={10,20,50,100,200,500,1000,2000};
	int klist[8]={53,99,231,444,862,2084,4077,7994};
	double tlist[8][2]={{0}};
	
	
	//int nlist[1]={10};
	//int klist[1]={53};
	//double tlist[1][2]={{0}};

	std::ofstream timefile;
	timefile.open("cpp_times.txt");
	
	for(int niter=0;niter<8;niter++){
		

		
		int n=nlist[niter];
		double ** A=new double*[n];
		double ** B=new double*[n];
		double ** Bpow=new double*[n];
		double ** Btemp=new double*[n];
		double ** logA=new double*[n];
		for(int i=0;i<n;i++){
			A[i]=new double[n];
			B[i]=new double[n];
			Bpow[i]=new double[n];
			Btemp[i]=new double[n];
			logA[i]=new double[n];
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				A[i][j]=1/(((double)(n))+1);
			}
			A[i][i]+=1/(((double)(n))+1);
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				B[i][j]=-A[i][j];
			}
			B[i][i]+=1;
			Bpow[i][i]=1;
		}
		

		auto start=std::chrono::steady_clock::now();  //this the start time
		
		for(int k=1;k<klist[niter];k++){
			
			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++){
					Btemp[i][j]=0;
				}
			}

			for(int i=0;i<n;i++){
				for(int l=0;l<n;l++){
					for(int j=0;j<n;j++){
						Btemp[i][j]+=Bpow[i][l]*B[l][j];
					}
				}
			}
			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++){
					Bpow[i][j]=Btemp[i][j];
				}
			}

			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++){
					logA[i][j]-=Bpow[i][j]/k;
				}
			}

		}
		
	
		auto end=std::chrono::steady_clock::now();  //this the start timer
		auto timediff=std::chrono::duration_cast<std::chrono::microseconds>(end-start);
		
		timefile<<n<<","<<timediff.count()/1000000.<<std::endl;
		std::cout<<n<<"\n";
		
		
		if(niter==1){
			std::ofstream outfile;
			outfile.open("log_A_10_cpp.txt");
			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++){
					if(j>0){
						outfile<<",";
					}
					outfile<<logA[i][j];
				}
				outfile<<"\n";
			}
		}
		
		
		for(int i=0;i<n;i++){
			delete[] A[i];
			delete[] B[i];
			delete[] Bpow[i];
			delete[] logA[i];
		}
		delete[] A;
		delete[] B;
		delete[] Bpow;
		delete[] logA;

	}
	
	timefile.close();
	
	
	
	return 0;
}
