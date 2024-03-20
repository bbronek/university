public class Zad1 {
    public static void main(String[] args) {
        try {
            System.out.println(4/0);
        }
        catch(Exception e) {
            System.out.println("You can't  " + e.getMessage());
        }
    }
}
