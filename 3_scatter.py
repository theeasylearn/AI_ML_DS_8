import matplotlib.pyplot as plt 
import seaborn as sns 

#load dataset 
titanic = sns.load_dataset("titanic")
print(titanic)
sns.scatterplot(x='age',y='fare',data=titanic,hue='pclass')
plt.show()