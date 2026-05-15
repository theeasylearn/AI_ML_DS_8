import matplotlib.pyplot as plt
import numpy as np

# Data
rohit_centuries = [3, 2, 8, 6, 10, 1, 2, 0, 4, 4, 2]
virat_centuries = [4, 11, 11, 11, 7, 0, 0, 2, 10, 3, 4]
years = np.arange(2015, 2026)

# Non-overlapping (side-by-side) bar chart
width = 0.35

#set chart size horizontally and vertically 
chart_width = 12
chart_length = 6
plt.figure(figsize=(chart_width,chart_length))

plt.bar(years - width/2, rohit_centuries, width=width, color='red', label='Rohit Sharma')
plt.bar(years + width/2, virat_centuries, width=width, color='yellow', label='Virat Kohli')

plt.xlabel('Years')
plt.ylabel('Number of Centuries')
plt.title("Centuries by Rohit Sharma and Virat Kohli (2015-2025)")
plt.xticks(ticks=years)
plt.legend()
plt.grid(axis='y', linestyle='--')

plt.show()