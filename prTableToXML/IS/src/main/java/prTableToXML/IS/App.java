package prTableToXML.IS;

import java.io.FileWriter;
import java.io.IOException;
import java.sql.SQLException;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws IOException
    {
    	try {
        	GenericSqlConnection con = new GenericSqlConnection("prueba.xml");
	    	con.addPaciente("SELECT * FROM PACIENTE;");
	    	con.closeFW();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			System.out.println("Error al conectar!!!!!");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	
    }
}
