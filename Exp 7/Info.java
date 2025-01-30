/*
 Create a Java program that defines a parent class called Student with two member variables: name and roll. 
 Initialize these variables using a no-argument constructor and include a member method info() to print your name and roll number. 
 Create three child classes: FirstSem, SecondSem, and ThirdSem, each extending the Student class. 
 Each child class should have a member variable SGPA which is initialized in a no-argument constructor. 
 Include a member method info() in all three child classes that prints the name, roll number and SGPA 
 for all three semesters using inheritance and method overriding.
 */
class Student {
    String name;
    int roll;

    Student() {
        name = "Shivansh Jha";
        roll = 123;
    }

    void info() {
        System.out.println("Name: " + name + " Roll Number: " + roll);
    }
}

class FirstSem extends Student {
    double SGPA;

    FirstSem() {
        SGPA = 8.5;
    }

    void info() {
        super.info();
        System.out.println("SGPA: " + SGPA);
    }
}

class SecondSem extends Student {
    double SGPA;

    SecondSem() {
        SGPA = 8.8;
    }

    void info() {
        super.info();
        System.out.println("SGPA: " + SGPA);
    }
}

class ThirdSem extends Student {
    double SGPA;

    ThirdSem() {
        SGPA = 9.0;
    }

    void info() {
        super.info();
        System.out.println("SGPA: " + SGPA);
    }
}

public class Info {
    public static void main(String[] args){
        
        FirstSem fs = new FirstSem();
        fs.info();
        System.out.println();
        SecondSem ss = new SecondSem();
        ss.info();
        System.out.println();
        ThirdSem ts = new ThirdSem();
        ts.info();
        System.out.println();
    }
}
