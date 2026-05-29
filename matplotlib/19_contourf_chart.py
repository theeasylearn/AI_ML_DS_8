import matplotlib.pyplot as plt 
import numpy as np 
plt.figure(figsize=(10, 6))
room_width = np.linspace(0,10,10)
# 1D array of height positions (e.g., 0 to 3 meters)
room_height = np.linspace(0,10,10)
# 2. Create a 2D grid from the 1D arrays
X, Y = np.meshgrid(room_width, room_height)
# print(X,Y)
room_temperature = 25 + 5 * np.exp(-((X - 2.5)**2 + (Y - 3.0)**2) / 4)
plt.contourf(X,Y,room_temperature,levels=10,cmap='viridis')
plt.xlabel('room width')
plt.ylabel('room height')
# plt.colorbar(label=room_temperature)
plt.title("Room temperature contour chart")
plt.show()


