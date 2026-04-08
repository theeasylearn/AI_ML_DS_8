class Student:
    #class variable
    ClassName = "THE EASYLEARN ACADEMY";
    #define constructor
    def __init__(self,name,rollno):
        print("constructor called...")
        #instance variable
        self.name = name 
        self.rollno = rollno
    def display(self):
        print("-"*110)
        print("Roll No ",self.rollno, " Name ",self.name)
        print("-"*110)
    
#create object 
s1 = Student(name='Darshil joshi',rollno=100) #constructor called automatically
s2 = Student(name='Nirav bariya',rollno=101) #constructor called automatically
s1.display() #display detail of Darshil
s2.display() #display detail of Nirav
print(s1.rollno,s1.name)
print(s1.ClassName) #accessing class variable using object
print(s2.ClassName) #accessing class variable using object
#accessing class variable using class 
print(Student.ClassName) #accessing class variable using class
Student.ClassName = "THE EASYLEARN" #change class variable using class 
print(Student.ClassName) #accessing class variable using object
