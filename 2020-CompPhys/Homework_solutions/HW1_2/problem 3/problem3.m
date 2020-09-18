a=[1 1 1];
b=[1 2 3];

[v1,v2]=GSO(a,b);

disp("testing:  ");
disp("mag 1:  "+num2str(dot(a,a))+" "+num2str(dot(v1,v1)));
disp("mag 2:  "+num2str(dot(b,b))+" "+num2str(dot(v2,v2)));
disp("dot product:  "+num2str(dot(v1,v2)));



function [v1,v2]=GSO(a,b)
    v1=a;
    v2=b-dot(a,b)*a/dot(a,a);
    v2=v2*sqrt(dot(b,b))/sqrt(dot(v2,v2));
	%not safe, didn't check for |a|
end
