
y=1.0

print("simple test:  guess and check got us to 1024")
for iter in range(1023):
	y=y*2.0
print(y)
y=y*2.0
print(y)


y=1.0
iter=1
while True:
	y=y*2.0
	iter=iter+1
	if y==float('inf'):
	#this step is not required, but makes life much easier to know when to stop
	# google:  how to test for infinity in python
		print('largest power of 2 at '+str(iter-1))
		break

print(" finished with floating point now")



#a similar block of code doesn't work for integers here, it just keeps growing without
# ever reaching inf.  Googling "what is the max size of an integer in python" explains
# that there is no maximum inti size, it's unbounded.  