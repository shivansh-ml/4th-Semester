class Complex {
    double real;
    double complex;

    Complex(double r, double c) {
        real = r;
        complex = c;
    }

    void display() 
    {
        System.out.println("The number is: " + String.format("%.2f", real) + " + i" + String.format("%.2f", complex) + "\n");
    }

    void ComplexSum(double r1, double c1, double r2, double c2) 
    {
        System.out.println("The Sum of two complex number is: " + String.format("%.2f", (r1 + r2)) + " + i" + String.format("%.2f", (c1 + c2)) + "\n");
    }

    void ComplexDot(double r1, double c1, double r2, double c2) {
        System.out.println("The Dot product of two complex number is: " + String.format("%.2f", (r1 * r2)) + " + i" + String.format("%.2f", (c1 * c2)) + "\n");
    }
}

public class ComplexSum {
    public static void main(String[] args) {
        Complex c = new Complex(5.98, 7.7);
        c.display();
        Complex c1 = new Complex(5.8, 7.79);
        c.ComplexSum(c1.real, c1.complex, c.real, c.complex);
        c.ComplexDot(c1.real, c1.complex, c.real, c.complex);
    }
}