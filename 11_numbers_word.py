#write a program to convert 2 digit amount into words
#input : 45
#output : four five 
#task fourty five 
numbers = input("Enter 2 digit amount")
#convert into integer  because input is always string and we can do mathematical operation on string
numbers = int(numbers)
#assume input is 83
last = numbers % 10 #3
# print(last)

#get first digit 
first = numbers // 10 #8
# print(first)
words = ['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine']
print(words[first],words[last] ) #eight three