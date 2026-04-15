# hierarchical inheritance 
class MyMath:
    def getPi(self):
        pi = 3.142857
        return pi 
    def getSquare(self,number):
        square = number * number
        return square
class Circle(MyMath):
    def __init__(self,radius):
        self.radius = radius
        print("Circle class constructor called....")
    def getArea(self):
        pi = super().getPi()
        square = super().getSquare(self.radius);
        area = pi * square 
        return area 

class Cylinder(MyMath):
    def __init__(self,radius,height):
        self.radius = radius 
        self.height = height 
    def getLateralSurface(self):
        temp = 2 * super().getPi() * self.radius * self.height
        return temp 

class Sphere(Circle):
    def __init__(self,radius):
        #call parent class constructor 
        super().__init__(radius)
        print("Sphere class constructor called....")
    #Method Overriding 
    def getArea(self):
        area = super().getArea()
        area = 4 * area 
        return area 
        
radius = int(input("Enter Sphere radius "))
s1 = Sphere(radius) #execute/run constructor 
area = s1.getArea()
print(f"Area = {area:.2f}")







