class Bank:
    #Class Variable
    NextAccountNo = 1
    #create constructor
    def __init__(self,name,acctype,balance):
        self.name = name
        self.acctype = acctype
        self.balance = balance 
        self.accno = Bank.NextAccountNo
        Bank.NextAccountNo= Bank.NextAccountNo + 1 #increase NextAccountNo by 1
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


name = input("Enter account holder name")
acctype = input("Account type")
balance = int(input("Account balance"))
b2 = Bank(name,acctype,balance)
b2.display()

name = input("Enter account holder name")
acctype = input("Account type")
balance = int(input("Account balance"))
b3 = Bank(name,acctype,balance)
b3.display()

