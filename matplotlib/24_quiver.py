import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Establish Precision Environment & Base Constraints
np.random.seed(42)
num_vehicles = 100

# Central coordinate anchor for Ahmedabad layout
base_lat = 23.0225
base_lon = 72.5714

# 2. Simulate Spatial Distribution (X, Y) Scaler operation
lons = base_lon + np.random.uniform(-0.05, 0.05, num_vehicles)
lats = base_lat + np.random.uniform(-0.05, 0.05, num_vehicles)

# 3. Formulate Directional Delta Vectors (U, V)
u_vectors = np.random.uniform(-0.006, 0.006, num_vehicles)
v_vectors = np.random.uniform(-0.006, 0.006, num_vehicles)



# 5. Initialize Canvas using standard Matplotlib styling
fig, ax = plt.subplots(figsize=(11, 9), dpi=300)

# Configure a clean background grid directly through Matplotlib axes
ax.grid(True, linestyle='--', linewidth=0.5, color='#d3d3d3', zorder=0)
ax.set_facecolor('#fdfdfd')

# Create the Quiver Plot
quiver = ax.quiver(
    lons,lats,u_vectors,v_vectors        # Ensures vectors sit cleanly above grid lines
)

# 7. Refine Labels, Titles, and Tick marks
ax.set_title("Ahmedabad City Traffic Vector Field Analysis (100 Vehicle Base)", fontsize=13, pad=15, fontweight='semibold')
ax.set_xlabel("Longitude Coordinates (X-Axis)", fontsize=11, labelpad=8)
ax.set_ylabel("Latitude Coordinates (Y-Axis)", fontsize=11, labelpad=8)
plt.show()