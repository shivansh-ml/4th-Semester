class BoolPattern {
    boolean A, B, C;

    void display(boolean A) {
        boolean i = false;
        int c = 0;
        do {
            if (c != 0) {
                i = true;
            }
            if (i == false) {
                System.out.print(0 + ",");
            } else {
                System.out.print(1);
            }
            c++;
        } while (i != A);
    }

    void display(boolean A, boolean B) {
        boolean i = false, j = false;
        int a = 0, b = 0;
        do {
            if (a != 0) {
                i = true;
            }
            j = false;
            b = 0;
            do {
                if (b != 0) {
                    j = true;
                }
                if (i == false) {
                    System.out.print(0);
                } else {
                    System.out.print(1);
                }
                if (j == false) {
                    System.out.print(0 + ",");
                } else {
                    System.out.print(1 + ",");
                }
                b++;
            } while (j != B);
            a++;
        } while (i != A);
    }

    void display(boolean A, boolean B, boolean C) {
        boolean i = false, j = false, k = false;
        int a = 0, b = 0, c = 0;
        do {
            if (a != 0) {
                i = true;
            }
            j = false;
            k = false;
            b = 0;
            c = 0;
            do {
                if (b != 0) {
                    j = true;
                }
                k = false;
                c = 0;
                do {
                    if (c != 0) {
                        k = true;
                    }
                    if (i == false) {
                        System.out.print(0);
                    } else {
                        System.out.print(1);
                    }
                    if (j == false) {
                        System.out.print(0);
                    } else {
                        System.out.print(1);
                    }
                    if (k == false) {
                        System.out.print(0 + ",");
                    } else {
                        System.out.print(1 + ",");
                    }
                    c++;
                } while (k != C);
                b++;
            } while (j != B);
            a++;
        } while (i != A);

    }
}

public class Bool {
    public static void main(String[] args) {
        BoolPattern bp = new BoolPattern();
        System.out.println("BoolPattern for one variable");
        bp.display(true);
        System.err.println();
        System.out.println("BoolPattern for two variable");
        bp.display(true, true);
        System.out.println();
        System.out.println("BoolPattern for three variable");
        bp.display(true, true, true);
    }
}