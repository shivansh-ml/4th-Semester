public class ExponentialTable {
    public static void main(String[] args) {
        
        System.out.println("x\t0\t0.1\t0.2\t0.3\t0.4\t0.5\t0.6\t0.7\t0.8\t0.9\t1");
        
        System.out.print("y\t");
        for (double x = 0; x <= 1; x += 0.1) {
            double y = Math.exp(-x); 
            System.out.printf("%.3f\t", y); 
        }
    }
}
