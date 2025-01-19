
//Import the class Scanner from util package.
//import java.util.Scanner;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class input {
    public static void main(String[] args) {
        //Create Buffered Reader class Project
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        try {
            String input =br.readLine();
            int n=Integer.parseInt(input);
            System.out.println("Square is: "+n*n);
            br.close();
        } 
        catch (IOException ioe) {
            System.err.println("Input Error "+ioe);
        }
    }

    // // Using java.util.Scanner class and System.in
    // public static void main(String[] args) 
    // {
    //     // Create the object of Scanner class using System.in
    //     try (Scanner sc = new Scanner(System.in)) 
    //     {
    //         // Using next() method to get the input from user
    //         System.out.println("Enter a String");
    //         String s = sc.nextLine();
    //         System.out.println("Entered String is: " + s);
    //     }
    // }

    // Using Console Class
    // public static void main(String[] args)
    // {
    // System.out.println("What is your name? ");
    // String name = System.console().readLine();
    // System.out.println("Hello, " + name + "!");
    // }
    // Console class is used to read the input from cmd line prompt(Will not work on
    // IDE like eclipse or netbeans)
}
/*
 * public String next()------------Finds and returns the next complete token from this scanner(To read 1 word next is preffered and it will skip the Blank Line)
 * public String nextLine()--------moves the scanner position to next Line and returns input as a string
 * public byte nextByte()----------scans the next token of the input and returns the token as a byte
 * public short nextShort()--------scans the next token as a short value
 * public int nextInt()------------scans the next token of input as a integer
 * public long nextLong()----------scans the next token of input as a long
 * public float nextFloat()--------scans the next token of input as a float
 * public double nextDouble()------scans the next token of input as a double
 * SCANNER IS USED TO READ AN INTEGER WITH nextInt(), THAT SAME SCANNER CANNOT BE USED TO READ A STRING USING nextLine() AND WAITING ON INPUT.
 * IT WILL NOT WORK BECAUSE IT WILL READ THE NEWLINE FROM INTEGER INPUT . ONE WAY IS TO CREATE ANOTHER SCANNER, SO YOU HAVE TWO ONE FOR INPUTTING INTEGERS AND THE OTHER FOR INPUTTING TEXT.
 */