public class ComparisonExample {
    public static void main(String[] args) {
        String first = new String("example");
        String second = new String("example");
        String alias = first;
        System.out.println("first == second: " + (first == second));
        System.out.println("first == alias: " + (first == alias));
        System.out.println("first equals second: " + first.equals(second));
    }
}
