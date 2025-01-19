// import java.io.DataInputStream;

// public class read_statement {
//     public static void main(String[] args) {
//         DataInputStream in = new DataInputStream(System.in);
//         int intNumber=0;
//         float floatNumber=0.0f;
//         try{
//             System.out.println("Enter an Integer: ");
//             intNumber=Integer.parseInt(in.readLine());
//             System.out.println("Enter a float number: ");
//             floatNumber=Float.valueOf(in.readLine()).floatValue();
//         }
//         catch(Exception e)
//         {
//             System.out.println("Input Error: "+e);
//         }
//         System.out.println("Int Number= "+intNumber);
//         System.out.println("Float Number= "+floatNumber);
//     }
// }

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ReadStatement {
    public static void main(String[] args) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int intNumber = 0;
        float floatNumber = 0.0f;
        try {
            System.out.println("Enter an Integer: ");
            intNumber = Integer.parseInt(in.readLine());
            System.out.println("Enter a float number: ");
            floatNumber = Float.parseFloat(in.readLine()); // Directly parse float
        } catch (IOException | NumberFormatException e) { // Multi-catch for IOException and NumberFormatException
            System.out.println("Input Error: " + e);
        }
        System.out.println("Int Number= " + intNumber);
        System.out.println("Float Number= " + floatNumber);
    }
}
/*
 * ReadLine Method reads the input from the computer a String. So we need to parse it to get the desired data type using wrapper classes.
 * We use exception handling mechanism and enclose the code that  might generate run time error inside  try block.
 * If run time error is not there then the code inside catch block will not be executed.
 * In-built method readLine() is used to read the input entered through keyboard.
 * The declaration of readLine() method of DataInputStream class is as follows: public String readLine() throws IOException
 * For every Java program java.lang.package is imported by default.
 * System is an inbuilt class from java.lang package.
 * (static data member)out->Belongs to class PrintStream->Have defined (static method)println.
 */