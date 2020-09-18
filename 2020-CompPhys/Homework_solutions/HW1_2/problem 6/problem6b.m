max_iteration=10000;  % max number of iterations
max_period=256;
start_testing=max_iteration-max_period;
numdiv=5000;


rlist=[];
xlist=[];
for riter=0:numdiv-1
    r=1.0+14.0*(riter)/numdiv;  %min r=1, max r~15
    rlist=[rlist r];
    x=0.001;
    xobs=0;
    period=max_period;
    xtmp=[];
    for iter=0:max_iteration-1
        x=r*x/(1+x*x);
        if iter>start_testing
            xtmp=[xtmp x];
        end
    end
    xlist=[xlist ; xtmp];
end

f=figure;
hold all;
set(f,'Visible','on');
plot(rlist,xlist,'.','MarkerSize',1,'color','black');
title('bifurcation diagram for rx/(1+x^2)');
box on
xlabel('r');
ylabel('x_n');
saveas(gcf,'bifurcation_7b','epsc');
hold off



