import numpy as np

#display numpy version
print(np.__version__)

list = [15,5,20,10,3]
tuple = (115,25,120,110,30.2)

#create array from list and tuple (sequence)
array_1 = np.array(list)
array_2 = np.array(tuple)

print(array_1,array_2)
