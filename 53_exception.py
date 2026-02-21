# numbers = [17, 93,  4, 58, 71, 29, 86, 12, 65, 40, 3, 99, 24, 76, 51, 8, 62, 35, 90, 14]
import re
import ast
data = "[,17, 93, 'test', 4,,,,,,, 58, 71, None,29, 86, 12, 65, 40, 3, 99, 24, 76, 51, 8, 62, 35, 90, 14,]"
# data = "['test','exam']" #empty list
# 1. Remove leading comma after [
data = re.sub(r"\[\s*,+", "[", data)

# 2. Replace multiple commas with single comma
data = re.sub(r",\s*,+", ",", data)

# 3. Remove trailing comma before ]
data = re.sub(r",\s*\]", "]", data)

numbers = ast.literal_eval(data)
# print(numbers)
total = 0 
count = 0
for num in numbers:
    # print(num,end=' ')
    try:
        total += num # total = total + num
        count+=1 # count = count + 1
    except TypeError as e:
        print('invalid value',num, 'so it is skipped')
try:
    average = total / count 
except ZeroDivisionError as e:
    print("empty dataset/list")
else:
    print(f"total = {total} average = {average}")