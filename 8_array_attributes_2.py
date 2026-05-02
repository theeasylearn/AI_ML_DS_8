import numpy as np 

array_3d = np.array([
        [
            [10,20],
            [40,5],
            [70,80],
        ],
        [
            [11,21,],
            [41,51],
            [71,81],
        ],
        [
            [12,22],
            [42,52],
            [72,82],
        ],
    ],dtype=np.int16)
print(array_3d)
print(array_3d.ndim) #3
print(array_3d.shape) # (3,3,2) 
print(array_3d.size) # (18) 
print(array_3d.dtype) 
print(array_3d.itemsize) 
print(array_3d.nbytes) #total size of array
print(array_3d.T) 