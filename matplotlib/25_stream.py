import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-2,2,10)
y = np.linspace(-2,2,10)

print(x,y)
X,Y = np.meshgrid(x,y)

U = -Y
V = X

plt.streamplot(X,Y,U,V)
plt.show()