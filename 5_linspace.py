import numpy as np 


#create an array that has 10 value between 1 and 2

array1 = np.linspace(1.0,2.0,num=10)


#crete an array has that 5 values between 2 and 3 and also need step size 

array2, step = np.linspace(2,3,num=5,retstep=True,endpoint=False)

print(array1)
print(array2,step)