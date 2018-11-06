package prTableToXML.IS;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Properties;

/**
 * 
 * @author marcomunozperez
 * TODO Add query exceptions
 */

public class SQLtoXML {
	
	protected Connection connection;
	FileWriter pw;
	
	public SQLtoXML() throws SQLException, IOException {

		String connectionString = "jdbc:mysql://localhost/bbTrack?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC"; 
		
		connection = DriverManager.getConnection(connectionString, "root", "bbtrack123");

	}
	
	public void initXML(String schema, String xsd, String file) throws IOException {
		File fichero = new File(file);
       	pw = new FileWriter(fichero, true);
       	
		pw.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
		pw.write("<?xml-stylesheet type=\"text/xsl\" href=\"" + schema + "\"?>\n");
		pw.write("<bbTrack xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"" + xsd + "\">\n");
	}
	
	public void endXML() throws IOException {
		pw.write(endLabel("bbTrack"));
	}
	
	public ResultSet executeQuery(String s) throws IOException, SQLException{
		// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			//execute query
			try (ResultSet rs = stmt.executeQuery(s)){
				return(rs);
			}
			catch (SQLException e) {
				e.printStackTrace();
			} 
		}
		
		return null;
	}
	
	public void addPaciente(String s) throws IOException{
		//// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			////execute query

			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
				
				List<String> all_id = getIdPaciente(rs);
								
				for(String id : all_id) {
					ResultSet rsPaciente = stmt.executeQuery("SELECT p.idPaciente, p.NUSS, p.Nombre , p.Apellidos, p.Sexo, p.Fecha_Nacimiento, p.Domicilio, p.Localidad, p.Correo_electronico, p.Telefono, p.Embarazada FROM PACIENTE p WHERE idPaciente="+id);
					xmlPaciente(rsPaciente);

					ResultSet rsHistorial = stmt.executeQuery("SELECT h.idHistorial, h.Fecha_primera_consulta, h.Vacunas FROM HISTORIAL h WHERE h.idPaciente="+id);
					xmlHistorial(rsHistorial);
					
					try(ResultSet rsFRP = stmt.executeQuery("SELECT f.Antecedentes_familiares, f.Factores_psicosociales, f.Antecedentes_obstetricos, f.Antecedentes_personales, f.Patologia_materna, f.Riesgos_especificos, f.Exposicion_a_teratogenos " + 
							" FROM HISTORIAL h, Factor_de_riesgo_prenatal f WHERE h.idPaciente="+id +" and h.idHistorial=f.idHistorial"))
					{xmlFRP(rsFRP);}
					catch(SQLException e) {
						xmlFRP(null);
					}
										
					ResultSet rsInforme = stmt.executeQuery("SELECT idInforme FROM INFORME WHERE idHistorial=\"H-"+id + "\";");
					
					List<String> all_id_Informe = new ArrayList<String>();
					all_id_Informe.addAll(getIdInforme(rsInforme));
					
					if(all_id_Informe.isEmpty()) {
						
						xmlInforme(null);
						xmlPrueba(null);
						xmlICD(null);
						
						pw.write(endLabel("Informe", 4));
					}
					
					for(String idInforme : all_id_Informe) {
												
						rsInforme = stmt.executeQuery("SELECT i.idInforme, i.Licencia_medico, i.Estado_paciente, i.Diagnostico, i.idConsulta, i.Fecha_consulta, a.Es_urgente, a.Sintomas" + 
								" FROM asiste_a a, informe i where a.idConsulta=i.idConsulta and a.Fecha_consulta=i.Fecha_consulta and i.idInforme=\"" + idInforme + "\" ;");
						
						xmlInforme(rsInforme);						
						
						ResultSet rsICD10 = stmt.executeQuery("Select Codigo from informe_icd_10 where idInforme=\"" + idInforme + "\"");
						xmlICD(rsICD10);
						
						ResultSet rsPrueba = stmt.executeQuery("SELECT p.idPrueba, p.idPrueba_externo, p.Nombre, p.Observaciones, p.Tipo FROM PRUEBA p WHERE p.idInforme=\""+idInforme+"\";");
						xmlPrueba(rsPrueba);
						
						 
						pw.write(endLabel("Informe", 4));
					}
					
					pw.write(endLabel("Historial", 3));
					
					pw.write(endLabel("Paciente", 2));


				}
				
			}
		} catch (SQLException e) {
			e.getMessage();
		}
	}
	
	
	public void addAllPaciente(String s) throws IOException{
		//// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			////execute query

			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
				
				pw.write(startLabel("Pacientes", 1) + "\n");
				
				List<String> all_id = getIdPaciente(rs);
				for(String id : all_id) {
					ResultSet rsPaciente = stmt.executeQuery("SELECT p.idPaciente, p.NUSS, p.Nombre , p.Apellidos, p.Sexo, p.Fecha_Nacimiento, p.Domicilio, p.Localidad, p.Correo_electronico, p.Telefono, p.Embarazada FROM PACIENTE p WHERE idPaciente="+id);
					xmlPaciente(rsPaciente);

					ResultSet rsHistorial = stmt.executeQuery("SELECT h.idHistorial, h.Fecha_primera_consulta, h.Vacunas FROM HISTORIAL h WHERE h.idPaciente="+id);
					xmlHistorial(rsHistorial);
					
					try(ResultSet rsFRP = stmt.executeQuery("SELECT f.Antecedentes_familiares, f.Factores_psicosociales, f.Antecedentes_obstetricos, f.Antecedentes_personales, f.Patologia_materna, f.Riesgos_especificos, f.Exposicion_a_teratogenos " + 
							" FROM HISTORIAL h, Factor_de_riesgo_prenatal f WHERE h.idPaciente="+id +" and h.idHistorial=f.idHistorial"))
					{xmlFRP(rsFRP);}
					catch(SQLException e) {						
						xmlFRP(null);
					}
					ResultSet rsInforme = stmt.executeQuery("SELECT idInforme FROM INFORME WHERE idHistorial=\"H-"+id + "\";");
					
					List<String> all_id_Informe = new ArrayList<String>();
					all_id_Informe.addAll(getIdInforme(rsInforme));
					
					
					if(all_id_Informe.size()==0) {
						xmlInforme(null);
						xmlICD(null);
						xmlPrueba(null);
						
						pw.write(endLabel("Informe", 4));
					}
					
					for(String idInforme : all_id_Informe) {
												
						rsInforme = stmt.executeQuery("SELECT i.idInforme, i.Licencia_medico, i.Estado_paciente, i.Diagnostico, i.idConsulta, i.Fecha_consulta, a.Es_urgente, a.Sintomas" + 
								" FROM asiste_a a, informe i where a.idConsulta=i.idConsulta and a.Fecha_consulta=i.Fecha_consulta and i.idInforme=\"" + idInforme + "\" ;");
						xmlInforme(rsInforme);						
						
						ResultSet rsICD10 = stmt.executeQuery("Select Codigo from informe_icd_10 where idInforme=\"" + idInforme + "\"");
						xmlICD(rsICD10);
						
						ResultSet rsPrueba = stmt.executeQuery("SELECT p.idPrueba, p.idPrueba_externo, p.Nombre, p.Observaciones, p.Tipo FROM PRUEBA p WHERE p.idInforme=\""+idInforme+"\";");
						xmlPrueba(rsPrueba);
						
						 
						pw.write(endLabel("Informe", 4));
					}
					
					pw.write(endLabel("Historial", 3));
					
					pw.write(endLabel("Paciente", 2));
				}
				pw.write(endLabel("Pacientes", 1));
			}
		} catch (SQLException e) {
			e.getMessage();
		}
	}
	
	public void addAllMedico(String s) throws IOException, SQLException{
		//// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			////execute query

			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
				
				pw.write(startLabel("Medicos", 1) + "\n");
				
				List<String> all_id = getIdMedico(rs);
				for(String id : all_id) {
					ResultSet rsMedico = stmt.executeQuery("SELECT m.Licencia, m.Nombre, m.Apellidos, m.Sexo, m.Especialidad FROM Medico m WHERE Licencia=\""+id + "\";");
					xmlMedico(rsMedico);
										
					ResultSet rsConsulta = stmt.executeQuery("SELECT idConsulta from atiende WHERE Licencia=\""+id + "\";");
					xmlAtiende(rsConsulta);
					
					pw.write(endLabel("Medico", 2));
				}
				pw.write(endLabel("Medicos", 1));
			}
		} catch (SQLException e) {
			e.getMessage();
		}
	}
	
	public void addMedico(String s) throws IOException, SQLException{
		//// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			////execute query

			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
								
					xmlMedico(rs);
			}
		} catch (SQLException e) {
			e.getMessage();
		}
	}
	
	public void addMedico(String s, String id) throws IOException, SQLException{
		//// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			////execute query

			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
				
					xmlMedico(rs);
					
					ResultSet rsConsulta = stmt.executeQuery("SELECT idConsulta from atiende WHERE Licencia=\""+id + "\";");
					xmlAtiende(rsConsulta);
					
					pw.write(endLabel("Medico", 2));
			}
		} catch (SQLException e) {
			e.getMessage();
		}
	}
	
	public void addAllICD(String s) throws IOException, SQLException{
		//// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			////execute query

			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
				
				pw.write(startLabel("ICD_10_Pregnancy", 1) + "\n");
				xmlAllICD(rs);
				pw.write(endLabel("ICD_10_Pregnancy", 1));

			}
		} catch (SQLException e) {
			e.getMessage();
		}
	}
	
	public void addAllConsulta(String s) throws IOException, SQLException{
		//// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			////execute query

			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
				pw.write(startLabel("Consultas", 1) + "\n");
				xmlConsulta(rs);
				pw.write(endLabel("Consultas", 1));

			}
		} catch (SQLException e) {
			e.getMessage();
		}
	}
	
	public void xmlPaciente(ResultSet result) throws IOException, SQLException {
        HashMap<String,String> idHash = new HashMap<>();
       
        String idPaciente = null;
        String NUSS = null;
        String Nombre = null;
		String Apellidos = null;
		String Sexo = null;
		String Fecha_nacimiento = null;
		String Domicilio = null;
		String Localidad = null;
		String Correo_electronico = null;
		String Telefono = null;
		boolean Embarazada = false;
        
        while (result.next()) {
        	idPaciente = result.getString("idPaciente");
        	NUSS = result.getString("NUSS");
        	Nombre = result.getString("Nombre");
        	Apellidos = result.getString("Apellidos");
        	Sexo = result.getString("Sexo");
        	Fecha_nacimiento = result.getString("Fecha_nacimiento");
        	Domicilio = result.getString("Domicilio");
        	Localidad = result.getString("Localidad");
        	Correo_electronico = result.getString("Correo_electronico");
        	Telefono = result.getString("Telefono");
        	Embarazada = result.getBoolean("Embarazada");
        }
        
        idHash.put("idPaciente", idPaciente);
		pw.write(startLabel("Paciente", idHash, 2));
		pw.write(startEndLabel("NUSS", NUSS, 3));
		pw.write(startEndLabel("Nombre", Nombre, 3));
		pw.write(startEndLabel("Apellidos", Apellidos, 3));
		pw.write(startEndLabel("Sexo", Sexo, 3));
		pw.write(startEndLabel("Fecha_nacimiento", Fecha_nacimiento, 3));
		pw.write(startEndLabel("Domicilio", Domicilio, 3));
		pw.write(startEndLabel("Localidad", Localidad, 3));
		pw.write(startEndLabel("Correo_electronico", Correo_electronico, 3));
		pw.write(startEndLabel("Telefono", Telefono, 3));
		pw.write(startEndLabel("Embarazada", Embarazada ? "1" : "0", 3));
		
	}
	
	public void xmlMedico(ResultSet result) throws IOException, SQLException {
        
		HashMap<String,String> idHash = new HashMap<>();
       
        String Licencia = null;
        String Nombre = null;
		String Apellidos = null;
		String Sexo = null;
		String Especialidad = null;
		
		while(result.next()) {
		Licencia = result.getString("Licencia");
		Nombre = result.getString("Nombre");
		Apellidos = result.getString("Apellidos");
		Sexo = result.getString("Sexo");
		Especialidad = result.getString("Especialidad");
        
		}
        idHash.put("Licencia", Licencia);
		pw.write(startLabel("Medico", idHash, 2));
		pw.write(startEndLabel("Nombre", Nombre, 3));
		pw.write(startEndLabel("Apellidos", Apellidos, 3));
		pw.write(startEndLabel("Sexo", Sexo, 3));
		pw.write(startEndLabel("Especialidad", Especialidad, 3));
		
	}
	
	public void xmlAllICD(ResultSet result) throws IOException, SQLException {
        
		HashMap<String,String> idHash = new HashMap<>();
       
        String Codigo = null;
        String Nombre = null;
		
		while(result.next()) {
			Codigo = result.getString("Codigo");
			Nombre = result.getString("Nombre");
			
	        idHash.put("Codigo", Codigo);
			
	        pw.write(startLabel("ICD_10", idHash, 2));
			pw.write(startEndLabel("Nombre", Nombre, 3));
			pw.write(endLabel("ICD_10", 2));
		}
		

		
	}
	
	public void xmlConsulta(ResultSet result) throws IOException, SQLException {
               
		HashMap<String,String> idHash = new HashMap<>();
	       
        String idConsulta = null;
        String Localizacion = null;
        String Centro_sanitario = null;
		
		while(result.next()) {
			idConsulta = result.getString("idConsulta");
			Localizacion = result.getString("Localizacion");
			Centro_sanitario = result.getString("Centro_sanitario");
			
	        idHash.put("idConsulta", idConsulta);
			
	        pw.write(startLabel("Consulta", idHash, 2));
			pw.write(startEndLabel("Localizacion", Localizacion, 3));
			pw.write(startEndLabel("Centro_sanitario", Localizacion, 3));
			pw.write(endLabel("Consulta", 2));
		}
		

		
	}
	
	public void xmlAtiende(ResultSet result) throws IOException, SQLException {
        
        String idConsulta = null;
		
        pw.write(startLabel("Consultas", 3) + "\n");
        
		while(result.next()) {
			idConsulta = result.getString("idConsulta");
						
			pw.write(startEndLabel("idConsulta", idConsulta, 4));
		}
		
        pw.write(endLabel("Consultas", 3));

		
	}
	
	public void xmlHistorial(ResultSet result) throws IOException, SQLException {
        
		HashMap<String,String> idHash = new HashMap<>();
       
        String idHistorial = null;
        String Fecha_primera_consulta = null;
        String Vacunas = null;

        
        if (result!=null) {
        	
        	while(result.next()) {
        	
        	idHistorial = result.getString("idHistorial");

        	Fecha_primera_consulta = result.getString("Fecha_primera_consulta");
        	Vacunas = result.getString("Vacunas");


            
        	}
        }else {

        }
        idHistorial = idHistorial==null ? "" : idHistorial;
        idHash.put("idHistorial", idHistorial);

        pw.write(startLabel("Historial", idHash, 3));
		pw.write(startEndLabel("Fecha_primera_consulta", Fecha_primera_consulta, 4));
		pw.write(startEndLabel("Vacunas", Vacunas, 4));

		
	}
	
	public void xmlFRP(ResultSet result) throws IOException, SQLException {
       
        String Antecedentes_familiares = null;
        String Factores_psicosociales = null;
        String Antecedentes_obstetricos = null;
		String Antecedentes_personales = null;
		String Patologia_materna = null;
		String Riesgos_especificos = null;
		String Exposicion_a_teratogenos = null;

		if(result!=null) {
        while (result.next()) {
        	Antecedentes_familiares = result.getString("Antecedentes_familiares");
        	Factores_psicosociales = result.getString("Factores_psicosociales");
        	Antecedentes_obstetricos = result.getString("Antecedentes_obstetricos");
        	Antecedentes_personales = result.getString("Antecedentes_personales");
        	Patologia_materna = result.getString("Patologia_materna");
        	Riesgos_especificos = result.getString("Riesgos_especificos");
        	Exposicion_a_teratogenos = result.getString("Exposicion_a_teratogenos");
        }
		}

		pw.write(startLabel("Factor_de_riesgo_prenatal", 4) + "\n");
		pw.write(startEndLabel("Antecedentes_familiares", Antecedentes_familiares, 5));
		pw.write(startEndLabel("Factores_psicosociales", Factores_psicosociales, 5));
		pw.write(startEndLabel("Antecedentes_obstetricos", Antecedentes_obstetricos, 5));
		pw.write(startEndLabel("Antecedentes_personales", Antecedentes_personales, 5));
		pw.write(startEndLabel("Patologia_materna", Patologia_materna, 5));
		pw.write(startEndLabel("Riesgos_especificos", Riesgos_especificos, 5));
		pw.write(startEndLabel("Exposicion_a_teratogenos", Exposicion_a_teratogenos, 5));
		pw.write(endLabel("Factor_de_riesgo_prenatal", 4));

	}
	
	public void xmlInforme(ResultSet result) throws IOException, SQLException {

        HashMap<String,String> idHash = new HashMap<>();

        String idInforme = null;
        String Licencia_medico = null;
        String Estado_paciente= null;
        String Diagnostico = null;
        String idConsulta = null;
		String Fecha_consulta = null;
		String Es_urgente = null;
		String Sintomas = null;
		
		
		if(result!=null) {
			
        	while(result.next()) {

        	idInforme = result.getString("idInforme");
        	Licencia_medico = result.getString("Licencia_medico");
        	Estado_paciente = result.getString("Estado_paciente");
        	Diagnostico = result.getString("Diagnostico");
        	idConsulta = result.getString("idConsulta");
        	Fecha_consulta = result.getString("Fecha_consulta");
        	Es_urgente = result.getString("Es_urgente");
        	Sintomas = result.getString("Sintomas");
        	

            idHash.put("Informe", idInforme);
    		pw.write(startLabel("Informe", idHash, 4));
    		pw.write(startEndLabel("Licencia_medico", Licencia_medico, 5));
    		pw.write(startEndLabel("Estado_paciente", Estado_paciente, 5));
    		pw.write(startEndLabel("Diagnostico", Diagnostico, 5));
    		pw.write(startEndLabel("idConsulta", idConsulta, 5));
    		pw.write(startEndLabel("Fecha_consulta", Fecha_consulta, 5));
    		pw.write(startEndLabel("Es_urgente", Es_urgente, 5));
    		pw.write(startEndLabel("Sintomas", Sintomas, 5));
    		
        	}}else {
        		
        		idInforme = idInforme==null ? "" : idInforme;
                idHash.put("Informe", idInforme);

        		pw.write(startLabel("Informe", idHash, 4));
        		pw.write(startEndLabel("Licencia_medico", Licencia_medico, 5));
        		pw.write(startEndLabel("Estado_paciente", Estado_paciente, 5));
	    		pw.write(startEndLabel("Diagnostico", Diagnostico, 5));
	    		pw.write(startEndLabel("idConsulta", idConsulta, 5));
	    		pw.write(startEndLabel("Fecha_consulta", Fecha_consulta, 5));
	    		pw.write(startEndLabel("Es_urgente", Es_urgente, 5));
	    		pw.write(startEndLabel("Sintomas", Sintomas, 5));

			}
	}
	
	public void xmlICD(ResultSet result) throws IOException, SQLException {
        
		String code =  null;
        
		pw.write(startLabel("ICD_10", 5) + "\n");
		
		if(result!=null) {
			
        	while(result.next()) {        		
        		code = result.getString("Codigo");
        		pw.write(startEndLabel("Codigo_ICD_10", code, 6));
        	}	
		}else {
    		pw.write(startEndLabel("Codigo_ICD_10", code, 6));
		}
		pw.write(endLabel("ICD_10", 5));
		
	}
	
	public void xmlPrueba(ResultSet result) throws IOException, SQLException {

        HashMap<String,String> idHash = new HashMap<>();

        String idPrueba = null;
        String idPrueba_externo = null;
        String Nombre= null;
        String Observaciones = null;
        String Tipo = null;
        
        boolean cnt = false;
		
        
		if(result!=null) {
			
        	while(result.next()) {
        		idPrueba = result.getString("idPrueba");
        		idPrueba_externo = result.getString("idPrueba_externo");
        		Nombre = result.getString("Nombre");
        		Observaciones = result.getString("Observaciones");
        		Tipo = result.getString("Tipo");

            idHash.put("idPrueba", idPrueba);
    		pw.write(startLabel("Prueba", idHash, 5)); 
    		pw.write(startEndLabel("idPrueba_externo", idPrueba_externo, 6)); 
    		pw.write(startEndLabel("Nombre", Nombre, 6));
    		pw.write(startEndLabel("Observaciones", Observaciones, 6));
    		pw.write(startEndLabel("Tipo", Tipo, 6));
    		pw.write(endLabel("Prueba", 5));


    		cnt = true;
    		
        	}
        }
		
		
		if (!cnt){

			idPrueba = idPrueba==null ? "" : idPrueba;
            idHash.put("Prueba", idPrueba);

    		pw.write(startLabel("idPrueba", idHash, 5)); 
    		pw.write(startEndLabel("idPrueba_externo", idPrueba_externo, 6)); 
    		pw.write(startEndLabel("Nombre", Nombre, 6));
    		pw.write(startEndLabel("Observaciones", Observaciones, 6));
    		pw.write(startEndLabel("Tipo", Tipo, 6));
    		pw.write(endLabel("Prueba", 5));
        }
        	


		
	}
	
	String startLabel(String id, int ident) {
		return identation(ident) + "<" + id + ">";
	}
	
	String startLabel(String id) {
		return "<" + id + ">";
	}

	String startLabel(String id, HashMap<String,String> Attributes, int ident) {
		
		String result = null;
		
		if(!Attributes.keySet().isEmpty()) {
		
		StringBuilder tag = new StringBuilder( identation(ident) + "<" + id);
		for (String key : Attributes.keySet()){
			tag.append(' ').append(key).append("=\"").append(Attributes.get(key)).append('\"');
		}
		tag.append(">\n");
		result = tag.toString();
		
		}else {
			result = startLabel(id);
		}
		
		
		return result;
	}

	String endLabel(String id, int ident) {
		
		return  identation(ident) + "</" + id + ">\n";
	}
	
	String endLabel(String id) {
		
		return  "</" + id + ">\n";
	}
	
	String startEndLabel(String id, String info, int ident) {
		if(info==null)
			info="";
		return identation(ident) + startLabel(id) + info + endLabel(id);
	}
	
	void escribir(List<String> list) throws IOException {
		for(String l : list)
			pw.write(l+"\n");
		
	}
	
    public List<String> getIdInforme(ResultSet result) throws SQLException, IOException {

        List<String> all_id = new ArrayList<>();
        
        while(result.next()) {
            	all_id.add(result.getString("idInforme"));
        }
        
        
        
        return(all_id);
    }
    
    public List<String> getIdPaciente(ResultSet result) throws SQLException, IOException {

        List<String> all_id = new ArrayList<>();
        
        if(result==null)
        	System.out.println("error");
        else {
        while(result.next()) {
            all_id.add(result.getString("idPaciente"));
        }  
        } 
        return(all_id);
    }
    
    public List<String> getIdPaciente(String s) throws SQLException, IOException {

		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			//execute query
			try (ResultSet rs = stmt.executeQuery(s)){
				return(getIdPaciente(rs));
			}
			catch (SQLException e) {
				e.printStackTrace();
			} 
		}
		return null;
    }
    
    
    public List<String> getIdMedico(ResultSet result) throws SQLException, IOException {

        List<String> all_id = new ArrayList<>();
        
        if(result==null)
        	System.out.println("error");
        else {
        while(result.next()) {
            	all_id.add(result.getString("Licencia"));
        }  
        } 
        return(all_id);
    }
    
    public List<String> getIdMedico(String s) throws SQLException, IOException {

		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			//execute query
			try (ResultSet rs = stmt.executeQuery(s)){
				return(getIdMedico(rs));
			}
			catch (SQLException e) {
				e.printStackTrace();
			} 
		}
		return null;
    }
    
    
    public void closeFW() throws IOException {
    	pw.close();
    }
	
    public String identation(int num) {
    	String result = "\t";
    	for(int i=1; i<num; i++)
    		result = result + "\t";
    	return(result);
    }
    
}
