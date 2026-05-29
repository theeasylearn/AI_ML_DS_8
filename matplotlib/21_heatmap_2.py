import matplotlib.pyplot as plt 
import numpy as np 

# 1. Clean up variable names (avoid using the built-in 'list' keyword)
temperatures_matrix = [
    # 1. Ahmedabad (Intense inland summer heat)
    [38.5, 39.0, 38.8, 39.2, 40.1, 40.5, 41.0, 41.2, 40.8, 41.5, 42.0, 42.3, 41.9, 42.1, 42.6, 43.0, 43.2, 42.8, 43.5, 44.1, 43.8, 44.0, 44.2, 44.5, 44.8, 45.0, 44.6, 43.9, 43.2, 42.5],
    # 2. Surat (Humid, coastal moderated)
    [34.2, 34.5, 34.8, 35.0, 35.2, 35.6, 36.0, 35.8, 36.1, 36.4, 36.8, 37.0, 36.9, 37.2, 37.5, 37.8, 38.0, 37.6, 37.9, 38.2, 38.5, 38.1, 38.3, 38.6, 38.9, 39.0, 38.7, 38.2, 37.8, 37.4],
    # 3. Vadodara (Central plain heat)
    [37.8, 38.2, 38.5, 38.9, 39.4, 39.8, 40.2, 40.5, 40.1, 40.7, 41.2, 41.5, 41.1, 41.4, 42.0, 42.3, 42.5, 42.1, 42.6, 43.2, 42.9, 43.1, 43.4, 43.7, 44.0, 44.2, 43.8, 43.1, 42.5, 41.8],
    # 4. Rajkot (Semi-arid Saurashtra heat)
    [39.0, 39.4, 39.2, 39.7, 40.5, 41.0, 41.4, 41.6, 41.2, 41.9, 42.4, 42.7, 42.3, 42.6, 43.1, 43.5, 43.8, 43.3, 44.0, 44.6, 44.2, 44.5, 44.8, 45.1, 45.3, 45.5, 45.0, 44.2, 43.6, 42.9],
    # 5. Bhavnagar (Coastal Saurashtra, balanced)
    [36.0, 36.4, 36.2, 36.7, 37.3, 37.8, 38.2, 38.4, 38.0, 38.6, 39.1, 39.4, 39.0, 39.3, 39.8, 40.2, 40.5, 40.1, 40.6, 41.2, 40.9, 41.1, 41.4, 41.7, 42.0, 42.2, 41.8, 41.1, 40.5, 39.8],
    # 6. Jamnagar (Near-coastal breeze influence)
    [35.1, 35.5, 35.3, 35.8, 36.4, 36.9, 37.3, 37.5, 37.1, 37.7, 38.2, 38.5, 38.1, 38.4, 38.9, 39.3, 39.6, 39.2, 39.7, 40.3, 40.0, 40.2, 40.5, 40.8, 41.1, 41.3, 40.9, 40.2, 39.6, 38.9],
    # 7. Bhuj (Arid Kutch, drastic desert day-peaks)
    [39.5, 40.0, 39.8, 40.3, 41.2, 41.8, 42.2, 42.4, 42.0, 42.7, 43.2, 43.5, 43.1, 43.4, 44.0, 44.4, 44.7, 44.2, 45.0, 45.6, 45.2, 45.5, 45.8, 46.1, 46.4, 46.6, 46.1, 45.3, 44.7, 43.9],
    # 8. Gandhinagar (Similar to Ahmedabad)
    [38.3, 38.8, 38.6, 39.0, 39.9, 40.3, 40.8, 41.0, 40.6, 41.3, 41.8, 42.1, 41.7, 41.9, 42.4, 42.8, 43.0, 42.6, 43.3, 43.9, 43.6, 43.8, 44.0, 44.3, 44.6, 44.8, 44.4, 43.7, 43.0, 42.3],
    # 9. Junagadh (Saurashtra foothills context)
    [37.2, 37.6, 37.4, 37.9, 38.5, 39.0, 39.4, 39.6, 39.2, 39.8, 40.3, 40.6, 40.2, 40.5, 41.0, 41.4, 41.7, 41.3, 41.8, 42.4, 42.1, 42.3, 42.6, 42.9, 43.2, 43.4, 43.0, 42.3, 41.7, 41.0],
    # 10. Dwarka (Low coastal peninsular strip)
    [31.5, 31.8, 32.0, 32.3, 32.5, 32.8, 33.1, 32.9, 33.2, 33.5, 33.8, 34.0, 33.9, 34.1, 34.4, 34.7, 35.0, 34.6, 34.9, 35.2, 35.5, 35.1, 35.3, 35.6, 35.9, 36.0, 35.7, 35.2, 34.8, 34.4]
]

cities_list = ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Bhuj", "Gandhinagar", "Junagadh", "Dwarka"]
array_2d = np.array(temperatures_matrix)

# 2. Adjust figure canvas and aspect ratio for wide 30-day datasets
plt.figure(figsize=(16, 7))

# 3. Swap colormap to thermal 'YlOrRd' (Yellow-Orange-Red) for climate context
# aspect='auto' prevents cells from distorting into compressed tall blocks
im = plt.imshow(array_2d, cmap='YlOrRd', interpolation='nearest', aspect='auto')

# 4. Apply clean labels, titles, and appropriate padding
plt.xlabel('Days of April 2026', fontsize=12, labelpad=12)
plt.ylabel('Cities', fontsize=12, labelpad=12)
plt.title('Daily Max Temperatures Across 10 Cities in Gujarat (April 2026)', fontsize=14, pad=15, fontweight='bold')

# 5. Correct the 0-indexed tick alignment mapping
plt.xticks(ticks=np.arange(30), labels=np.arange(1, 31), fontsize=10)
plt.yticks(ticks=np.arange(10), labels=cities_list, fontsize=11)

# 7. Structure the colorbar legend cleanly
cbar = plt.colorbar(im, pad=0.02)
cbar.set_label('Temperature (°C)', rotation=270, labelpad=18, fontsize=11)
plt.show()