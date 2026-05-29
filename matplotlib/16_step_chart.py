import matplotlib.pyplot as plt 
import numpy as np 
price = [
    26.07,  # 2000
    28.75,  # 2001
    26.66,  # 2002
    29.93,  # 2003
    33.71,  # 2004
    37.84,  # 2005
    43.49,  # 2006
    42.85,  # 2007
    45.52,  # 2008
    40.62,  # 2009
    44.63,  # 2010
    58.37,  # 2011
    65.64,  # 2012
    67.26,  # 2013
    72.43,  # 2014
    61.33,  # 2015
    59.35,  # 2016
    70.60,  # 2017
    69.97,  # 2018
    68.29,  # 2019
    75.14,  # 2020
    83.71,  # 2021
    95.41,  # 2022
    96.72,  # 2023
    104.24, # 2024
    103.94  # 2025
]
years = list(range(2000,2026))

plt.figure(figsize=(18,12))

plt.step(years,price,where='pre',color='blue',)
plt.xticks(ticks=years,labels=years)
plt.xlabel('years')
plt.ylabel('price')
plt.title("Petrol price in last 25 years")
plt.legend(['petrol price'])
plt.grid()
plt.show()


