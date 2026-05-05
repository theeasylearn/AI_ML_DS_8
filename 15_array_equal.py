import numpy as np 
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

arr3 = np.array([1, 2, 4])

arr4 = np.array([[1, 2, 3]])

print(arr1,arr2,arr3,arr4) 

print(np.array_equal(arr1,arr2)) #True because shape and values are same
print(np.array_equal(arr1,arr3)) #False because shape are same but one or more values are different
print(np.array_equal(arr1,arr4)) #False because shape are different 
print(np.all(arr1 == arr4)) #True because all function ignore the shape
