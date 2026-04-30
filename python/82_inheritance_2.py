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
    
class MB(KB):
    def __init__(self, bytes):
        super().__init__(bytes) #parent class constructor 
        print("MB class constructor called...")
    def getMB(self):
        mb = super().getKB() / 1024
        return mb 
    

#create object 
#OBJECT = CLASSNAME()
bytes = int(input("Enter bytes "))
# k1 = KB(bytes) #constructor will be run automatically
# kb = k1.getKB()
# print(f"kilobytes = {kb:.2f}")

m1 = MB(bytes)
mb = m1.getMB()
kb = m1.getKB()
print(f"kb = {kb:.2f}")
print(f"mb = {mb:.2f}")