import numpy as np 

#create an array with zero 
array1 = np.zeros(5)

#create an array with 1s
array2 = np.ones(10)

#create an 2 dimensional array 
array3 = np.ones([5,3])

print(array1)
print(array2)
print(array3)

#we can update value of any specific element
#update 0th element in array1 
array1[0] = 10 

#update 1st element in array 2
array2[1] = 100

#update 0th row and 1st column in array3
array3[0][1] = 999

print("now let us display all array again")
print(array1,array2)
print(array3)


