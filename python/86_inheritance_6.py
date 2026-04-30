# multiple inheritance 
class Triangle:
    #constructor
    def __init__(self,base,height):
        self.base = base
        self.height = height;
        print("Triangle class constcructor called")
    def getArea(self):
        area = 0.50 * self.base * self.height
        return area 
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width 
        print("Rectangle class constructor called.")
    def getArea(self):
        area = self.length * self.width
        return area 
#add class Circle which also has constructor and getArea method and it should also inherted in Property class
class Property(Triangle,Rectangle):
    def __init__(self, base, height,length,width):
        Triangle.__init__(self,base,height) #calling Trinagle class constructor
        Rectangle.__init__(self,length,width) #calling Rectangel class constructor
        print("property class constructor called")
    #method overriding
    def getArea(self):
        area1 = Triangle.getArea(self)
        area2 = Rectangle.getArea(self)
        totalarea = area1 + area2 
        return totalarea
b = int(input("Enter base"))
h = int(input("Enter height"))
l = int(input("Enter length"))
w = int(input("Enter width"))

p1 = Property(b,h,l,w)
totalarea = p1.getArea()
print(f"Total Area = {totalarea}")
