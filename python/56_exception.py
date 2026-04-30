# write a program to handle custom exception using Custom Exception using class 
#define custom exception using class keyword 
class NegativeInput(Exception):
    pass 
try:
    amount = int(input("Enter principal amount"))
    rate = float(input("Enter interest rate"))
    year = int(input("Enter duration in (year)"))
    if amount<0:
        raise NegativeInput("amount can not be given less then 0") #raising custom exception NegativeInput with error message
    if rate<0:
        raise NegativeInput("rate can not be given less then 0")
    if year<0:
        raise NegativeInput("year can not be given less then 0")
    #calculate simple interest 
    interest = (amount * rate * year) / 100
except ValueError:
    print("invalid input, only digits are allowed")
except NegativeInput as error:
    print(error)
else:
    print(f"simple interest = {interest}")
finally:
    print("thank you for using our program")