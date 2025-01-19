class Rectangle
{
    double length;
    double breadth;
    double area()
    {
        return length*breadth;
    }
    double perimeter()
    {
        return 2*(length+breadth);
    }
} 
public class Rect {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.length = 10;
        r.breadth = 20;
        System.out.println("Area of Rectangle is: "+r.area());
        System.out.println("Perimeter of Rectangle is: "+r.perimeter());
    }
}