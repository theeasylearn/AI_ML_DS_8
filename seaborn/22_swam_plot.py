from vega_datasets import data 
import seaborn as sns 
import matplotlib.pyplot as plt 
#list all dataset in vega 
# list = data.list_datasets() # return list of all dataset 
# for dataset in list:
#     print(dataset)

#load income dataset
cars = data.cars()
print(cars)

#create swarm plot 
sns.swarmplot(data=cars,y='Miles_per_Gallon',x='Cylinders',hue='Origin',size=4)
plt.xlabel('Cylinders')
plt.ylabel('Miles per gallon')
plt.grid(which='both')
plt.show()