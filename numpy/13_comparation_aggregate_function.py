import numpy as np 

a = np.array([10, 20, 30, 7,15])

#relational operators 
print(a>15)

X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
#matrix multiplication
print(X @ Y) 
print(np.dot(X,Y))


#aggregate function
print("sum ",np.sum(a))
print("minimum ",np.min(a))
print("maximum ",np.max(a))
print("average (mean)",np.mean(a))