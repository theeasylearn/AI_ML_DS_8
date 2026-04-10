# example multilevel inheritance 

#Parent class 1
class Person:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")

#Child class 2
class Student(Person):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDO(self):
        super().walk()
        super().eat()
        super().talk()
        self.read()
        self.write()    

#leaf class 3
class Developer(Student):
    def code(self):
        print("I can code in python")
    def debug(self):
        print("I can debug code in python")
    #method overidding
    def whatICanDO(self):
        super().whatICanDO()
        self.code()
        self.debug()


#create object of developer class
d1 = Developer()
d1.code()
d1.debug()

#calling parent method Developer
d1.read()
d1.write()

#calling grand parent class method 
d1.walk()
d1.talk()
d1.eat()
