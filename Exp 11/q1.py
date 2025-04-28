class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    
    def get_info(self):
        print(f"Color: {self.color}, Filled: {'Yes' if self.filled else 'No'}")

class Rectangle(Shape):
    def __init__(self, color, filled, length, width):
        super().__init__(color, filled)
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

rect = Rectangle("Red", True, 5, 10)
rect.get_info()
print("Area:", rect.calculate_area())
