import java.util.Scanner;

public class PointInCircle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the x-coordinate of the point: ");
        double x = scanner.nextDouble();

        System.out.print("Enter the y-coordinate of the point: ");
        double y = scanner.nextDouble();

        double radius = 5.0;

        double distanceSquared = x * x + y * y;
        double radiusSquared = radius * radius;

        if (distanceSquared < radiusSquared) {
            System.out.println("The point (" + x + ", " + y + ") lies inside the circle.");
        } else if (distanceSquared > radiusSquared) {
            System.out.println("The point (" + x + ", " + y + ") lies outside the circle.");
        } else {
            System.out.println("The point (" + x + ", " + y + ") lies on the circle.");
        }

        scanner.close();
    }
}
