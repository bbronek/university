class GenerateRandomNumber {
    public void gen(int a,int b,int n){
        double r = 0;
        int c =0;
        while(c<n){
            r = Math.random()*b+a;
            System.out.println(Math.round(r));
            ++c;
        }
    }
}
public class RandomNumbers {
    public static void main(String[] args) {
        GenerateRandomNumber g = new GenerateRandomNumber();
        g.gen(1,10,23);
    }


}
