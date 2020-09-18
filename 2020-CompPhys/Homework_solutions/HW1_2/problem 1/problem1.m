xvals=zeros(1,21);
yvals=zeros(1,21);
dt=1;
for iter=0:20
   dt=10^(-iter);
   diff=difference(dt);
   xvals(iter+1)=dt;
   yvals(iter+1)=diff;
end

f=figure;
hold all;
ax=gca;
plot(xvals,yvals,'-o','color','black');
ax.XScale='log';
ax.YScale='log';
title('matlab');
xlabel('dt');
ylabel('difference')
box on;
set(f,'Visible','off');
saveas(f,'matlab','epsc');
hold off


function g = difference(dt)
    e=9*exp(-2);
    f=1/(1+e);
    der=e*f*f;
    fnew=1/(1+9*exp(-2-dt));
    g=abs(der-(fnew-f)/dt);
end