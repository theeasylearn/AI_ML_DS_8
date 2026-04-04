from datetime import datetime as dt 
birthdate = input("Enter your birth date (%d/%m/%Y)")
print(birthdate)
date1 = None
try:
#convert string birthdate into date type birthdate
    date1 = dt.strptime(birthdate,"%d/%m/%Y")
except ValueError as error:
    print("invalid format in inputted date. format must be %d/%m/%Y")
else:
    print(date1) #2022-12-29 00:00:00
    #display this date in us format
    print(dt.strftime(date1,"%m/%d/%Y"))
finally:
    print("good bye.")
