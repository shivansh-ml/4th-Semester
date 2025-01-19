import java.util.*;
class Book
{//Outer class Book Definition
    int id;
    String name;
    Scanner sc;
    Page[] pages;//Inner class Objects Array
    //Inner class Definition
    class Page {//Inner class page definition{
        int[] lines;//array of line to store no of words
        Page(int numlines)//inner class constructor
        {
            lines = new int[numlines];
        }
        void setLines()//intialize the number of words info for every line
        {
            for(int i=0;i<lines.length;i++)
            {
                System.out.println("Enter the no of words for line "+(i+1));
                lines[i]=sc.nextInt();
            }
        }
        int getLines()//return no of lines
        {
            return lines.length;
        }
    }//End of Inner class Definition
    //Outer class Constructor
    Book(int id, String name, int numpages){
        this.id=id;
        this.name=name;
        sc=new Scanner(System.in);
        pages=new Page[numpages];//Array of Objects of page class
        for (int i = 0; i < pages.length; i++) {
            System.out.println("Enter no of lines of page"+(i+1));
            int nlines=sc.nextInt();
            pages[i]=new Page(nlines);//Create inner class page object
            pages[i].setLines();//set the no of words per line
        }
    }
    //Perform Statistics...find total no of words in the book
    public int getNumofWords()
    {
        int now=0;
        // for(int i=0;i<pages.length;i++)//loop for num of pages
        // //loop for no of words per line
        //     for(int j=0;j<pages[i].getLines();j++)
        //         now+=pages[i].lines[j];
        //     return now;
        for (Page page : pages) {
            for (int j = 0; j < page.getLines(); j++) {
                now += page.lines[j];
            }
        }
        return now;
    }//End of Outer class Definition
}
public class Composition_relationship {
    public static void main(String[] args) {
        Book book=new Book(1,"OOPM Book",3);//Create a book with 3 pages 
        int nowords=book.getNumofWords();
        System.out.println("Total Words = "+ nowords);
        System.out.println("Book Name = " + book.name);
        System.out.println("Book ID = "+book.id);
        book.sc.close();
    }
}
