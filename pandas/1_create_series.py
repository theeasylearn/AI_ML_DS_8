import pandas as pd 
import numpy as np 
#display current version of pandas
print(pd.__version__)  #__version__ is called properties 

#create Series (Series means one dimensional list)

#python list
runs = [0, 35, 55, 69, 29, 38]

#create Series using list 
s1 = pd.Series(runs)
print(s1)

#create Series of 7 cities of gujarat on 06-may-2026
s2 = pd.Series([42.3, 41.0, 41.0, 39.0, 38.5, 38.0, 35.0])
print(s2)

state_income = {"Sikkim": 677000, "Goa": 650000, "Delhi": 461000, "Telangana": 350000, "Karnataka": 330000, "Haryana": 325000, "Tamil Nadu": 315000, "Gujarat": 305000, "Maharashtra": 290000, "Kerala": 285000, "Andhra Pradesh": 245000, "Punjab": 200000, "Himachal Pradesh": 235000, "Mizoram": 220000, "Arunachal Pradesh": 215000, "Uttarakhand": 255000, "Rajasthan": 180000, "West Bengal": 165000, "Odisha": 175000, "Chhattisgarh": 155000, "Madhya Pradesh": 150000, "Assam": 130000, "Manipur": 105000, "Nagaland": 145000, "Meghalaya": 115000, "Tripura": 160000, "Jharkhand": 95000, "Uttar Pradesh": 90000, "Bihar": 60000}

#create Series from dictionary
s3 = pd.Series(state_income)
print(s3)

#create an array 
array1 = np.array([100,200,300,500,1000])

#create series 
s4 = pd.Series(array1,index=['A','B','C','D','E '],name='Income') 
print(s4)

