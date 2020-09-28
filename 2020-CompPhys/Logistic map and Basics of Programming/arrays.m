n=10;  %columns


A=rand(n,n);
B=rand(n,n);
C=zeros(n,n);

tic
for i=1:n
	for j=1:n
		for k=1:n
			C[i,j]+=A[i,k]*B[k,j];
		end
	end
end
toc

tic
Cfast=A*B;
toc


