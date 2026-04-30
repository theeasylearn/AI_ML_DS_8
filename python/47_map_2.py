
list1 = [14, 27, 5, 63, 91]
list2 = [8, 46, 32, 19, 74]
#calculate sum of each value 
sum = map(lambda num1,num2: num1 + num2,list1,list2)

sum = list(sum)
print(sum)
