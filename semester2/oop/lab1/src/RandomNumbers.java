import java.util.concurrent.ThreadLocalRandom;

public class RandomNumbers {
    public static void main(String[] args) {
        for (int index = 0; index < 23; ++index) {
            System.out.println(ThreadLocalRandom.current().nextInt(1, 11));
        }
    }
}
