#create date object using give day, month & year
import datetime as dt 

day = int(input("Enter day of your birthday"))
month = int(input("Enter month of your birth date"))
year = int(input("Enter year of your birth date"))

#create date object
birthdate = dt.date(year,month,day)
print(birthdate)
