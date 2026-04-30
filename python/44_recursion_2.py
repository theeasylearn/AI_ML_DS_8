#write a program to convert decimal number into binary number
def toBinary(number):
    reminder = 0 #local variable 
    if number>0:
        reminder = number % 2 # 1
        number = number // 2 #8
        toBinary(number) #recursion
        print(reminder,end='')
number = int(input("Enter number"))
#call function 
toBinary(number) #1st call


