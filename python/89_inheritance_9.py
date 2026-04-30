# hybrid inheritance
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

class Actor(Person):
    def dance(self):
        print("I can dance")
    def fight(self):
        print("I can fight")
    def drama(self):
        print("I can do acting")
    def whatICanDo(self):
        super().walk()
        super().talk()
        super().eat()
        self.fight()
        self.dance()
        self.drama()

class Producer(Student,Actor):
    def Produce(self):
        print("I can produce movie")
    #Method Overriding 
    def whatICanDO(self):
        #calling Student(Parent) whatICanDo
        Student.whatICanDO(self)
        #calling Actor(Parent) whatICanDo
        Actor.whatICanDo(self)

#create Producer class object 
p1 = Producer()
p1.whatICanDo() #calling method of Producer 
