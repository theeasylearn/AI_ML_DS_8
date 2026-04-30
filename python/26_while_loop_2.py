# example of while loop 
# 1 -4  9  -16 25 -36 49 -64 ..... 400 

number = 1
square = 0
while number<21: # == != < > <= >=
    square = number * number #1
    reminder = number % 2 # 1
    if reminder==0: #even
        square = 0 - square
    print(square,end=' ')
    number = number + 1 #2



