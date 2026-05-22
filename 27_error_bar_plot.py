import numpy as np 
import matplotlib.pyplot as plt

players = ['Virat Kohli', 'Rohit Sharma', 'Shubman Gill', 'Shreyas Iyer']
means = [58.72, 48.84, 55.00, 46.00]
errors = [4.1, 4.8, 5.2, 5.5] 

# Initialize the plot layout
plt.figure(figsize=(8, 5), dpi=100)

# Create the vertical error bar chart
plt.errorbar(
    x=players,        # Categories go on the x-axis
    y=means,          # Numerical values go on the y-axis
    yerr=errors,      # Vertical error intervals match the y-axis numerical data
    fmt='o',
    color='blue', 
    ecolor='red', 
    elinewidth=2.5,
    capsize=6,
    markersize=9,
    label='Batting Average'
)

# Customizing axes and adding guidelines (Fixed plt.set_* typos)
plt.xlabel('Players', fontsize=11, labelpad=10)
plt.ylabel('Batting Average', fontsize=11, labelpad=10)
plt.title('Top Indian Batsmen: ODI Performance & Consistency', fontsize=13, pad=15, fontweight='bold')
plt.ylim(35, 70)

# Clean grid lines matching your vertical orientation (grid on Y-axis makes reading averages easier)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()