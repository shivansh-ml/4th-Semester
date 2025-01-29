class UniversityMember {
    String name;
    String gender;

    UniversityMember(String name, String gender) {
        this.name = name;
        this.gender = gender;
    }

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Gender: " + gender);
    }
}

class Student extends UniversityMember {
    String course;
    String branch;

    Student(String name, String gender, String course, String branch) {
        super(name, gender);
        this.course = course;
        this.branch = branch;
    }

    void displayStudentDetails() {
        display();
        System.out.println("Course: " + course);
        System.out.println("Branch: " + branch);
    }
}

class Employee extends UniversityMember {
    String employeeID;

    // Constructor
    Employee(String name, String gender, String employeeID) {
        super(name, gender);
        this.employeeID = employeeID;
    }

    void displayEmployeeDetails() {
        display();
        System.out.println("Employee ID: " + employeeID);
    }
}

class Teaching extends Employee {
    String designation;

    Teaching(String name, String gender, String employeeID, String designation) {
        super(name, gender, employeeID);
        this.designation = designation;
    }

    void displayTeachingDetails() {
        displayEmployeeDetails();
        System.out.println("Designation: " + designation);
    }
}

class NonTeaching extends Employee {
    String designation;

    NonTeaching(String name, String gender, String employeeID, String designation) {
        super(name, gender, employeeID);
        this.designation = designation;
    }

    void displayNonTeachingDetails() {
        displayEmployeeDetails();
        System.out.println("Designation: " + designation);
    }
}

// Derived class from Student
class Year extends Student {
    String yearID;
    String semID;
    String rollNumber;
    double SGPA;

    // Constructor
    Year(String name, String gender, String course, String branch, String yearID, String semID, String rollNumber, double SGPA) {
        super(name, gender, course, branch);
        this.yearID = yearID;
        this.semID = semID;
        this.rollNumber = rollNumber;
        this.SGPA = SGPA;
    }

    void displayYearDetails() {
        displayStudentDetails();
        System.out.println("Year ID: " + yearID);
        System.out.println("Semester ID: " + semID);
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("SGPA: " + SGPA);
    }
}

public class Main {
    public static void main(String[] args) {
        Student student = new Student("John Doe", "Male", "BTech", "Computer Science");
        student.displayStudentDetails();

        Employee employee = new Employee("Jane Smith", "Female", "E12345");
        employee.displayEmployeeDetails();

        Teaching teaching = new Teaching("Dr. Alice", "Female", "T67890", "Professor");
        teaching.displayTeachingDetails();

        NonTeaching nonTeaching = new NonTeaching("Mr. Bob", "Male", "N54321", "Clerk");
        nonTeaching.displayNonTeachingDetails();

        Year year = new Year("Mike Johnson", "Male", "MTech", "Electrical Engineering", "Y2", "S1", "R123", 9.5);
        year.displayYearDetails();
    }
}