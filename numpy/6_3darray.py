import numpy as np 

array_3d = np.array([
        [
            [10,20,30],
            [40,50,60],
            [70,80,90],
        ],
        [
            [11,21,31],
            [41,51,61],
            [71,81,91],
        ],
        [
            [12,22,32],
            [42,52,62],
            [72,82,92],
        ],
    ])
print(array_3d)

#access 0th deapth 1st row and 2nd column element
print(array_3d[0][1][2])

#update 1th deapth 1st row and 2nd column element
array_3d[1][1][2] = 999
print(array_3d)
