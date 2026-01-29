#create user defined function 
#def function-name():
# With return value with argument 
def getSquare(number):
    #function body 
    square = number * number 
    #here square is local variable
    #local variable means variable created inside function, such variable only available inside function in which it is created 
    return square
def getQube(num):
    #function body 
    qube = getSquare(num) * num 
    #here qube is local variable 
    return qube 

#normal variable
n1 = int(input("Enter number"))
result = getSquare(n1) #function run/call/execute
print('square is ',result) #will execute only after getSquare function finish (synchronous calling)
result2 = getQube(n1) #function run/call/execute
print('Qube is ',result2) 