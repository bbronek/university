import java.util.Scanner;

public class NameValidation {
    public static void main(String[] args) throws CustomException {
        Scanner scan = new Scanner(System.in);
        String name = scan.nextLine();
        if (name.equals("Tomasz")) {
            throw new CustomException("You can't be called Tomasz");

        } else {
            System.out.println("Your name is a " + name);
        }
    }
}
