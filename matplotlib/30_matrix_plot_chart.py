import matplotlib.pyplot as plt
import numpy as np

leh_march_2026 = [
    -5.0, -5.0, -1.0, 2.0, 4.0, 5.0, 3.0, 1.0, 3.0, 2.0,
    2.0, -2.0, -4.0, -3.0, -2.0, -5.0, -5.0, -2.0, -1.0, -2.0,
    -4.0, -4.0, -3.0, -5.0, -3.0, -1.0, -1.0, 0.0, 2.0, 3.0, 1.0
]

# Convert the 1D list into a 2D matrix so matshow plots it cleanly
# We add an extra dimension to make it a 1 row x 31 columns matrix
data_matrix = np.array(leh_march_2026).reshape(1, -1)

# Initialize the figure
fig, ax = plt.subplots(figsize=(12, 3))

# Plot using matshow on the axes
cax = ax.matshow(data_matrix, cmap='hot')

# FIX: Explicitly use the 'label' keyword argument
plt.colorbar(cax, label='Temperature (°C)')

plt.title('Leh Temperature - March 2026', pad=20)
plt.xlabel('Day of Month')
plt.yticks([]) # Hide the y-axis since it's just 1 row

plt.show()