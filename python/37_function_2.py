import shutil
width = shutil.get_terminal_size().columns
# Without return value without argument
def printLine():
    print("_"*width)
# Without return value with argument
def printCenter(message):
    print(message.center(width))

# With return value without argument
def getPi():
    pi = 22/7
    #pi is local variable available to access only inside this function
    return pi 
printLine()
printCenter("the easylearn")
printLine()
#normal variable
pi = getPi()
print(f"pi = {pi}")
printLine()
print(getPi()) #we can call one function into another function