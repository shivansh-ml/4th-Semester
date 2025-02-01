class Employee {
    String name;
    int salary;
    String dept;
    String EmpID;

    Employee() {
        name = null;
        dept = null;
        EmpID = null;
        salary = 0;
    }

    Employee(String s, int sal) {
        name = s;
        dept = null;
        EmpID = null;
        salary = sal;
    }

    Employee(String s, int sal, String d) {
        name = s;
        dept = d;
        EmpID = null;
        salary = sal;
    }

    Employee(String s, int sal, String d, String e) {
        name = s;
        dept = d;
        EmpID = e;
        salary = sal;
    }

    void display() {
        System.out.println("Name: " + name + "\n" + " Salary: " + salary + "\n" + " Department: " + dept + "\n"
                + "Employee Id: " + EmpID);
    }
}

public class constructor {
    public static void main(String[] args) {
        Employee e = new Employee();
        Employee e1 = new Employee("SJ", 20020);
        Employee e2 = new Employee("Sj", 2992920, "HR");
        Employee e3 = new Employee("SJ", 1279129, "Sales", "ABC_!23");
        e.display();
        e1.display();
        e2.display();
        e3.display();

    }
}
