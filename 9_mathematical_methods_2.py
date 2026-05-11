import pandas as pd 

marks = [65,50,75,45,80]

#create series
s1 = pd.Series(marks)

print(s1)

print("add 1 into each value",s1.add(1))
print("subtract 3 into each value",s1.sub(3))
print("multiply each value by 3 ",s1.mul(3))
print("divide each value by 3 ",s1.div(3))

print(s1.pow(2))
print("Sum of all values ",s1.sum())
print("mean value ",s1.mean())
print("median of all the values ",s1.median())



