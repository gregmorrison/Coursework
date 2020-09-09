
#  FUNCTION DEFINITION
def logistic_calculate(r,x):
	#r and x are both passed by value, and cannot be updated within the function
	return r*x*(1-x)
	#this returns the new value of x.
# END OF FUNCTION DEFINITION


# PARAMETERS
max_iterations=10000  # how many iterations to do
numprint=30	 #how many numbers to print to the screen
r=1.4  # our choice for r.

# INITIALIZATION
x=0.01    # initial value for x

#iteratively update the value for x.
for iter in range(max_iterations):
	
	x=logistic_calculate(r,x);
	# x must be updated with the function by hand, since it was by value only.
	
	if max_iterations-iter<numprint:
		#if we have waited long enough, print to the terminal
		print(x);
		
		