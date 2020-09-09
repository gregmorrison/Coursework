
%  PARAMETERS

max_iterations=10000;  % max number of iterations
numprint=30;  % how many numbers to print to the screen
r=1.4;  % our choice of r

% INITIALIZATION
x=.01;  %our initial value

% ITERATIONS
for iter=1:max_iterations
	x=logistic_calculate(r,x);
	if max_iterations-iter<numprint
		disp(x);
	end
end  %end of iteration loop

% in matlab, functions are defined at the end of the script, not the beginning.
%t they can be declared externally too, which we'll see later.
function x=logistic_calculate(r,x)
	x=r*x*(1-x);
end
