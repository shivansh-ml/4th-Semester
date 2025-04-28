import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

circle = Circle(5)
square = Square(4)
print("Circle Area:", circle.area(), "Circle Perimeter:", circle.perimeter())
print("Square Area:", square.area(), "Square Perimeter:", square.perimeter())
