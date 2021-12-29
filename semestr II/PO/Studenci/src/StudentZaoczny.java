public class StudentZaoczny extends Student {
    public static int ilosc = 0;

    public StudentZaoczny(){}

    public StudentZaoczny(String index){
        super(index);
        ilosc ++;
    }

    public static int getIlosc(){
        return ilosc;
    }


}
