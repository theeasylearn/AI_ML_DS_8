#let use create home class 
class Student:
    def __init__(self,name,surname,age,weight):
        print("__init__ method called")
        #create instance variable
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
    def display(self):
        print("Name ",self.name) #krishna
        print("Surname ",self.surname) 
        print("Age ",self.age)
        print("Weight ",self.weight)
    def update(self,name,surname,age,weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        print("update operation completed....")
        
#accept input from user (name,surname,age,weight)
name = input("Enter Student name")
surname = input("Enter Student surname")
age = int(input("Enter student age"))
weight = float(input("Enter weight"))

#object = classname()
s1 = Student(name,surname,age,weight) # __init__ method will be called automatically
print("before update")
s1.display()
print("enter student detail to update")
name = input("Enter Student name")
surname = input("Enter Student surname")
age = int(input("Enter student age"))
weight = float(input("Enter weight"))

s1.update(name,surname,age,weight)
print("after update")
s1.display()