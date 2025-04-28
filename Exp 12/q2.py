class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        return "Woof Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo Moo!"

# Creating instances
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"{animal.__class__.__name__} makes sound: {animal.sound()}")
