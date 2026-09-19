import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class ReadFile {
    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            System.err.println("Usage: java ReadFile <source> <destination>");
            return;
        }
        String content = Files.readString(Path.of(args[0]));
        System.out.print(content);
        Files.writeString(Path.of(args[1]), content);
    }
}
