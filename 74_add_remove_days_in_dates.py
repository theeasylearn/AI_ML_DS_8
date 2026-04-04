from datetime import datetime as dt 
from datetime import timedelta 
import math 
recharge_date = input("Enter your mobile recharge date (%d/%m/%Y)")
print(recharge_date)
date1 = None
try:
    #convert string recharge_date into date type recharge_date
    date1 = dt.strptime(recharge_date,"%d/%m/%Y")
    days = input("Enter recharge validity in days")
    no_of_days = int(days)
    # no_of_days = math.fabs(no_of_days) #converting negative value into positive 
    #add days into recharge_date to get recharge expiry date 
    td = timedelta(days=no_of_days)
    date1 = date1.__add__(td) #add unit of timedelta object (days) and return new datetime object
    print("recharge expiry date",date1)
except ValueError as error:
    print("invalid format in inputted date. format must be %d/%m/%Y")
finally:
    print("good bye.")
