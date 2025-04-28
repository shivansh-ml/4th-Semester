class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
    
    def display_info(self):
        print(f"Vehicle: {self.name}, Mileage: {self.mileage}")

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

car = Car("Sedan", 15)
truck = Truck("Pickup", 8)
car.display_info()
truck.display_info()
