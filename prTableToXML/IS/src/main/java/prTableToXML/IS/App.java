package prTableToXML.IS;

import java.io.IOException;
import java.sql.SQLException;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    	GenericSqlConnection con = new MySQLConnection();
    	try {
			con.connect("bbtrack");
	    	con.executeQuery("SELECT compound_id FROM names where name like 'water'");
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

    }
}
