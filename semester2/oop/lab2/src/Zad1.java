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

class StudentDzienny extends Student
{
    private static int ilosc = 0;
    public StudentDzienny(String Index)
    {
        super(Index);
        ilosc ++;
    }
    public static int getilosc()
    {
        return ilosc;
    }
}

class StudentZaoczny extends Student
{
    private static int ilosc = 0;
    public StudentZaoczny(String Index)
    {
        super(Index);
        ilosc ++;
    }
    public static int getilosc()
    {
        return ilosc;
    }
}

public class Zad1 {
    public static void main(String[] args) {
        Student s1 = new StudentZaoczny("123456");
        Student s2 = new StudentDzienny("234567");
        Student s3 = new StudentDzienny("345678");
        Student s4 = new StudentZaoczny("456789");
        Student s5 = new StudentDzienny("111111");

        s1.setIndex("9997");
        System.out.println("Dzienni: "+ StudentDzienny.getilosc());
        System.out.println("Zaoczni: "+ StudentZaoczny.getilosc());
        System.out.println("");
        System.out.println("Student 1: "+s1.getIndex());
        System.out.println("Student 2: "+s2.getIndex());
        System.out.println("Student 3: "+s3.getIndex());
        System.out.println("Student 4: "+s4.getIndex());
        System.out.println("Student 5: "+s5.getIndex());
    }
}
