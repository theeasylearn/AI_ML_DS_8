# example of lambda function 
# create function which calculate and return simple interest amount of given amount, rate & year 
# def getInterest(amount,rate,year):
#     interest = (amount * rate * year) / 100
#     return interest
#  or 
getInterest = lambda amount,rate,year : (amount * rate * year) / 100

amount = float(input("Enter amount: "))
rate = float(input("Enter rate: "))
year = float(input("Enter year: "))

interest = getInterest(amount,rate,year) #function call
print("simple interest amount ",interest)