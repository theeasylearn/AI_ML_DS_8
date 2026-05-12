import pandas as pd 

#display current version of pandas
print(pd.__version__)  #__version__ is called properties 

#create Series (Series means one dimensional list)

#python list
runs = [0, 35, 55, 69, 29, 38]

#create Series using list 
s1 = pd.Series(runs,index=["Salil Arora", "Abhishek Sharma", "Ishan Kishan", "Heinrich Klaasen", "Nitish Kumar Reddy", "Travis Head"])
print(s1)

#create Series of 7 cities of gujarat on 06-may-2026
s2 = pd.Series([42.3, 41.0, 41.0, 39.0, 38.5, 38.0, 35.0],index=["Rajkot", "Surendranagar", "Kandla", "Ahmedabad", "Gandhinagar", "Bhavnagar", "Surat"])
print(s2)
