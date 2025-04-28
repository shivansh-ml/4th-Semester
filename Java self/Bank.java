import java.util.*;
class Account{
    String name;
    int balance;
    int accountNumber;

    Account(String name,int balance,int accountNumber){
        this.name = name;
        this.accountNumber=accountNumber;
        this.balance=balance;
    }

    void display(){
        System.out.println("Account Number: "+accountNumber);
        System.out.println("Account Holder Name: "+name);
        System.out.println("Account Balance: "+balance);
    }

    void credit(int amount){
        balance += amount;
        System.out.println("Account Balance after credit: "+balance);
    }

    void debit(int amount){
        if (amount > balance) {
            System.out.println("Insufficient balance");
            return;
        }
        balance -= amount;
        System.out.println("Account Balance after debit: "+balance);
    }
}
public class Bank{
    public static void main(String[] args) {
        Account account = new Account("John Doe", 1000, 12345);
        account.display();
        account.credit(500);
        account.debit(2000);
        Scanner sc =  new Scanner (System.in);
        System.out.println("Enter the amount to be credited:");
        int amount = sc.nextInt();
        account.credit(amount);
        sc.close();
}
}
