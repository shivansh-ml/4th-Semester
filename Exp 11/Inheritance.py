class Animal:
    def __init__(self, species):
        self.species = species
    def speak(self):
        pass # Abstract method
    def info(self):
        print(f"I am a {self.species}")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog("Canine")
dog.info()
print(dog.speak())