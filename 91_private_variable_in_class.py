class Account:
    def __init__(self,name,balance):
        #create private instance variable
        self.__balance = balance 

        self.name = name 
    def display(self):
        print("Name ",self.name)
        print("Balance ",self.__balance)


a1 = Account('Darshil Joshi',1000)
a1.display()
a1.__balance = 0  #this line will be ignored by interpreter because __balanace is private variable
a1.display()



