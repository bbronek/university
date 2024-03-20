import java.sql.*;
import io.github.cdimascio.dotenv.Dotenv;

Dotenv dotenv = Dotenv.load();

public class ConnMySQL
{

    public static void main(String[] args) throws ClassNotFoundException {
        Connection conn = null;
        String dbName = dotenv.get("DBNAME") ;
        String dbUserName = dotenv.get("USERNAME");
        String dbPassword = dotenv.get("PASSWORD");
        String connectionString = dotenv.get("URL") + dbName + "?user=" + dbUserName + "&password=" + dbPassword + "&useUnicode=true&characterEncoding=UTF-8";
        Class.forName("com.mysql.cj.jdbc.Driver");
        try {

           conn = DriverManager.getConnection(connectionString);
           Statement stat = conn.createStatement();
           ResultSet rs = stat.executeQuery(dotenv.get("QUERY"));

           while(rs.next()){
               System.out.println(rs.getString(dotenv.get("COLUMN1")) + " " + rs.getString(dotenv.get("COLUMN2")));
           }


        }
        catch (SQLException ex) {
            System.out.println("SQLException: " + ex.getMessage());
            System.out.println("SQLState: " + ex.getSQLState());
            System.out.println("VendorError: " + ex.getErrorCode());
        }
        finally {
            if(conn != null)
            {
                try
                {
                    conn.close();
                }
                catch(Exception e) {
                    System.out.println(e.getMessage());
                }
            }
        }
    }
}
