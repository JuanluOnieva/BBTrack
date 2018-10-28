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
        	SQLtoXML con = new SQLtoXML("prueba.xml");
        	con.initXML("pruebaXSL.xsl", "document.xsd");
	    	con.addPaciente("SELECT * FROM PACIENTE;");
	    	con.endXML();
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
