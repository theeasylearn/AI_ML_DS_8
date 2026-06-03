import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

# 1. Load data 
data = {
    "Player": ["Virat Kohli", "Rohit Sharma", "KL Rahul"],
    "2022": [1, 0, 0],
    "2023": [6, 2, 2],
    "2024": [0, 0, 0],
    "2025": [3, 2, 0],
    "Total": [10, 4, 2]
}

df = pd.DataFrame(data)

# 2. Melt DataFrame to long format (excluding the 'Total' column for yearly breakdown)
df_melted = df.melt(id_vars='Player', value_vars=['2022', '2023', '2024', '2025'], 
                    var_name='Year', value_name='Centuries')

print(df_melted)

# Create the grouped bar chart
ax = sns.barplot(x='Year', y='Centuries', hue='Player', data=df_melted)

plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Number of Centuries', fontsize=12, fontweight='bold')
plt.title('Year-wise ODI Centuries Breakdown (2022-2025)', fontsize=14, fontweight='bold', pad=15)

plt.legend(title='Player', loc='upper right')
plt.ylim(0, 7)  # Generous headroom for the labels

plt.tight_layout()
plt.show()