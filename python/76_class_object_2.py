#let use create home class 
class Student:
    def __init__(self):
        print("__init__ method called")
        #create instance variable
        self.name = "krishna"
        self.surname = "dave"
        self.age = 25
        self.weight = 75.22
    def display(self):
        print("Name ",self.name) #krishna
        print("Surname ",self.surname) 
        print("Age ",self.age)
        print("Weight ",self.weight)
    def update(self):
        self.name = "darshil"
        self.surname = "joshi"
        self.age = 18
        self.weight = 76.11

#object = classname()
s1 = Student() # __init__ method will be called automatically
print("before update")
s1.display()
s1.update()
print("after update")
s1.display()