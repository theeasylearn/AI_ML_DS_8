import numpy as np 
arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr)
print("_"*100)
#column slicing 
print(arr[:,1])
print("_"*100)
#row slicing 
print(arr[1,:]) 

#mixed slicing
print(arr[0:2,1:3])

#array filter (get value greater then 30)
print(arr[arr>30])

#array filter (get value greater then 60)
print(arr[arr>60])