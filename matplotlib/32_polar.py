import matplotlib.pyplot as plt 
import numpy as np 

positions = ["Wicketkeeper", "First Slip", "Third Man", "Point", "Deep Cover", "Cover", 
             "Long-off", "Mid-off", "Mid-on", "Long-on", "Mid-wicket",]
angles_deg = [180, 195, 225, 270, 300, 315, 340, 345, 15, 20, 45]
distances = [20, 22, 55, 25, 68, 26, 75, 25, 25, 75, 24]

angles_rad = np.radians(angles_deg)

plt.polar(angles_rad,distances)
plt.title('field placement')
plt.show()

