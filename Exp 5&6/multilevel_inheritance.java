class UniversityMember{
    String Name;char Gender;

    public UniversityMember(String Name, char Gender) {
        this.Name=Name;
        this.Gender=Gender;
    }

    public UniversityMember() {
        Name=null;
        Gender=' ';
    }

    void Display(){
        System.out.println("Name: "+Name+" Gender: "+Gender);
    }
    
}
class Stud extends UniversityMember{
    String course, branch;

    public Stud() {
        course=null;
        branch=null;
    }
    public Stud(String course, String branch){
        this.course=course;
        this.branch=branch;
    }
    void display(){
        System.out.println("Course: "+course+" Branch: "+branch);
    }
}
class Year extends Stud{
    int yearId, semId;
    double cgpa;
    public Year() {
        yearId=0;
        semId=0;
        cgpa=0.0;
    }
    public Year(int yearId, int semId, double cgpa){
        this.yearId=yearId;
        this.semId=semId;
        this.cgpa=cgpa;
    }
    void disp(){
        System.out.println("Year ID: "+yearId+" Semester ID: "+semId+" CGPa "+cgpa);
    }
}
public class multilevel_inheritance {
    public static void main(String[] args) {
        UniversityMember s = new UniversityMember("Shivansh Jha", 'M');
        s.Display();
        Stud st = new Stud("Btech", "CSE");
        st.display();
        Year y = new Year(1, 1, 8.0);
        y.disp();
    }
}
