# write a program to find out whether given year is leap year or not.
year = int(input("Enter year to check is this leap year or not ")) # 2024
if year<=0:
    print("invalid year")
else:
    reminder1 = year % 4 # 0
    reminder2 = year % 100 # 24
    reminder3 = year % 400 # 24
    if reminder1==0 and reminder2!=0:
        print("given year is leap year")
    else:
        if reminder2==0 and reminder3==0:
            print("given year is leap year")
        else:
            print("given year is not leap year")