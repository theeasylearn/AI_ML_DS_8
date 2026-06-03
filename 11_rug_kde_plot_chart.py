import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

#load data 
covid = pd.read_csv('covid_death.csv').squeeze()
covid = covid.dropna(subset=['age'])
sns.rugplot(x='age',data=covid,height=0.2,color='blue')
sns.kdeplot(x='age',data=covid,color='orange')
plt.xlabel('age')
plt.title('rug plot')
plt.show()