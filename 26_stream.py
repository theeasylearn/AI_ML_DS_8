import numpy as np
import matplotlib.pyplot as plt

# 1. Setup a dense coordinate grid (Longitude -180 to 180, Latitude -90 to 90)
Y, X = np.mgrid[-90:90:200j, -180:180:400j]
U = np.zeros_like(X)
V = np.zeros_like(Y)

def add_gyre(lon_c, lat_c, r_lon, r_lat, strength, clockwise=True):
    """Simulates an mathematical elliptical fluid vortex for gyre flow."""
    direction = -1 if clockwise else 1
    dx = (X - lon_c) / r_lon
    dy = (Y - lat_c) / r_lat
    dist = np.sqrt(dx**2 + dy**2)
    
    mask = dist < 1.0
    profile = np.sin(np.pi * dist) * mask * strength
    return direction * dy * profile, -direction * dx * profile

# Populate the major Northern and Southern Hemisphere systems
# North Atlantic (Clockwise)
u, v = add_gyre(-40, 30, 45, 20, strength=2.5, clockwise=True)
U += u; V += v
# South Atlantic (Counter-Clockwise)
u, v = add_gyre(-20, -25, 40, 20, strength=2.2, clockwise=False)
U += u; V += v
# North Pacific (Clockwise)
u, v = add_gyre(160, 35, 65, 20, strength=2.8, clockwise=True)
U += u; V += v
u, v = add_gyre(-140, 35, 55, 20, strength=2.8, clockwise=True)
U += u; V += v
# South Pacific (Counter-Clockwise)
u, v = add_gyre(-120, -30, 65, 25, strength=2.5, clockwise=False)
U += u; V += v
u, v = add_gyre(160, -30, 55, 25, strength=2.5, clockwise=False)
U += u; V += v
# Indian Ocean (Counter-Clockwise)
u, v = add_gyre(80, -25, 45, 20, strength=2.4, clockwise=False)
U += u; V += v

# Add the Antarctic Circumpolar Current (ACC) belt
acc_mask = (Y > -65) & (Y < -45)
U += 3.5 * acc_mask
V += 0.4 * np.sin(X * np.pi / 45) * acc_mask  # Subtle wave pattern

# Add Equatorial Counter Current
U += 1.2 * ((Y > -2) & (Y < 5))

# Calculate velocity magnitudes for the streamline colormap
speed = np.sqrt(U**2 + V**2)

# Plotting the streamplot
fig, ax = plt.subplots(figsize=(14, 7), facecolor='#111111')
ax.set_facecolor('#111111')

strm = ax.streamplot(X, Y, U, V, color=speed, linewidth=1.2, cmap='YlGnBu', 
                     density=2.2, arrowstyle='->', arrowsize=1.0)

ax.set_title("Global Ocean Surface Currents Simulation (Streamplot)", color='white', fontsize=16)
ax.set_xlim(-180, 180)
ax.set_ylim(-80, 80)
plt.savefig('ocean_streamplot.png', dpi=300)
plt.show()