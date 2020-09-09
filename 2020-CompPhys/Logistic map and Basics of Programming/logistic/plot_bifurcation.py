import numpy as np  #read in csv files.
import pandas as pd  #read in csv files.  

import matplotlib as mp			#plot data
import matplotlib.pyplot as plt	#plot data


bdata=np.genfromtxt('bifurcations.txt',delimiter=',')
## This uses numpy to import the data.

#PandasData=pd.read_csv('bifurcations.txt')
#bdata=PandasData.values.tolist()
##  This uses pandas to import the data
##  NOTE:  pandas imports this as a data frame, not a list or array.
## 	we have to convert it!



nrow=len(bdata)
ncol=len(bdata[0])
for riter in range(0,nrow,5):
	#each row corresponds to a particular choice for r.  
	# we skip every 5th row in this command.  

	yvals=bdata[riter][1:]
	#every observed value for x for this r.  
	# the 0th element is r
	# later elements are one of 256 observed values of x.
	
	
	
	yvals=list(set(yvals))
		#this picks out every unique value of r.
		# the set() finds the unique elements.  This is stored as a set
		# which we must convert to a list.
	
#	yvals=np.unique(np.array(yvals))
		#another way to do it, using numpy.

#	yvals=pd.Series(yvals).unique()
		#another way to do it, using pandas.
		
		
	xvals=[bdata[riter][0]]*len(yvals)
	#this is just a list containing the value r
	# the length of this list is the same as the length of the y values.

	plt.scatter(xvals,yvals,marker=".",s=3,color='b')
	#note that this commands creates an image of the points at each value
	#of r.  we have to iterate over r and add each layer to the list.

	plt.suptitle('bifurcation diagram')
	plt.xlabel('r')
	plt.ylabel('x')
	
plt.savefig('bifurcation_python.png')
#save the figure.
plt.show();
#show the plot.  Note that .show() clears the plot afterwards!







