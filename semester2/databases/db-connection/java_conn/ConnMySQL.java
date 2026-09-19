import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class ConnMySQL {
    private static String environment(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException("Missing environment variable: " + name);
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        String url = environment("URL") + environment("DBNAME");
        try (Connection connection =
                 DriverManager.getConnection(url, environment("DBUSER"), environment("PASSWORD"));
             Statement statement = connection.createStatement();
             ResultSet rows = statement.executeQuery(environment("QUERY"))) {
            while (rows.next()) {
                System.out.println(rows.getString(environment("COLUMN1")) + " " +
                                   rows.getString(environment("COLUMN2")));
            }
        }
    }
}
