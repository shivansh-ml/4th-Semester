// 3. Create a Java class called Account with the member data account number,name, balance. Using constructors and member methods, perform the following:

// 1. to accept and display the details of an account
// 2. to credit the account with some amount and display the message “A/C credited with Rs. XYZ and Balance: Rs. ABC” (where, XYZ is the amount credited and ABC is the new balance in the account).
// 3. to debit the account with some amount and display the message “A/C debited with Rs. XYZ and Balance: Rs. ABC” (where, XYZ is the amount debited and ABC is the new balance in the account).
import java.util.*;

class Account {
    String name;
    int balance;
    int accountNumber;

    Account(String name, int accountNumber, int balance) {
        this.name = name;
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    void display() {
        System.out.println(" Name : " + name);
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Account Balance: " + balance);
    }

    void credit(int amount) {
        balance += amount;
        System.out.println("A/C credited with Rs. " + amount + " and Balance: Rs. " + balance);
    }

    void debit(int amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("A/C debited with Rs. " + amount + " and Balance: Rs. " + balance);
        } else {
            System.out.println("Insufficient balance");
        }
    }
}

public class Bank 
{
    public static void main(String[] args) 
    {
        System.out.println("Enter your details");
        int x = 0;
        while(x==0)
        {
            try(Scanner sc  = new Scanner(System.in)){
                System.out.print("Enter your name: ");
                String s = sc.nextLine(); 
                System.out.print("Enter your initial balance: ");
                int balance = sc.nextInt();
                System.out.print("Enter your account number: ");
                int accountNumber = sc.nextInt();
                Account a = new Account(s, accountNumber, balance);
                a.display();
                while(x==0)
                {
                    System.out.println("1. Credit");
                    System.out.println("2. Debit");
                    System.out.println("3. Exit");
                    int choice = sc.nextInt();
                    switch (choice) 
                    {
                        case 1->
                        {
                            System.out.println("Enter the amount you wish to credit: ");
                            int amount = sc.nextInt();
                            a.credit(amount);
                        }
                        case 2->
                        {
                            System.out.println("Enter the amount you wish to debit: ");
                            int amount = sc.nextInt();
                            a.debit(amount);
                        }
                        case 3->
                        {
                            System.out.println("Exiting the program\n");
                            x = 1;
                        }
                    }
                }
            }
        }
    }
}