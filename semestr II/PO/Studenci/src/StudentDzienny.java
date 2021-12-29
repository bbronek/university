public class StudentDzienny extends Student{
    public static int ilosc = 0;

    public StudentDzienny(){
    }

    public StudentDzienny(String index){
        super(index);
        ilosc ++;

    }

    public static int getilosc(){
        return ilosc;
    }


}
