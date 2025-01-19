class Room {
    float length;
    float breadth;
    void getdata(float a, float b)
    {
        length = a;
        breadth =b;
    }
}
class RoomArea
{
    public static void main(String args[])
    {
    float area;
    Room room1 = new Room();//Creates an object room1  
    room1.getdata(10.5f, 20.5f);//Passes values to length and breadth
    area=room1.length*room1.breadth;
    System.out.println("Area = "+area);
    }
}

/*
Room class contains two variables and one method to assign value to these variables.
RoomArea contains the main method that initiates the execution.
room1 assign values to the data members of room using the getdata method. 
*/


