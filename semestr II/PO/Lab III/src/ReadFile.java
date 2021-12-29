import java.io.File;
//import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class ReadFile {
    public static void main(String[] args) throws IOException {
        File file = new File("/home/bbronek/Desktop/Lab III/src/helloo");
        Scanner scan = new Scanner(file);

        String fileContent = "";
        while(scan.hasNextLine()){
            fileContent = fileContent.concat(scan.nextLine() + '\n');
        }
        scan.close();

        System.out.println(fileContent);

        FileWriter writer = new FileWriter("/home/bbronek/Desktop/Lab III/src/output");

        writer.write(fileContent);
        writer.close();


    }
}
