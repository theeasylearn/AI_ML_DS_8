#write a program to findout elder person from given 2 person birth date and findout gap in year between person

import datetime as dt 
import math as mt 
print("Enter 1st person detail")
name = input("enter 1st person name")
print(f"Enter birth detail of {name}")
day = int(input("Enter day of your birthday"))
month = int(input("Enter month of your birth date"))
year = int(input("Enter year of your birth date"))

#create date object
birthdate_1 = dt.date(year,month,day)
print(birthdate_1)

print("Enter 2nd person detail")
name_2 = input("enter 2nd person name")
print(f"Enter birth detail of {name_2}")

day = int(input("Enter day of your birthday"))
month = int(input("Enter month of your birth date"))
year = int(input("Enter year of your birth date"))

#create date object
birthdate_2 = dt.date(year,month,day)
print(birthdate_2)

#compare date object
if birthdate_1<birthdate_2:
    print(f"{name} is elder then {name_2}")
else:
    print(f"{name_2} is elder then {name}")

#findout gap between (subtract any one date from other date)
gap = birthdate_1 - birthdate_2
print("gap between 2 person in days ",mt.fabs(gap.days))
years = mt.fabs(gap.days)//365
print("gap between 2 person in year ",years)


