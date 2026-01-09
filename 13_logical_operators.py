#concept of logical operators in python 
num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))
num3 = int(input("Enter num 3")) 

# True   True     and       True  
result = num1 < num2 and num2 < num3 
print(f"{result} = {num1} < {num2} and {num2} < {num3}")
# True   True     and       False  
result = num1 < num2 or num2 > num3 
print(f"{result} = {num1} < {num2} or {num2} > {num3} ")
#        10 > 20  or    20 > 30    

#False =   False  or   False
result = num1 > num2 or num2 > num3 
print(f"{result} = {num1} > {num2} or {num2} > {num3} ")