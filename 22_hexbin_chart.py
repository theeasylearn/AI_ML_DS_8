import matplotlib.pyplot as plt 
import numpy as np 
# 1. Initialize seed for consistent coordinate simulation
np.random.seed(42)

num_of_rides = 1000

# 2. Simulate geographical ride hot-spots across Ahmedabad
# Hub 1: Kalupur Area | Hub 2: Satellite/Vastrapur | Hub 3: Ashram Road
lat_hubs = [23.03, 23.02, 23.05]
lon_hubs = [72.60, 72.53, 72.57]
lats = []
lons = []
for count in range(num_of_rides):
    # Route weights simulating standard ride distribution density
    hub_idx = np.random.choice([0, 1, 2], p=[0.4, 0.4, 0.2])
    lats.append(np.random.normal(lat_hubs[hub_idx], 0.025))
    lons.append(np.random.normal(lon_hubs[hub_idx], 0.025))

# Mock categorization between providers
services = np.random.choice(['Ola', 'Uber'], size=num_of_rides, p=[0.48, 0.52])

plt.hexbin(lons,lats,gridsize=30,cmap='inferno')
plt.title('Hexbin Density Mapping: 1,000 Ola/Uber Rides in Ahmedabad', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Longitude', fontsize=11, labelpad=10)
plt.ylabel('Latitude', fontsize=11, labelpad=10)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()