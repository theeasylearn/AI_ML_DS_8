import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 0, 3])

print(a,b)

print(a == b)
print(a != b)

print("are both array same ",np.all(a==b)) #False
print("any one value in both is same ",np.any(a==b)) #True
