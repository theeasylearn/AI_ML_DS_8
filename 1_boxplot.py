import matplotlib.pyplot as plt 
import seaborn as sns 

#load dataset 
tips = sns.load_dataset("tips")
print(tips)
sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()