import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;


public class App {

    /**
     * @param inh
     * @param listInhabitants
     * @return b
     */

    public static boolean modifyData(Inhabitant inh, List<Inhabitant> listInhabitants ){
        boolean b = true;
        for(Inhabitant x : listInhabitants) {
            if (x.pesel.equals(inh.pesel)){
                b = false;
                x.setMiasto(inh.miasto);
                x.setImie(inh.imie);
                x.setNazwisko(inh.nazwisko);
            }
        }
        return b;
    }

    /**
     * @param pesel
     * @throws PeselException
     * @return
     */

    public static void checkPesel(String pesel) throws PeselException{
        int sum = 0, n;
        char ch;

        for(int i = 0; i < pesel.length(); ++i)
        {
            ch = pesel.charAt(i);
            n = Character.getNumericValue(ch) * (i+1);
            sum += n;

        }
        int m = sum%10;
        int df = 10 - m;


        if (pesel.length() != 11) {
            throw new PeselException("Nie poprawna dlugosc peselu");
        }

        else if (df != Integer.parseInt(String.valueOf(pesel.charAt(pesel.length() - 1)))) {
            throw new PeselException("Nie poprawna cyfra kontrolna");
        }



    }

    /**
     * @param args
     * @throws IOException
     * Example of use:
     *  Prosze podaj mi nazwe swojego miasta:
     *      > Poznan
     *  Podaj imie, nazwisko, pesel:
     *      > Jan Kowalski 53011337928
     *  Chcesz dodadc nastepnego mieszkanca? Wpisz litere t lub n:
     *      > n
     *      > Task execution finished 'App.main()'.
     */

    public static void main(String[] args) throws IOException {

        List<Inhabitant> listInhabitants = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        String runAgain;
        do {
            Inhabitant inh = new Inhabitant();
            System.out.println("Prosze podaj mi nazwe swojego miasta: ");

            inh.setMiasto(scanner.nextLine());

            System.out.println("Podaj imie, nazwisko, pesel");
            String data = scanner.nextLine();
            String[] dataArray = data.split(" ");

            try {
                checkPesel(dataArray[2]);
            } catch (PeselException pex) {
                System.out.println(pex);
            }

            inh.setImie(dataArray[0]);
            inh.setNazwisko(dataArray[1]);
            inh.setPesel(dataArray[2]);

            if(modifyData(inh, listInhabitants)){
                listInhabitants.add(inh);
            }


            System.out.println("Chcesz dodac nastepnego mieszkanca? Wpisz litere t lub n.");
            runAgain = scanner.nextLine();

        } while (runAgain.equals("t"));

        scanner.close();


        FileWriter writer = new FileWriter("mieszkancy.txt");
        for(Inhabitant inh : listInhabitants) {
            writer.write(inh.miasto+ " " + inh.imie + " " + inh.nazwisko + " " + inh.pesel + "\n");
        }
        writer.close();
    }

}
