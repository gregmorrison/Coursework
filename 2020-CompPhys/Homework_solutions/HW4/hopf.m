trange=[0 20];

tol=odeset('RelTol',.1);

init=[0,2.5,-1];  %in this implementation, X=[x,y,a]
[t,W]=ode45(@deriv_lazy,trange,init,tol);  %perform the integration

init=[4,0,1];
[t,X]=ode45(@deriv_lazy,trange,init,tol);

init=[0,-1.5,4];
[t,Y]=ode45(@deriv_lazy,trange,init,tol);

init=[-4,0,4];
[t,Z]=ode45(@deriv_lazy,trange,init,tol);


disp(strcat("simulation generated:  ",string(length(W))," points for a=-1"))
disp(strcat("simulation generated:  ",string(length(X))," points for a=1"))
disp(strcat("simulation generated:  ",string(length(Y))," points for a=4"))
disp(strcat("simulation generated:  ",string(length(Z))," points for a=4"))

figure
hold on
scatter(W(:,1),W(:,2),'*')
scatter(X(:,1),X(:,2),'o')
scatter(Y(:,1),Y(:,2),'x')
scatter(Z(:,1),Z(:,2),'+')

xlabel('x')
ylabel('y')
legend('a=-1','a=1','a=4','a=4')

axis([-4 4 -4 4])
pbaspect([1 1 1])



%this is lazy, we build our parameter into the vector x:
% X=[x ; y ; a]
% and set da/dt = 0.
function dX=deriv_lazy(t,X)
    x=X(1);
    y=X(2);
    a=X(3);
    r=x^2+y^2;
    dX=[a*x+y-x*r;-x+a*y-y*r;0];
end
%this will become numerically unstable for long times, but 
% for moderate simulation time will work fine, and not require
% dealing with a paramter.  

%numericallly stable version of the function.  
function dX=deriv(t,X,param)
    x=X(1);
    y=X(2);
    r=x^2+y^2;
    dX=[param(1)*x+y-x*r;-x+param(1)*y-y*r];
end
% to implement this, pass as an implicit function.  for a=1, e.g.
%  [t,X]=ode45(@(t,y) deriv(t,y,1) , trange , init)
% I did not do so in these solutions, b/c implicit functions have not
% been discussed in any meaningful way  