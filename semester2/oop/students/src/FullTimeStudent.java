public class FullTimeStudent extends Student {
    private static int count = 0;

    public FullTimeStudent() { this(""); }

    public FullTimeStudent(String index) {
        super(index);
        count++;
    }

    public static int getCount() { return count; }
}
