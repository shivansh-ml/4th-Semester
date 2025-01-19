import java.util.*;

class Triangle {
    private int side1;
    private int side2;
    private int side3;

    public Triangle(int side1, int side2, int side3) {
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public void Display() {
        System.out.println("Side 1: " + side1 + "\nSide 2: " + side2 + "\nSide 3: " + side3);
    }

    public void Equilateral() {
        if (side1 == side2 && side2 == side3) {
            System.out.println("This is an Equilateral Triangle");
        } else {
            System.out.println("This is not an Equilateral Triangle");
        }
    }

    public void Isoceles() {
        if (side1 == side2 || side2 == side3 || side1 == side3) {
            System.out.println("This is an Isoceles Triangle");
        } else {
            System.out.println("This is not an Isoceles Triangle");
        }
    }

    public void Right_Angle() {
        if (side1 == Math.sqrt(Math.pow(side2, 2) + Math.pow(side3, 2))) {
            System.out.println("The triangle is a right angle triangle\n");
        } else {
            System.out.println("The triangle is not a right angle triangle\n");
        }
    }

    public void changeSide(int l) {
        System.out.println("Choose the side you wish to change\n");
        int ch;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("1. Hypotenuse 1\n2. Base 2\n3. Height 3");
            ch = sc.nextInt();
            switch (ch) {
                case 1 -> side1 = l;
                case 2 -> side2 = l;
                case 3 -> side3 = l;
                default -> System.out.println("The user choice is Invalid");
            }
        }
    }
};

public class Triangles {
    public static void main(String[] args) {
        int s1, s2, s3;
        System.out.println("Enter the sides of the triangle\n");
        try (Scanner sc = new Scanner(System.in)) {
            s1 = sc.nextInt();
            s2 = sc.nextInt();
            s3 = sc.nextInt();
            Triangle t = new Triangle(s1, s2, s3);
            t.Display();
            System.out.println("What do you want to check\n");
            System.out.println("1.Equilateral triangle\n2.Isosceles triangle\n3.Right-Angled triangle\n");
            int ch = sc.nextInt();
            switch (ch) {
                case 1 -> {
                    System.out.println("Checking if the triangle is an Equilateral triangle\n");
                    t.Equilateral();
                }
                case 2 -> {
                    System.out.println("Checking if the triangle is an Isosceles triangle\n");
                    t.Isoceles();
                }
                case 3 -> {
                    System.out.println("Checking if triangle is an equilateral triangle\n");
                    t.Right_Angle();
                }
                default -> System.out.println("The user choice is Invalid");
            }
        }
    }
}