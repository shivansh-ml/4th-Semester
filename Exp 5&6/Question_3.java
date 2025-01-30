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
    FirstSem1(int n1aI, String s1aI){
        this.n1aI = n1aI;
        this.s1aI = s1aI;
    }
}

class SecondYear1 extends student1 {
    int n1b;
    String s1b;
    SecondYear1(){
        n1b=0;
        s1b=null;
    }
    SecondYear1(int n1b, String s1b){
        this.n1b = n1b;
        this.s1b = s1b;
    }
}

class ThirdYear1 extends student1 {
    int n2c;
    String s2c;
    ThirdYear1(){
        n2c = 0;
        s2c = null;
    }
    ThirdYear1(int n2c, String s2c){
        this.n2c=n2c;
        this.s2c=s2c;
    }
}

class FourthYear1 extends student1 {
    int n2d;
    String s2d;
    FourthYear1(){
        n2d = 0;
        s2d = null;
    }
    FourthYear1(int n2d, String s2d){
        this.n2d = n2d;
        this.s2d = s2d;
    }
}

public class Question_3 {
    public static void main(String[] args) {
        Person1 p = new Person1();
        student1 s = new student1();
        FirstYear1 fy = new FirstYear1();
        FirstSem1 fs = new FirstSem1();
        SecondYear1 sy = new SecondYear1();
        ThirdYear1 ty = new ThirdYear1();
        FourthYear1 Fy = new FourthYear1();
        System.out.println("Default value of value present in the classes");
        System.out.println("For person1 : " + p.n+" & "+p.s);
        System.out.println("For student1 : " + s.n1+" & "+s.s1);
        System.out.println("For Firstyear1 : " + fy.n1a+" & "+fy.s1a);
        System.out.println("For FirstSem1 : " + fs.n1aI+" & "+fs.s1aI);
        System.out.println("For SecondYear1 : " + sy.n1b+" & "+sy.s1b);
        System.out.println("For ThirdYear1 : " + ty.n2c+" & "+ty.s2c);
        System.out.println("For FourthYear1 : " + Fy.n2d+" & "+Fy.s2d);
        Person1 p1 = new Person1(1, "Person");
        student1 s1 = new student1(2,"Student");
        FirstYear1 fy1 = new FirstYear1(3, "FirstYear");
        FirstSem1 fs1 = new FirstSem1(4,"FirstSemester");
        SecondYear1 sy1 = new SecondYear1(5,"SecondYear");
        ThirdYear1 ty1 = new ThirdYear1(6,"ThirdYear");
        FourthYear1 Fy1 = new FourthYear1(7,"FourthYear");
        System.out.println("After intialzing the value of the variable");
        System.out.println("For person1 : " + p1.n+" & "+p1.s);
        System.out.println("For student1 : " + s1.n1+" & "+s1.s1);
        System.out.println("For Firstyear1 : " + fy1.n1a+" & "+fy1.s1a);
        System.out.println("For FirstSem1 : " + fs1.n1aI+" & "+fs1.s1aI);
        System.out.println("For SecondYear1 : " + sy1.n1b+" & "+sy1.s1b);
        System.out.println("For ThirdYear1 : " + ty1.n2c+" & "+ty1.s2c);
        System.out.println("For FourthYear1 : " + Fy1.n2d+" & "+Fy1.s2d);
    }
}
