import numpy as np 

#generate random array size of 3 x 2 
array_1 = np.random.rand(3,2)
print(array_1)

#generate random array of integer type which has 10 value between 50 to 100
array_2 = np.random.randint(50,101,size=10)
print(array_2)

#create float type array between 10 to 20 size 5
array_3 = np.random.normal(10,21,size=5)
print(array_3)

print("one item from array 2 ",np.random.choice(array_2))

np.random.shuffle(array_2)
print("Array2 after shuffle ",array_2)