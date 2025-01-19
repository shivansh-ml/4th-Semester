import java.util.*;

public class Exp1c {
    public static void main(String[] args) {
        // Using try-with-resources to automatically close the Scanner
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter length of rectangle:");
            int l = sc.nextInt();
            System.out.println("Enter breadth of rectangle:");
            int b = sc.nextInt();
            int p = 2 * (l + b);            
            System.out.println("The area is "+l*b);
            System.out.println("The perimeter is " +p );
        } // The Scanner 'sc' will be automatically closed here
    }
}