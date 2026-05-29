import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility of data generation
np.random.seed(42)

# 24 Hours array
hours = np.arange(24)

# Simulate generation behavior for Bhavnagar power sources over a 24-hour cycle
# Peak demand usually happens during the afternoon (12 PM - 4 PM) and evening (7 PM - 10 PM)

# 1. Solar: Peaks sharply in the middle of the day (10 AM to 4 PM), zero at night
solar = np.array([0, 0, 0, 0, 0, 0, 5, 25, 60, 110, 150, 180, 190, 185, 160, 115, 65, 20, 2, 0, 0, 0, 0, 0])

# 2. Wind: Stronger in coastal regions like Bhavnagar during late evening, early morning, and afternoon sea breezes
wind = np.array([75, 70, 68, 65, 60, 62, 68, 72, 75, 80, 85, 90, 95, 92, 88, 85, 82, 85, 90, 95, 92, 88, 82, 78])

# 3. Hydro: Used as a flexible "peaker" source to handle rapid demand spikes (e.g., morning routines and evening peaks)
hydro = np.array([10, 10, 10, 10, 12, 25, 40, 35, 30, 25, 20, 20, 25, 30, 25, 25, 30, 45, 55, 50, 40, 30, 20, 15])

# 4. Coal (Baseload): Runs consistently to provide steady foundation power, ramping up slightly for evening peaks when solar drops
coal = np.array([150, 145, 142, 140, 145, 160, 180, 190, 195, 190, 185, 185, 190, 195, 195, 200, 210, 230, 240, 235, 220, 200, 180, 165])

# Stack the data for plotting
y = np.vstack([coal, solar, wind, hydro])

# Define descriptive color palette
# Dark grey/black for coal, bright yellow for solar, light blue/cyan for wind, deep blue for hydro
colors = ['#4A4A4A', '#FFD700', '#87CEEB', '#1F77B4']
labels = ['Coal (Baseload)', 'Solar Power', 'Wind Energy', 'Hydroelectric']

# Plotting
plt.figure(figsize=(12, 7))
plt.stackplot(hours, y, labels=labels, colors=colors, alpha=0.85)

# Formatting axes and labels
plt.title("Bhavnagar Hourly Electricity Consumption Profile (24-Hour Cycle)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Hour of the Day (00:00 to 23:00)", fontsize=11, labelpad=10)
plt.ylabel("Electricity Consumption / Generation (MW)", fontsize=11, labelpad=10)

plt.xticks(hours, [f"{h:02d}:00" for h in hours], rotation=45)
plt.xlim(0, 23)
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Placing legend neatly outside to prevent overlap
plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title="Energy Sources", frameon=True)

plt.tight_layout()
plt.show()
