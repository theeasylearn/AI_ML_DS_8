import math as m  #import math module and assign alias(nick name) m 
# convert each element into positive value using lambda function
my_list = [-45, 12, 78, -3, 0, 56, -89, 34, -21, 67, 5, -14, 92, -76, 18, -9, 41, -60, 23, -2]
list2 = [] #empty list
# for number in my_list:
#     if number<0:
#         number = 0 - number
#     list2.append(number)
positive_iterable = map(lambda number: m.fabs(number),my_list)
print(list(positive_iterable))