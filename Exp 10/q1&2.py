class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Creating an instance and displaying student information
student1 = Student("Alice", 20, "A")
student1.display_info()

# Calling method talk to display student details
def talk():
    student1.display_info()

talk()