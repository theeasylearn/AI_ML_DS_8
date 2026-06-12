# pip install vega_datasets 
from  vega_datasets import data 
import matplotlib.pyplot as plt 
import seaborn as sns 
# print(data.list_datasets()) 
df = data.cars()
# print(df)   Name  Miles_per_Gallon  Cylinders  ...  Acceleration       Year  Origin
plt.figure(figsize=(2,2),dpi=50)
sns.pairplot(data=df,diag_kind='kde')
plt.show()