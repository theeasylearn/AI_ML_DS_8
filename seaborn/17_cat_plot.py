# pip install vega_datasets 
from  vega_datasets import data 
import matplotlib.pyplot as plt 
import seaborn as sns 
# print(data.list_datasets()) 
cars = data.cars()
print(cars)

sns.catplot(x='Cylinders',y='Miles_per_Gallon',data=cars,kind='bar')
plt.title("Card milage data")
plt.xlabel("Cylinder")
plt.ylabel('Miles per Gallon')
plt.show()
