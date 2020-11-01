nlist=[10 20 50 100 200 500 1000 2000];
klist=zeros(length(nlist),1);


for niter=1:length(nlist)
   n=nlist(niter);              %matrix size
   A=(ones(n,n)+eye(n))./(n+1); % matrix
   B=eye(n)-A;                  % 1-A, needed for taylor expansion
   lmax=max(eig(B));  %smallest eigenvalue of A (leads to slowest convergence of 1-A)
   kmax=findmax(lmax,.0005);
   klist(niter)=kmax;
end


tlist=zeros(length(nlist),4);
for niter=1:length(nlist)
   tic;
   n=nlist(niter);              %matrix size
   A=(ones(n,n)+eye(n))./(n+1); % matrix
   B=eye(n)-A;                  % 1-A, needed for taylor expansion
   Bpow=eye(n);                 % where we store B^k
   logA=zeros(n,n);             % where we store log(A)
   t1=toc;                      %done with memory allocation, etc.  Let's save that value

   tic;   
   k=1;
   while k<klist(niter)                 %taylor iterations up to kmax
       Bpow=Bpow*B;
       logA=logA-Bpow./k;
       k=k+1;
   end
   t2=toc;              %finish timing
   if(niter==1)
       csvwrite('log_A_10_matlab.csv',logA);
   end
                        %store values
   tlist(niter,1)=n;
   tlist(niter,2)=t1;
   tlist(niter,3)=t2;
   tlist(niter,4)=k;
end
csvwrite('matlab_times.txt',tlist);



function k=findmax(x,tol)
    k=1;
    y=x;
    ss=0;
    while(abs(ss-log(1-x))/abs(log(1-x))>tol)
       ss=ss-y/k;  % ss= -x/1-x^2/2-....
       y=y*x;  %y=x^k
       k=k+1;
    end
end