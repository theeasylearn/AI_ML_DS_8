def getInches(meter,foot=0,inch=0):
    print(f"meter = {meter}, foot = {foot} , inch = {inch}")
    #calculate and return total inches of given meter,foot,inch
    totalInch = (meter * 3.28 * 12) + (foot * 12) + inch
    return totalInch

meter = 3 
foot = 4
inch = 6
totalInch = getInches(meter,foot,inch)
print(f" total inches = {totalInch}")

totalInch = getInches(meter,foot)
print(f" total inches = {totalInch}")

totalInch = getInches(meter)
print(f" total inches = {totalInch}")
