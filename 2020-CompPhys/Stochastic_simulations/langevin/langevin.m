rng(1,'twister');

kT=4.1;
zeta=20;
m=4.2;
dt=0.02;
nstep=100000;
xvals=zeros(1,nstep);
tvals=zeros(1,nstep);

x=0;
t=0;
xold=0;
xnew=0;

xvals=zeros(1,nstep);
tvals=zeros(1,nstep);

stiffness=.5*zeta*kT;
for i=1:nstep
    f=force(x,stiffness);
    R=randn()*sqrt(2*zeta*kT/dt);
    xnew=x;
    xnew=xnew+(x-xold)*(1-zeta*dt/2/m)/(1+zeta*dt/2/m);
	xnew=xnew+(f+R)*dt*dt/m/(1+zeta*dt/2/m);
	xold=x;
	x=xnew;
	t=t+dt;
    xvals(i)=x;
    tvals(i)=t;
end


figure
plot(tvals,xvals)

function f=force(x,k)
    x0=floor(x)+0.5;
    f=-k*(x-x0);
end