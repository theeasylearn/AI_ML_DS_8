import matplotlib.pyplot as plt 
import seaborn as sns 
from vega_datasets import data 
#load income flights_200k

cars = data.cars()
sns.jointplot(data=cars,x='Cylinders',y='Miles_per_Gallon',kind='reg')
plt.show()
