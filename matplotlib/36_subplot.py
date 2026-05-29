import matplotlib.pyplot as plt 
import numpy as np 

#display infloation in last 10 year 
# Order of years: 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
inflation_rates = [4.95, 3.33, 3.94, 3.73, 6.62, 5.13, 6.70, 5.65, 4.95, 4.60]
# Order of years: 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
growth_rates = [8.26, 6.80, 6.45, 3.87, -5.78, 9.69, 6.99, 8.15, 8.20, 7.60]
years = np.arange(2016,2026)
# print(years)
plt.figure(figsize=(12,8))
#create 1st chart
# 1 = no of total rows ,2 = no of total columns ,1 = chart position (index)
plt.subplot(1,2,1)
plt.plot(years,inflation_rates,color='red',label='inflation')
plt.title('inflation rate')
plt.xticks(ticks=years)
plt.xlabel('year')
plt.ylabel('inflation rate')
plt.grid()
plt.legend()

#second chart
plt.subplot(1,2,2)
plt.bar(years,growth_rates,color='blue',label='growth rate')
plt.title('GDP growth rate')
plt.xticks(ticks=years)
plt.xlabel('year')
plt.ylabel('growth rate')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
