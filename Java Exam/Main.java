
import java.util.*;
import java.lang.Math;

class Triangle{
    int Area(){
        System.out.println("No sides has been entered to display area");
        return 0;
    }
    int Area(int a)
    {
        System.out.println("Insuffcient Information");
        return 0;
    }
    int Area(int h, int b){
        double area  = 0.5*h*b;
        System.out.println("Area of the triangle is: "+area);
        return 0;
    }
    int Area(int a, int b, int c){
        int k = a+b+c; 
        int s = k/2;
        double area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
        System.out.println("Area of the triangle is: "+area);
        return 0;
    }
}

public class Main{
    public static void main(String[] args) {
        Triangle t = new Triangle();
        System.out.println("Enter number of sides of triangle:");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(n == 0){
            t.Area();
        }
        else if(n == 1){
            t.Area(5);
        }
        else if(n == 2){
            System.out.println("Enter height of the Triangle:");
            int h = sc.nextInt();
            System.out.println("Enter base of the Triangle:");
            int b = sc.nextInt();
            t.Area(h, b);
        }
        else if (n==3){
            System.out.println("Enter first side of the triangle");
            int a = sc.nextInt();
            System.out.println("Enter second side of the triangle");
            int b = sc.nextInt();
            System.out.println("Enter third side of the triangle");
            int c = sc.nextInt();
            t.Area(a, b, c);
        }
        else{
            System.out.println("Invalid input");
        }
        sc.close();
    }
}