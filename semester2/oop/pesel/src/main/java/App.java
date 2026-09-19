import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {
    public static boolean modifyData(Inhabitant inhabitant, List<Inhabitant> inhabitants) {
        for (Inhabitant existing : inhabitants) {
            if (existing.getPesel().equals(inhabitant.getPesel())) {
                existing.setCity(inhabitant.getCity());
                existing.setFirstName(inhabitant.getFirstName());
                existing.setLastName(inhabitant.getLastName());
                return false;
            }
        }
        return true;
    }

    public static void checkPesel(String pesel) throws PeselException {
        if (pesel == null || !pesel.matches("[0-9]{11}")) {
            throw new PeselException("PESEL must contain exactly 11 digits");
        }
        int[] weights = {1, 3, 7, 9, 1, 3, 7, 9, 1, 3};
        int sum = 0;
        for (int index = 0; index < weights.length; ++index) {
            sum += (pesel.charAt(index) - '0') * weights[index];
        }
        if ((10 - sum % 10) % 10 != pesel.charAt(10) - '0') {
            throw new PeselException("Invalid PESEL check digit");
        }
    }

    public static void main(String[] args) throws IOException {
        List<Inhabitant> inhabitants = new ArrayList<>();
        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                System.out.println("Enter your city:");
                if (!scanner.hasNextLine()) break;
                String city = scanner.nextLine();
                System.out.println("Enter first name, last name, and PESEL:");
                if (!scanner.hasNextLine()) break;
                String[] fields = scanner.nextLine().trim().split("\\s+");
                try {
                    if (fields.length != 3) throw new PeselException("Expected three fields");
                    checkPesel(fields[2]);
                    Inhabitant inhabitant = new Inhabitant();
                    inhabitant.setCity(city);
                    inhabitant.setFirstName(fields[0]);
                    inhabitant.setLastName(fields[1]);
                    inhabitant.setPesel(fields[2]);
                    if (modifyData(inhabitant, inhabitants)) inhabitants.add(inhabitant);
                } catch (PeselException exception) {
                    System.out.println(exception.getMessage());
                }
                System.out.println("Add another inhabitant? Enter y or n:");
                if (!scanner.hasNextLine() || !scanner.nextLine().equalsIgnoreCase("y")) break;
            }
        }
        Path output = Path.of(args.length > 0 ? args[0] : "inhabitants.txt");
        try (BufferedWriter writer = Files.newBufferedWriter(output)) {
            for (Inhabitant inhabitant : inhabitants) {
                writer.write(String.join(" ", inhabitant.getCity(), inhabitant.getFirstName(),
                        inhabitant.getLastName(), inhabitant.getPesel()));
                writer.newLine();
            }
        }
    }
}
