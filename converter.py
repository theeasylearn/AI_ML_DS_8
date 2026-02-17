#create converter functions for measurement units 
#foot in inch
def footToInch(foot):
    #here inch is local variable 
    inch = foot * 12 
    return inch  
#meter to inch 
def meterToInch(meter):
    #here inch is local variable 
    inch = meter * 39.37
    return inch 
#cm to inch 
def cmToInch(cm):
    #here inch is local variable 
    inch = cm / 2.54
    return inch 

print("i am module, ready to run..")