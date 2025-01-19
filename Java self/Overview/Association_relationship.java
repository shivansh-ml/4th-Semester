import java.util.Scanner;
class SmartCard{
    int emp_idn;
    public void MarkAttendance(Employee e){
        emp_idn=e.getEmpId();
        //Instructions to mark present for empid...e.
        System.out.println("Employee "+emp_idn+" is marked present");
    }
    public int getEmpId(Employee e)
    {
        return e.empid;
    }
}
class Employee{
    int empid;
    Employee()
    {
        System.out.println("Enter Employee ID");
        try (Scanner sc = new Scanner(System.in)) {
            this.empid=sc.nextInt();
        }
    }
    int getEmpId()
    {
        return empid;
    }
    public void Login(SmartCard sc)
    {
        //Instructions to login functionality......
        //get the empid from the employee object and mark attendance using smartcard object
        int eid=sc.getEmpId(this);
        //Login and Mark attendance
        System.out.println("Login succesulfull for Employee "+eid);
    }
}
public class Association_relationship {
    public static void main(String[] args) {
        System.out.println("****************Association between Employee and SmartCard****************");
        Employee e=new Employee();
        System.out.println("New Employee is Created!");
        SmartCard scd=new SmartCard();
        scd.MarkAttendance(e);//passing the reference of employee to smartcard
        e.Login(scd);//passing the reference of smartcard to employee
    }
}
