#import bank module 
import bank 

print("Balance before deposit",bank.balance)
amount = int(input("Enter how many rupees you want to deposit"))
bank.deposit(amount)
print("Balance after deposit ",bank.balance)
amount = int(input("Enter how many rupees you want to withdraw"))
bank.withdrawal(amount)
print("Balance after withdrawal ",bank.balance)

