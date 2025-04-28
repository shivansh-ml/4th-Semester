class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    pass

class Developer(Employee):
    pass

class Tester(Employee):
    pass

manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
tester = Tester("Charlie", 50000)
manager.display_details()
developer.display_details()
tester.display_details()