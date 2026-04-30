#create methods deposit and withdrawal rupees from bank account
balance = 1000
def deposit(amount):
    global balance 
    if amount<0:
        print("amount can not be < 0")
    else:
        balance = balance + amount 
        print("balance increased successfully")

def withdrawal(amount):
    global balance 
    if amount>0:
        print("amount can not be > 0") 
    else:
        balance = balance + amount 
        print("balance deducted successfully")