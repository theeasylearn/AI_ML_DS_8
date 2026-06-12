import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

#load dataset 
covid = pd.read_csv('covid_death.csv').squeeze()

#set chart dimension 
plt.figure(figsize=(18,10))

#create chart 
sns.countplot(x='Sex',data=covid,)
plt.xlabel('States')
plt.ylabel('Death Count')
plt.title("State wise covid 19 death count")
plt.show()