import java.util.Arrays;
import java.util.Scanner;

public class Zad2 {
    public static void main(String[] args) {
        String[] v;
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        v = new String[n];
        scan.nextLine();
        for(int i=0;i<n;++i){
            System.out.println("Print your surname");
            v[i] = scan.nextLine();
        }
        Arrays.sort(v);
        for(int i=0;i<n;++i){
            System.out.println(v[i] +" "+ v[i].length());

        }

    }
}
