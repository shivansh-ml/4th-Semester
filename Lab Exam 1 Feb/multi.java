class UniversityMember{
    String name;
    char gender;
    UniversityMember(){
        name = "Shivansh Jha";
        gender = 'M';
    }
    void display(){
        System.out.println("Name: "+name);
        System.out.println("Gender: "+gender);
    }
}
class Student extends UniversityMember {
    String course, branch;
    Student(){
        course = "B.Tech";
        branch = "CSE";
    }
    void display(){
        super.display();
        System.out.println("Course: "+course);
        System.out.println("Branch: "+branch);
    }
}
class Year extends Student{
    int semId;
    int year;
    int sgpa;
    Year(int semId, int year, int sgpa){
        this.semId = semId;
        this.year = year;
        this.sgpa=sgpa;
    }
    void display(){
        super.display();
        System.out.println("Year: "+year);
        System.out.println("Semester Id: "+semId);
        System.out.println("SGPA: "+sgpa);
    }
}
public class multi{
    public static void main(String[] args) {
        Year y = new Year(4, 2 , 8);
        y.display();
    }
}
