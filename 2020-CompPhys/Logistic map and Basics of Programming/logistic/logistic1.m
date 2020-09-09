max_iteration=10000;  % max number of iterations
max_period=256;
start_testing=max_iteration-max_period;
numdiv=5000;
tolerance=1e-8;

bfile=fopen('bifurcations_matlab.txt','w');
pfile=fopen('periods_matlab.txt','w');

for riter=0:numdiv-1
    r=1.0+3.0*(riter)/numdiv;
    
    x=0.001;
    xobs=0;
    period=max_period;
    
    for iter=0:max_iteration-1
        x=logistic_calculate(r,x);
    
        if iter==start_testing
            xobs=x;
            fprintf(bfile,'%f',r);  %f means float, %d means integer
        end
        if iter>start_testing
            fprintf(bfile,',%f',x);
            if abs(x-xobs)<tolerance
                period=iter-start_testing; 
            end
        end
    end
    fprintf(bfile,'\n');
    fprintf(pfile,'%f,%f\n',r,period);
end


function x=logistic_calculate(r,x)
	x=r*x*(1-x);
end
