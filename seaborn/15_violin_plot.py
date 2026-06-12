import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

marks = pd.read_csv('marks.csv').squeeze()
# print(marks)
sns.violinplot(x='Division',y='Mark',data=marks)

# # Set labels precisely matching the axes
plt.xlabel('Division', fontsize=12)
plt.ylabel('Marks', fontsize=12)
plt.yticks(ticks=list(range(40,100,5)))
plt.title('marks distribution in different division', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.grid(which='both')
plt.show()