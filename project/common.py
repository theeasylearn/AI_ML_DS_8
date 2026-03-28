import os 
size = os.get_terminal_size()
column = size.columns
def PrintLine(letter='_',count=0):
    if count==0:
        count = column
    print(letter*count)

def PrintCenter(message):
    print(message.center(column))