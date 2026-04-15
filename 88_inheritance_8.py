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
    
radius = int(input("Enter Circle radius "))
c1 = Circle(radius)

area1 = c1.getArea()

radius = int(input("Enter cylineder radius "))
height = int(input("Enter cylineder height "))

c2 = Cylinder(radius,height)
area2 = c2.getLateralSurface()

print("circle area = ",area1)
print("cylinder surface area = ",area2)



