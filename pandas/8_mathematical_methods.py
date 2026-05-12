import pandas as pd 

runs = [-1, 35, 55, 69, 29, 38]
#create Series using list 
s1 = pd.Series(runs,index=["Salil Arora", "Abhishek Sharma", "Ishan Kishan", "Heinrich Klaasen", "Nitish Kumar Reddy", "Travis Head"])
print(s1)

print(s1.abs()) 

#get minimum value
print(s1.min())


#get maximum value
print(s1.max())


#get label of minimum value 
print(s1.idxmin())

#get lable of maximum value
print(s1.idxmax())

#get size of the Series
print(len(s1),"or you can use size ", s1.size)

#sort the value in a to z order
print(s1.sort_values())

#sort the index in a to z order
print(s1.sort_index())

