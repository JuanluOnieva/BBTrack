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
public class xmlPacienteMedico 
{
    public static void main( String[] args ) throws IOException
    {
    	try {
        	SQLtoXML con = new SQLtoXML();
        	List<String> allIdPaciente = con.getIdPaciente("SELECT * FROM PACIENTE;");
        	for(String id : allIdPaciente) {
        		con.initXML("pruebaXSL.xsl", "document.xsd", "Pacientes/"+id+".xml");
        		con.addPaciente("SELECT * FROM PACIENTE where idPaciente=" + id + ";");
        		con.endXML();
        		con.closeFW();
	    	
        	}
        	
        	List<String> allIdMedico = con.getIdMedico("SELECT * FROM MEDICO;");
        	for(String id : allIdMedico) {
        		con.initXML("pruebaXSL.xsl", "document.xsd", "Medicos/"+id+".xml");
        		con.addMedico("SELECT m.Licencia, m.Nombre, m.Apellidos, m.Sexo, m.Especialidad FROM Medico m WHERE Licencia=\""+id + "\";", id);
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
