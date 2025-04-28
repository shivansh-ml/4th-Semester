class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage
    
    def display_info(self):
        super().display_info()
        print(f"Mileage: {self.mileage} km/l")

car = Car("Toyota", "Corolla", 2022, 15)
car.display_info()