import numpy as np
import time 
print("")

#multiply v2 . matrix . v1

n=1000;
m=500;


start=time.time()  #start time
v1=[1]*n  					#construct a list of n constant elements
v2=[i for i in range(m)];	#construct a list of varying elements
mat=[[3]*n]*m				# construct a 2d list


print("there are "+str(len(mat))+" rows in mat");
print("there are "+str(len(mat[0]))+" columns in mat");


product=0 			# we will compute v2.mat.v1
for i in range(m):
	for j in range(n):
		product=product+v2[i]*mat[i][j]*v1[j]

print("the value of the first element is "+str(mat[0][0]))
print("the product v2.mat.v1 = "+str(product))

end=time.time();  #end time
print("the calculation took "+str(end-start)+" seconds using standard python methods");


print("")



start=time.time()

u1=np.ones(n)			#build a list of ones
u2=np.arange(m)		#build a range 0..m-1
mat2=np.full((m,n),3)	#build an nxm array filled with the value 3.  

print("there are "+str(mat2.shape)+" rows and columns in mat2")

product=u2.dot(mat2.dot(u1))  #compute u2.mat2.u1


print("the value of the first element is "+str(mat2[0][0]))
print("the product u2.mat2.u1 = "+str(product))
end=time.time()
print("the calculation took "+str(end-start)+" seconds using numpy methods");

print("")