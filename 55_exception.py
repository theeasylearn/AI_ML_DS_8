# write a program to handle custom exception using Custom Exception using class 
#define custom exception using class keyword 
class NegativeInput(Exception):
    pass 
try:
    amount = int(input("Enter principal amount"))
    rate = float(input("Enter interest rate"))
    year = int(input("Enter duration in (year)"))
    if amount<0 or rate<0 or year<0:
        raise NegativeInput #raising custom exception NegativeInput
    #calculate simple interest 
    interest = (amount * rate * year) / 100
except ValueError:
    print("invalid input, only digits are allowed")
except NegativeInput:
    print("amount, rate, year must be only positive numeric input ")
else:
    print(f"simple interest = {interest}")
finally:
    print("thank you for using our program")