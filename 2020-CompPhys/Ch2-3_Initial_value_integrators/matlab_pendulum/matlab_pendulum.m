
addpath('NM4P/Matlab');

theta=0.1*pi;
omega=0;
t=0;
T=30;
g=9.81;
L=1.0;


dt=0.1;
nstep=T/dt;

params=[];
X=[0,0];
sampleTimes=(1:(nstep+1))*dt;
eulerResults=[theta];
rk4Results=[theta];
verletResults=[theta];


X(1)=theta;
X(2)=omega;
t=0;
for iter=1:nstep
    X=euler(X,t,dt,'deriv',params);
    eulerResults=[eulerResults X(1)];
    t=t+dt;
end

X(1)=theta;
X(2)=omega;
t=0;
for iter=1:nstep
    X=rk4(X,t,dt,'deriv',params);
    rk4Results=[rk4Results X(1)];
    t=t+dt;
end


X(2)=theta;
thetaNew=theta+dt*omega+dt*dt*(-sin(theta))/2;
X(1)=thetaNew;
verletResults=[verletResults thetaNew];
t=0;
for iter=1:nstep-1
    thetaCurrent=X(1);
    thetaNew=2*X(1)-X(2)+dt*dt*(-sin(thetaCurrent));
    X(1)=thetaNew;
    X(2)=thetaCurrent;
    verletResults=[verletResults thetaNew];
    t=t+dt;
end



figure
subplot(121)
hold on
plot(sampleTimes,eulerResults,'b'); 
plot(sampleTimes,rk4Results,'k'); 
plot(sampleTimes,verletResults+.01,'r'); 
xlabel('t');
ylabel('theta');
legend({'euler','rk4','verlet'},'Location','southwest');

subplot(122)
hold on
plot(sampleTimes,rk4Results-verletResults,'k'); 
xlabel('t');
ylabel('theta');



function xnew=euler(x,t,tau,deriv,params)
    xnew=x+tau*feval(deriv,x,t,params);
end


