import java.util.*;
class box1
{
    double side;
    double volume()
    {
        return side * side * side;//3. set values to two objects using parameterized methods and get the volumes of two boxes
    }
}
public class Box2 {
    public static void main(String args[])
    {
      System.out.println("Hello \n");  
      box1 cube_a = new box1();
      box1 cube_b = new box1(); //1. Create two object of class box
      try(Scanner sc=new Scanner(System.in))
      {
        System.out.println("Enter value of first cube");
        cube_a.side=sc.nextDouble();
        System.out.println("Volume of first cube is "+cube_a.volume());
        System.out.println("Enter value of second cube");
        cube_b.side=sc.nextDouble();
        System.out.println("Volume of first cube is "+cube_b.volume());//2. assign values to two objects using objects’ instance-variables and get the volumes of two boxes
      }
    }
}