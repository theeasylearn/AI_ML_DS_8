import numpy as np

arr1 = np.array([1, 2, 3, -1, 5])
arr2 = np.array([4, 0, 2, 7, 3])

and_operations = np.logical_and(arr1>0,arr2<5)
print(and_operations)

or_operations = np.logical_or(arr1>0,arr2<8)
print(or_operations)

not_operations = np.logical_not(arr1>0)
print(not_operations)

xor_operations = np.logical_xor(arr1>3,arr2<8)

print(xor_operations)




