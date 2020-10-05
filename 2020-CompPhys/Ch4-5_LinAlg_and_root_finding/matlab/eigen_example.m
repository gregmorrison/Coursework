n=1000;  %columns



A=rand(n,n);
A=(A+A')/2;

%A=ones(n,n);

tic
[V,D]=eig(A);
toc

%disp(num2str(A*V(:,n)/D(n,n)));
%disp(" ")
%disp(num2str(V(:,n)));
