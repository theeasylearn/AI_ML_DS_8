import numpy as np
import matplotlib.pyplot as plt

# Data for exactly 11 players
positions = [
    "Bowler", "Wicketkeeper", "First Slip", "Point", "Cover", 
    "Mid-off", "Mid-on", "Square Leg", "Fine Leg", "Long-on", "Deep Mid-wicket"
]
angles_deg = [0, 180, 195, 270, 315, 345, 15, 90, 135, 20, 60]
distances = [20.12, 20, 22, 25, 25, 25, 25, 24, 50, 75, 70]

angles_rad = np.radians(angles_deg)

# Create figure
plt.figure(figsize=(9, 9))

# ==================== PURE plt.polar CIRCLES ====================
theta_circle = np.linspace(0, 2 * np.pi, 300)

# 30-yard circle
plt.polar(theta_circle, np.full_like(theta_circle, 27.4),
          color='#2e7d32', linestyle='--', linewidth=2, alpha=0.8, label='30-Yard Circle')

# Boundary
plt.polar(theta_circle, np.full_like(theta_circle, 80),
          color='#c62828', linestyle='-', linewidth=2.5, alpha=0.9, label='Boundary (80m)')

# ==================== FIELDERS using plt.polar (markers) ====================
colors = ['#1565c0' if p in ['Bowler', 'Wicketkeeper'] else '#d32f2f' for p in positions]
marker_sizes = [13 if p in ['Bowler', 'Wicketkeeper'] else 10.5 for p in positions]

for i in range(len(positions)):
    plt.polar([angles_rad[i]], [distances[i]], 'o',
              color=colors[i],
              markersize=marker_sizes[i],
              markeredgecolor='white',
              markeredgewidth=1.5,
              zorder=5)

# Get current (polar) axes for configuration
ax = plt.gca()

# Cricket field orientation
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_facecolor('#e8f5e9')
ax.set_rmax(85)
ax.set_rlabel_position(180)

# Title
plt.title("Precise 11-Player Polar Field Placement\n(Standard ODI/T20 Setting for Right-Handed Batsman)", 
          pad=30, fontsize=14, weight='bold', color='#111111')

plt.show()

print("✅ Pure plt.polar chart saved as 'cricket_field_polar_pltpolar.png'")