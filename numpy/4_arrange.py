import numpy as np 

#create an array which has 0 to 10 
array1 = np.arange(stop=11)

#create an array which has 10 to 20 
array2 = np.arange(start=10,stop=21)


#create an integer array which has 5,10,15 .... 50
array3 = np.arange(start=5,stop=51,step=5,dtype=int)

print(array1,array2,array3)