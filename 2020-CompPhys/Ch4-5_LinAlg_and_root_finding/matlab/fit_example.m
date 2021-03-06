tvals=(-200:200)/20;
noise=randn(1,length(tvals))*0.1;  %randn stands for random_normal.  we have not discussed random number generation yet.  
xvals=2*sin(tvals*2*pi/10)+noise;

vals=[1,1,2*pi/8];  %initial guess.  We have 3 parameters in our fit function
bestfit=fminsearch(@(x)lsquares(tvals,xvals,@fitfunction,x),vals);  
%minimize the squared error.  Note that matlab doesn't have an easy
%single function that performs a least squares search, so we had to 
%define a function to do it by defining lsquares (squared error between data 
%and fit), and using the fminsearch function to minimize that.

figure %plot data and fit
hold on
plot(tvals,xvals,'o')
plot(tvals,fitfunction(tvals,bestfit),'k','Linewidth',2)



function x=fitfunction(t,params)
    A=params(1);
    B=params(2);
    omega=params(3);
    x=A*sin(omega*t)+B*cos(omega*t);  %our fit function
end

function d=lsquares(tvals,xvals,fitfunction,params)  %computes the squared error between fit and data
    d=sum((xvals-fitfunction(tvals,params)).^2);
end
