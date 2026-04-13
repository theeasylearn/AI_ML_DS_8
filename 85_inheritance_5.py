# example multiple inheritance 

#Parent class 1
class Person:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")

#Parent class 2
class Robot:
    def automate(self):
        print("I can do automation")
    def manipulate(self):
        print("I can manipulate")
    
class Humanoid(Person,Robot):
    #Method overriding 
    def eat(self):
        print("I can not eat.")
    def whatICanDo(self):
        super().walk()
        super().talk()
        super().automate()
        super().manipulate()
    

h1 = Humanoid()
h1.whatICanDo()
h1.eat()