import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-5,5,10)
y = np.linspace(-5,5,10)

print(x,y)
X,Y = np.meshgrid(x,y)

U = -X 
V = Y 

plt.quiver(X,Y,U,V)
plt.show()