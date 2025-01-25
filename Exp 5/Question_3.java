// 3. Modify the program written for Problem 2 to do the following:

// 1. Add variables to each of the class. 
// Add a no-argument constructor in each of the classes to initialize the variables to default values 
// (0 for integers and NULL/EMPTY for strings).
// 2. Add parameterized constructors in each class to assign user inputs to the member variables.
class Person1 {
    int n;
    String s;

    Person1() {
        n = 0;
        s = null;
    }

    Person1(int n, String s) {
        this.n = n;
        this.s = s;
    }
}

class student1 extends Person1 {
    int n1;
    String s1;

    student1() {
        n1 = 0;
        s1 = null;
    }

    student1(int n1, String s1) {
        this.n1 = n1;
        this.s1 = s1;
    }
}

class FirstYear1 extends student1 {
    int n1a;
    String s1a;

    FirstYear1() {
        n1a = 0;
        s1a = null;
    }

    FirstYear1(int n1a, String s1a) {
        this.n1a = n1a;
        this.s1a = s1a;
    }
}

class FirstSem1 extends FirstYear1 {
    int n1aI;
    String s1aI;
    FirstSem1() {
        n1aI = 0;
        s1aI = null;
    }
    
}

class SecondYear1 extends student1 {
    
}

class ThirdYear1 extends student1 {
    
}

class FourthYear1 extends student1 {
    
}

public class Question_3 {
    public static void main(String[] args) {

    }
}
