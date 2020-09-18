import numpy as np

def GSO(a,b):
	magSqA=a.dot(a)   # check to see if |a|>0 for safety, not included here.  
	if magSqA<0.0000000001:
		print("zero vector")
		return [a,b]
	
	magSqB=b.dot(b)
	dotprod=a.dot(b)
	
	v1=np.copy(a)   # in python, v1=a means that v1 points to the memory location of a
	v2=np.copy(b)	# and can't be changed by this function
	
	v2=np.subtract(v2,dotprod*a/magSqA)
	
	v2=v2/np.sqrt(v2.dot(v2))*np.sqrt(magSqB)
	
	return [v1,v2]
	
	
a=np.array([1,1,1],dtype='float')
b=np.array([1,2,3],dtype='float')
v1=np.zeros(3);
v2=np.zeros(3);
[v1,v2]=GSO(a,b)

print("testing results:  ")
print("mag1:  "+str(a.dot(a))+" "+str(v1.dot(v1)))
print("mag2:  "+str(b.dot(b))+" "+str(v2.dot(v2)))
print("dot prod:  "+str(v1.dot(v2)))
