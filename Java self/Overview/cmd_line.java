class cmd_line {
    public static void main(String args[]) {
        int count, i=0;
        String string;
        count=args.length;
        System.out.println("Number of arguments = "+count);
        while(i<count)
        {
            string=args[i];
            i=i+1;
            System.out.println(i+" : "+"Java is "+string+"!");
            // System.out.println("Argument "+(i+1)+" = "+string);
        }
    }    
}
/*
 Args is declared as an array of strings (string objects) Any arguments provided in the command line at time of execution is passed to args as its elements
Pass this in the terminal---java cmd_line Simple Object_Oriented Distributed Robust Secure Portable Multithreaded Dynamic 
 */