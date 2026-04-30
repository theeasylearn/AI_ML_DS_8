#Parent class
class Person:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")

#Child class
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

#create object (class type variable)
#object-name = class()
p1 = Person()
#calling function using object
p1.walk()
p1.talk()
p1.eat()
print("_"*120)
s1 = Student()
s1.whatICanDO()
s1.walk()
s1.read()