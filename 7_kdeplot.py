import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np 

#load data 
covid = pd.read_csv('covid_death.csv').squeeze()

# Fetch data and isolate the last 30 completed working days
plt.figure(figsize=(20,12))
sns.kdeplot(x='age',data=covid,hue='Sex',alpha=0.5,fill=True)
plt.xlabel('age')
plt.ylabel('no of deaths')
plt.title('Age &gender wise death in covid 19')
plt.tight_layout()
plt.show()