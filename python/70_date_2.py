#write a program to findout elder person from given 2 person birth date

import datetime as dt 
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



