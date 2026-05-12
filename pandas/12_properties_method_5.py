import pandas as pd 
gujarat_cities = {
    "ahmedabad": 380001,
    "surat": 395003,
    "vadodara": 390001,
    "rajkot": 360001,
    "bhavnagar": 364001,
    "jamnagar": 361001,
    "gandhinagar": 382010,
    "junagadh": 362001,
    "anand": 388001,
    "navsari": 396445
}
#create series using dictionary
s1 = pd.Series(gujarat_cities,name='pincode list')
print(s1)
print(s1.loc['bhavnagar'])
print(s1.loc['vadodara'])
# print(s1.loc['bhuj']) #error because key does not exists
print(s1.iloc[1])
print(s1.iloc[2])
print(s1.get('anand'))
print(s1.get('bhavnagar'))
print(s1.get('pune'))