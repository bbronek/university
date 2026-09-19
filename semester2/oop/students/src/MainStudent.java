import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MainStudent {
    public static void main(String[] args) throws IOException {
        List<Student> students = new ArrayList<>();
        try (Scanner scanner = new Scanner(System.in)) {
            do {
                System.out.println("Enter your student ID (f for full-time, p for part-time):");
                if (!scanner.hasNextLine()) break;
                String index = scanner.nextLine().trim();
                if (!index.startsWith("f") && !index.startsWith("p")) {
                    System.out.println("Student ID must begin with f or p");
                    continue;
                }
                Student student = index.startsWith("f")
                        ? new FullTimeStudent(index) : new PartTimeStudent(index);
                System.out.println("Enter your first name:");
                if (!scanner.hasNextLine()) break;
                student.setName(scanner.nextLine());
                System.out.println("Enter your last name:");
                if (!scanner.hasNextLine()) break;
                student.setSurname(scanner.nextLine());
                students.add(student);
                System.out.println("Add another student? Enter y or n:");
                if (!scanner.hasNextLine() || !scanner.nextLine().equalsIgnoreCase("y")) break;
            } while (true);
        }
        try (BufferedWriter writer = Files.newBufferedWriter(Path.of(args.length > 0 ? args[0] : "students.txt"))) {
            for (Student student : students) {
                writer.write(String.join(" ", student.getName(), student.getSurname(), student.getIndex()));
                writer.newLine();
            }
        }
    }
}
