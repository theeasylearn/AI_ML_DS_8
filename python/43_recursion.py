#concept of recursion 
# write a program to display 1 to 10 in reverse order 
def reverse(number):
    if number<10:
        number= number + 1
        reverse(number) #function reverse call it self (reverse) recursion
        print(number)
    
reverse(0)