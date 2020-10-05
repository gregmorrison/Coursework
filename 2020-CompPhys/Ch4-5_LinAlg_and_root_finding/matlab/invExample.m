n=5;  %columns
A=rand(n,n);
%A=ones(n,n);
y=rand(n,1);

tic
s1=linsolve(A,y);
toc

tic
Ainv=inv(A);
s2=Ainv*y;
toc

%A*Ainv
%det(A)
