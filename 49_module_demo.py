#import converter module
import converter as c 
#here c as alias that you can use instead of converter 
foot = float(input("Enter value in foot: "))
meter = float(input("Enter value in meter: "))
cm = float(input("Enter value in centimeter: "))
inch = c.cmToInch(cm) #this will call cmToInch function of converter module 
print(f"{cm} inch to {inch}")
inch = c.footToInch(foot)
print(f"{foot} foot to {inch}")
inch = c.meterToInch(meter)
print(f"{meter} meter to {inch}")
