import shutil
width = shutil.get_terminal_size().columns
# Without return value without argument
def printLine():
    print("_"*width)
# Without return value with argument
def printCenter(message):
    print(message.center(width))

# With return value without argument

printLine()
printCenter("the easylearn")
printLine()