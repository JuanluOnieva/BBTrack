package prTableToXML.IS;

import java.io.File;
import java.io.IOException;
import java.sql.SQLException;
import java.util.List;
public class main {

	public static void main(String[] args)  throws IOException, SQLException {
		// TODO Auto-generated method stub
		if(args.length < 3) {
			new RuntimeException("Se requieren al menos tres parámetros: Usuario Pss BD");
		}
		
    	SQLtoXML con = new SQLtoXML(args[0], args[1]);

		if(args[2].equals("bbTrack")) {
			System.out.println("XML de " + args[2]);
			try {
	        	con.initXML("XSLHome.xsl", "XSDGeneral.xsd", "bbTrack.xml");
		    	con.addAllPaciente("SELECT * FROM PACIENTE;");
		    	con.addAllMedico("SELECT * FROM MEDICO;");
		    	con.addAllConsulta("Select * from Consulta");
		    	con.addAllICD("Select * from ICD_10");
		    	con.endXML();
		    	con.closeFW();
		    	
		    	List<String> allIdPaciente = con.getIdPaciente("SELECT * FROM PACIENTE;");
	        	
	        	File pacientes = new File("Pacientes");
	        	if(!pacientes.exists())
	        		pacientes.mkdirs();

	        	
	        	for(String id : allIdPaciente) {
	        		con.initXML("XSLPaciente.xsl", "XSDPaciente.xsd", "Pacientes/"+id+".xml");
	        		con.addPaciente("SELECT * FROM PACIENTE where idPaciente=" + id + ";");
	        		con.endXML();
	        		con.closeFW();
		    	
	        	}
	        	
	        	File medicos = new File("Medicos");
	        	if(!medicos.exists())
	        		medicos.mkdirs();

	        	
	        	List<String> allIdMedico = con.getIdMedico("SELECT * FROM MEDICO;");
	        	for(String id : allIdMedico) {
	        		con.initXML("XSLMedico.xsl", "XSDMedico.xsd", "Medicos/"+id+".xml");
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
		else if(args[2].equals("Pacientes")){
	    	try {	        	
	        	if(args.length == 4) {
	        		
	    			System.out.println("XML de " + args[3]);
	        		
		        	List<String> allIdPaciente = con.getIdPaciente("SELECT * FROM PACIENTE WHERE idPaciente = '" + args[3] + "';");
		        	
		        	File pacientes = new File("Paciente");
		        	if(!pacientes.exists())
		        		pacientes.mkdirs();

		        	
		        	for(String id : allIdPaciente) {
		        		con.initXML("XSLPaciente.xsl", "XSDPaciente.xsd", "Paciente/"+id+".xml");
		        		con.addPaciente("SELECT * FROM PACIENTE where idPaciente=" + id + ";");
		        		con.endXML();
		        		con.closeFW();
			    	
		        	}
	        	}else {
	        	
	    			System.out.println("XML de " + args[2]);
	        		
		        	List<String> allIdPaciente = con.getIdPaciente("SELECT * FROM PACIENTE;");
		        	
		        	File pacientes = new File("Pacientes");
		        	if(!pacientes.exists())
		        		pacientes.mkdirs();
	
		        	
		        	for(String id : allIdPaciente) {
		        		con.initXML("XSLPaciente.xsl", "XSDPaciente.xsd", "Pacientes/"+id+".xml");
		        		con.addPaciente("SELECT * FROM PACIENTE where idPaciente=" + id + ";");
		        		con.endXML();
		        		con.closeFW();
			    	
		        	}
	        	}	
	        	
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				System.out.println("Error al conectar!!!!!");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}else if(args[2].equals("Medicos")) {
	    	try {	        
    			System.out.println("XML de " + args[2]);
	    		
	        	File medicos = new File("Medicos");
	        	if(!medicos.exists())
	        		medicos.mkdirs();

	        	
	        	List<String> allIdMedico = con.getIdMedico("SELECT * FROM MEDICO;");
	        	for(String id : allIdMedico) {
	        		con.initXML("XSLMedico.xsl", "XSDMedico.xsd", "Medicos/"+id+".xml");
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

}
