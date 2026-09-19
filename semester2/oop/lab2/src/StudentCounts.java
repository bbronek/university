abstract class Student {

    String Index;
    public Student (String Index)
    {
        this.Index = Index;
    }
    public void setIndex(String Index)
    {
        this.Index = Index;
    }
    public String getIndex()
    {
        return this.Index;
    }
}

class FullTimeStudent extends Student
{
    private static int count = 0;
    public FullTimeStudent(String Index)
    {
        super(Index);
        count ++;
    }
    public static int getCount()
    {
        return count;
    }
}

class PartTimeStudent extends Student
{
    private static int count = 0;
    public PartTimeStudent(String Index)
    {
        super(Index);
        count ++;
    }
    public static int getCount()
    {
        return count;
    }
}

public class StudentCounts {
    public static void main(String[] args) {
        Student s1 = new PartTimeStudent("123456");
        Student s2 = new FullTimeStudent("234567");
        Student s3 = new FullTimeStudent("345678");
        Student s4 = new PartTimeStudent("456789");
        Student s5 = new FullTimeStudent("111111");

        s1.setIndex("9997");
        System.out.println("Full-time: "+ FullTimeStudent.getCount());
        System.out.println("Part-time: "+ PartTimeStudent.getCount());
        System.out.println("");
        System.out.println("Student 1: "+s1.getIndex());
        System.out.println("Student 2: "+s2.getIndex());
        System.out.println("Student 3: "+s3.getIndex());
        System.out.println("Student 4: "+s4.getIndex());
        System.out.println("Student 5: "+s5.getIndex());
    }
}
