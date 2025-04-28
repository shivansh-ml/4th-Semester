import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive")
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Creating instances with error handling
try:
    shapes = [Circle(-5), Rectangle(4, 6), Triangle(3, -8)]
    for shape in shapes:
        print(f"Area: {shape.area()}")
except ValueError as e:
    print("Error:", e)
