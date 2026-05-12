import pandas as pd 
runs = [0, 35, 55, 69, 29, 38]
#create Series using list 
s1 = pd.Series(runs,index=["Salil Arora", "Abhishek Sharma", "Ishan Kishan", "Heinrich Klaasen", "Nitish Kumar Reddy", "Travis Head"])
print(s1)

#1st 3 score
print(s1.head(3))

#last 3 score 
print(s1.tail(3))

#Series as list
print(s1.to_list())

#series as dictionary 
print(s1.to_dict())

print(s1.describe())

s2 = s1.astype(dtype="Int32")
print(s2)

