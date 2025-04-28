class Employee:
    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement this method")

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_pay(self):
        return self.salary

# Creating instances
employees = [
    HourlyEmployee("Alice", 20, 40),
    SalariedEmployee("Bob", 5000)
]

for employee in employees:
    print(f"{employee.name}'s Payment: {employee.calculate_pay()}")
