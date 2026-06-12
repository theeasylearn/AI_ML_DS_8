import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np 

#load data 
covid = pd.read_csv('covid_death.csv').squeeze()
sns.ecdfplot(data=covid,x='age',color='blue')
plt.xlabel('age')
plt.ylabel('')
plt.title('ecdf chart')
plt.tight_layout()
plt.show()