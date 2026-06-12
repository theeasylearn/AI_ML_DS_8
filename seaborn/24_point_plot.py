from vega_datasets import data 
import seaborn as sns 
import matplotlib.pyplot as plt 
#load income dataset
cars = data.cars()
print(cars)

#create swarm plot 
sns.pointplot(data=cars,y='Miles_per_Gallon',x='Cylinders',estimator='mean',hue='Origin')
plt.xlabel('Cylinders')
plt.ylabel('Miles per gallon')
plt.grid(which='both')
plt.show()