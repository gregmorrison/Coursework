
[t,result]=ode45(@deriv,[0,200000],[.00001]);

figure

plot(t,result)


function f=deriv(t,X)
   f=X*X-X*X*X; 
end
