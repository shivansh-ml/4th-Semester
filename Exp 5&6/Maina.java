// 2. Modify the Java program shown in Listing 5.2 to do the following:

// 1. Add a class FirstSem that is an extension of class FirstYear. Add a function void subjects() to the class FirstSem that displays “6 theory courses and 2 lab courses”. Compile and run the program. Apply the concept of multilevel inheritance.
// 2. Add three more classes, SecondYear, ThirdYear, FourthYear which are extensions of class Student. 
// Add three functions, void year2(), void year3(), void year4() to three new classes SecondYear, ThirdYear, FourthYear respectively. 
// The function void year2() displays “2nd year...”, function void year3() prints “3rd year...”, and function void year4() shows “4th year...” Apply the concept of hierarchical inheritance.
class Person{
    void Name(){
        System.out.println("Name is Shivansh Jha");
    }
}
class student extends Person{
    void roll(){
        System.out.println("Roll is 2330335");
    }
}
class FirstYear extends student{
    void year(){
        System.out.println("FirstYear");
    }
}
class FirstSem extends FirstYear{
    void subjects(){
        System.out.println("6 theory courses and 2 lab courses");
    }
}
class SecondYear extends student{
    void year2(){
        System.out.println("2nd year...");
    }
}
class ThirdYear extends student{
    void year3(){
        System.out.println("3rd year...");
    }
}
class FourthYear extends student{
    void year4(){
        System.out.println("4th year...");
    }
}
public class Maina {
    public static void main(String[] args) {
        FirstSem fs = new FirstSem();
        fs.Name();
        fs.roll();
        fs.year();
        fs.subjects();
        SecondYear sy = new SecondYear();
        sy.year2();
        ThirdYear ty = new ThirdYear();
        ty.year3();
        FourthYear fy = new FourthYear();
        fy.year4();
    }
}
