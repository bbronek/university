public class PartTimeStudent extends Student {
    private static int count = 0;

    public PartTimeStudent() { this(""); }

    public PartTimeStudent(String index) {
        super(index);
        count++;
    }

    public static int getCount() { return count; }
}
