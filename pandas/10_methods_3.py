import pandas as pd 

s1 = pd.Series([1,2,2,3,3,4,5,6,None,None])
print(s1)

print("Most Frequent value\n",s1.mode())
print("Standard Deviation \n",s1.std())
print("Standard Variance \n",s1.var())
print("Total valid value(not null and not NAN values) \n",s1.count())
print("Total value \n",len(s1))
print("is null",s1.isnull())
print("replace null value with 0 ",s1.fillna(0))
print("drop null value ",s1.dropna())
