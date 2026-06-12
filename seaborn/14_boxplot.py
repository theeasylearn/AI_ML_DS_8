import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

# Load dataset 
olympic = pd.read_csv('olympic.csv')

# Set chart dimension using recommended subplots method
fig, ax = plt.subplots(figsize=(12, 6))

# Create chart: X is categorical (Country), Y is numerical (Gold)
sns.boxplot(x='Country', y='Gold', data=olympic, ax=ax, palette='Set1')

# Set labels precisely matching the axes
ax.set_xlabel('Country', fontsize=12)
ax.set_ylabel('Gold Medals Won', fontsize=12)
ax.set_title('Distribution of Gold Medals by Country (2004–2024)', fontsize=14, fontweight='bold')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()