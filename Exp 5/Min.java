// 1. Modify the Java program shown in Listing 5.1 to do the following:

// 1. Add a function void gender() to class Person that prints the state-
// ment “Gender is...”

// 2. Add a function void branch() to class Student that prints the state-
// ment “Branch is ECSC”.
class Person{
    void Gender(){
        System.out.println("Gender is Male");
    }
    void Name(){
        System.out.println("Name is Shivansh Jha");
    }
}
class Student extends Person{
    void Branch(){
        System.out.println("Branch is ECSC");
    }
    void roll(){
        System.out.println("Roll is 2330335");
    }
}
public class Min{
    public static void main(String[] args) {
        Student sc= new Student();
        sc.Name();
        sc.Gender();
        sc.roll();
        sc.Branch();
    }
}
