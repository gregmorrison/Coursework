eps=10;
alpha=.5;
max_eigenval=[];
for n=5:200
    M1=zeros(n,n);
	M2=zeros(n,n);
    M1(1:1+n:end)=1-2*eps/2;
    M1(2:n+1:end)=eps/2;
    M1(n+1:1+n:end)=eps/2;

	M2(1:1+n:end)=1+2*eps/2;
	M2(2:n+1:end)=-eps/2;
	M2(n+1:1+n:end)=-eps/2;


	lambdamax=max(abs(eig(inv(M2)*M1)));
    max_eigenval=[max_eigenval ; [n lambdamax]];
end


figure
plot(max_eigenval(:,1),max_eigenval(:,2),'-o')
xlabel('n')
ylabel('labmda_{max}')
