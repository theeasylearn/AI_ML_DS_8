import matplotlib.pyplot as plt 
import numpy as np 
#create data 
# y axis 
sales_lakhs = [164.56, 175.90, 202.00, 211.80, 174.16, 151.21, 134.66, 158.62, 179.74, 196.07, 217.00]

sales_lakhs = np.array(sales_lakhs)
#x axis 
years = np.arange(2015,2026)
# print(len(sales_lakhs),len(years))

plt.bar(years,sales_lakhs,align='edge',width=0.6,color='orange')

plt.xlabel('years')
plt.xticks(ticks=range(2015,2026))
plt.ylabel('sales in lakhs')
plt.title("2 wheel sales in lakhs between 2015 to 2025")
plt.show()
