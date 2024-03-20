import java.util.*;
import java.io.FileWriter;
import java.io.IOException;

public class MainStudent {

    public static void main(String[] args) throws IOException
    {
        String dz;
        List<Student> listStudent = new ArrayList<>();

        Scanner scanner = new Scanner(System.in);

        String runAgain;
        do {
            StudentDzienny std = new StudentDzienny();
            StudentZaoczny stz = new StudentZaoczny();
            System.out.println("Proszę podaj swój numer indeksu:");
            dz = scanner.nextLine();
            if (dz.substring(0, 1).equals("d"))
                std.setIndex(dz);
            else
                stz.setIndex(dz);

            System.out.println("Proszę podaj swoje imię");
            if (dz.substring(0, 1).equals("d"))
                std.setName(scanner.nextLine());
            else
                stz.setName(scanner.nextLine());

            System.out.println("Proszę podaj swoje nazwisko:");
            if (dz.substring(0, 1).equals("d"))
                std.setSurname(scanner.nextLine());
            else
                stz.setSurname(scanner.nextLine());

            if (dz.substring(0, 1).equals("d"))
                listStudent.add(std);
            else
                listStudent.add(stz);

            System.out.println("Chcesz wykonać kolejne działanie? Wpisz literę t lub n.");
            runAgain = scanner.nextLine();

        } while (runAgain.equals("t"));

        scanner.close();

        FileWriter writer = new FileWriter("studenci.txt");
        for(Student st : listStudent) {
            writer.write(st.name + " " + st.surname + " " + st.index + "\n");
        }
        writer.close();
    }

}