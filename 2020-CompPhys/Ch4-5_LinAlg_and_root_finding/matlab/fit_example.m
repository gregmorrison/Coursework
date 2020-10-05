

tvals=(-200:200)/20;
noise=randn(1,length(tvals))*0.1;  %randn stands for random_normal.  we have not discussed random number generation yet.  
xvals=2*sin(tvals*2*pi/10)+noise;


figure 

plot(tvals,xvals,'o')

function x=fitfunction(t,A,B,omega)
    x=A*sin(omega*t)+B*cos(omega*t);
end
