package prTableToXML.IS;

import java.io.FileWriter;
import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 * Hello world!
 *
 */
public class xmlPaciente 
{
    public static void main( String[] args ) throws IOException
    {
    	try {
        	SQLtoXML con = new SQLtoXML();
        	System.out.println("hola");
        	List<String> allIdPaciente = con.getIdPaciente("SELECT * FROM PACIENTE;");
        	for(String id : allIdPaciente) {
        		con.initXML("pruebaXSL.xsl", "document.xsd", id+".xml");
        		con.addPaciente("SELECT * FROM PACIENTE where idPaciente=" + id + ";");
        		con.endXML();
        		con.closeFW();
	    	
        	}
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
