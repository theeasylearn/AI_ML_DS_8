#concept of relational operators 
num1 = int(input("Enter value for num 1"))
num2 = int(input("Enter value for num 2"))

#relational expression has variables/value and reational operators 
result = num1 == num2 
print(f"{result} = {num1} == {num2}")

result = num1 != num2 #True 
print(f"{result} = {num1} != {num2}")

result = num1 < num2 #True 
print(f"{result} = {num1} < {num2}")

result = num1 > num2 #False 
print(f"{result} = {num1} > {num2}")

result = num1 <= num2 #True 
print(f"{result} = {num1} <= {num2}")

result = num1 >= num2 #False 
print(f"{result} = {num1} >= {num2}")