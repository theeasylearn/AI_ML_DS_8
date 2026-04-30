class Bank:
    #create constructor
    def __init__(self,name,acctype,balance):
        self.name = name
        self.acctype = acctype
        self.balance = balance 
        self.accno = 1
    def display(self):
        print("Account Holder name",self.name)
        print("Account type ",self.acctype)
        print("Account No",self.accno)
        print("Balance ",self.balance)
    def updateBalance(self,amount):
        self.balance = self.balance + amount 
        print("Balance updated successfully")


#create 
name = input("Enter account holder name")
acctype = input("Account type")
balance = int(input("Account balance"))
b1 = Bank(name,acctype,balance)
b1.display()
amount = int(input("Enter transaction amount"))
b1.updateBalance(amount)
b1.display()

#task - convert this example into menu driven program  Press 1 to create account, Press 2 update balance , Press 3 display program should continue to run untill use press 0