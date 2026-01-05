# example of list
# ctrl+/ is shortcut key for comments
# name = "gautam"
# print(name) #gautam
# name = "dhruvil"
# print(name)
# name = "raees"
# print(name)
#normal variable can store at a time only single value
# //create list
names = ["kahan","darshil","raees","ayan","gautam","dharmik","dhruvil"]
dishes = ['pulav','pav bhaji','dosa']

print(names)
print(names[0]) #print 0th value in list kahan
print(names[1]) #print 1th value in list darshil
print(names[4]) #print 4th value in list gautam
print(names[5]) #print 5th value in list dharmik
# print(names[8]) #error because list has no 8th position
print(names[0:2]) #print 2 items from begining 
#always remember that when use two value with slice operator value after : is not including
#print 2rd to 4th item 
print(names[2:5]) # raees ayan gautam
#print all items from 4th items
print(names[4:]) #"gautam","dharmik","dhruvil"
#it will print name list 5 times
print(names*5)
print(names+dishes)