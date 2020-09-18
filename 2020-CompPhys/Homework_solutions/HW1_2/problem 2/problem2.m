disp("integer test:  ")
x=1;
for iter=1:1024
    x=x*2;
    if(iter>1022)
        disp(strcat("2^",num2str(iter)," = ",num2str(x)))
    end
end
%returns an inf for the integer rep

disp("double test:  ")
y=1;
for iter=1:1024
    y=y*2;
    if(iter>1022)
        disp(strcat("2^",num2str(iter)," = ",num2str(y)))
    end
end
%returns an inf for the dlouble rep