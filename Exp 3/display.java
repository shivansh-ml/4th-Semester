class UniMember {
    String name;
    char gender;
    class Student {
        int Roll_No;
    }
    class Employee {
        int Emp_ID;
    }
}

public class display{
    public static void main(String[] args) {
        UniMember std = new UniMember();
        UniMember.Student student = std.new Student();

        std.name = "Rahul";
        std.gender = 'M';
        student.Roll_No = 101;

        UniMember empMember = new UniMember();
        UniMember.Employee empEmployee = empMember.new Employee();
        empMember.name = "Umesh Yadav";
        empMember.gender = 'M';
        empEmployee.Emp_ID = 2001;

        System.out.println("Detail Of Student are: ");
        System.out.println("Name: " + std.name);
        System.out.println("Gender: " + std.gender);
        System.out.println("Roll No: " + student.Roll_No);

        System.out.println("\nDetail Of Employee are: ");
        System.out.println("Name: " + empMember.name);
        System.out.println("Gender: " + empMember.gender);
        System.out.println("Emp ID: " + empEmployee.Emp_ID);
    }
}