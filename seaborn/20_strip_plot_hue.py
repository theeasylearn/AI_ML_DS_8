# pip install vega_datasets 
from vega_datasets  import data 
import matplotlib.pyplot as plt 
import seaborn as sns 

#load dataset 
cars = data.cars()
print(type(cars))
print(cars)
sns.stripplot(data=cars,x='Cylinders',y='Miles_per_Gallon',hue='Origin')
plt.xlabel('Cylinders')
plt.ylabel("Miles Per gallon")
plt.title("Cars miliege by cylinders")
plt.grid(which='both')
plt.legend()
plt.show()