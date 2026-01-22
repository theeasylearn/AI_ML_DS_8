#write a program to convert given amount into words 
# input : 12345
# output : one two three four five 
list = [] #empty list
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
#          0      1    2       3       4   5       6       7       8       9     
number = int(input("Enter amount")) #12345

while number>0:
    reminder = number % 10 #5
    list.insert(0,words[reminder])
    number = number // 10 # 1234

print(' '.join(list))
