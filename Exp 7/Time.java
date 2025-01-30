class TimeFormat {
    int hr;
    int min;
    int ss;

    TimeFormat() {
        hr = 0;
        min = 0;
        ss = 0;
    }

    TimeFormat(int ss) {
        hr = 0;
        min = 0;
        this.ss = ss;
    }

    TimeFormat(int min, int ss) {
        hr = 0;
        this.min = min;
        this.ss = ss;
    }

    TimeFormat(int hr, int min, int ss) {
        this.hr = hr;
        this.min = min;
        this.ss = ss;
    }

    void display() {
        System.out.println("Time is ->"+hr+":"+min+":"+ss);
    }
}

class Time {
    public static void main(String[] args) {
        TimeFormat tf = new TimeFormat();
        tf.display();
        TimeFormat tf1 = new TimeFormat(30);
        tf1.display();
        TimeFormat tf2 = new TimeFormat(01, 30);
        tf2.display();
        TimeFormat tf3 = new TimeFormat(01, 30, 45);
        tf3.display();
    }
}