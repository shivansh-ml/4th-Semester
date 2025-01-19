class helloworld
{
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
//main function is the entry point of the program or the starting point for the interpreter to take the exam.
//public is an acess specifier declares the main as unprotected.
//static declares the main as one that belongs to entire class and not  apart of objects of the class. 
//main must always be declared static since interpreter uses this method before any objects are created.
//void specifies that main does not return any value but simply prints some text to the screen.
//println->member of OUT object->static data member ofSystem class.

/*
General structure of a Java Program---
Documentation Section---------Suggested
Package Statement-------------Optional
import Statement--------------Optional
Interface Statement-----------Optional
Class defintions--------------Optional
Main method class-------------Essential
{
    Main method definition----Essential
    {
        1. Variable declarations
        2. Method declarations
        3. Method calls
    }
}
*/

//package statement informs the compiler that the classes defined here belong to this packages.Eg-package student;
//Eg-import student.test; import statement allows the classes defined in the student package to be used in this package.
//Interface is like a class but includes a group of method declarations.
//classes are used to map the objects in the real world to the objects in the program.
