class KB:
    #create constructor
    def __init__(self,bytes):
        #create instance variable
        self.bytes = bytes
        print("constructor called.")

    def getKB(self):
        #create local variable
        kb = self.bytes / 1024
        return kb
# derived class as it extends/inherit MB class
class MB(KB):
    def __init__(self, bytes):
        super().__init__(bytes) #parent class constructor 
        print("MB class constructor called...")
    def getMB(self):
        mb = super().getKB() / 1024
        return mb 
    
class GB(MB):
    def __init__(self, bytes):
        super().__init__(bytes) #parent class constructor 
        print("GB class constructor called...")
    def getGB(self):
        gb = super().getMB() / 1024
        return gb 
    
#create object 
#OBJECT = CLASSNAME()
bytes = int(input("Enter bytes "))
# k1 = KB(bytes) #constructor will be run automatically
# kb = k1.getKB()
# print(f"kilobytes = {kb:.2f}")

g1 = GB(bytes)
gb = g1.getGB()
print(f"giga bytes = {gb:.2f}")