class Box 
{
    double width ;
    double height ;
    double depth ;
    //compute and return volume
    double volume ( ) {
    return width * height * depth ;
    }
    //sets dimensions of Box
    void setDim (double w, double h , double d ) {
    width = w;
    height = h ;
    depth = d ;
    }
}
    public class boxdem {
    public static void main (String args [ ] ) {
    Box mybox = new Box ( ) ;
    double vol ;
    //initialize mybox
    mybox.setDim (10 , 20 , 15) ;
    //get volume of box
    vol = mybox . volume ( ) ;
    System.out.println("Volume : " + vol ) ;
    }
}