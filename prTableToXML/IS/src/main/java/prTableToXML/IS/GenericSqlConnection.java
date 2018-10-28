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

public class GenericSqlConnection implements DBDriverInterface {
	
	protected Connection connection;
	protected long time = 0;
	protected int rowsNumber = 0;
	protected String url;
	protected Properties props = new Properties();
	protected boolean moreDB = true;
	FileWriter pw;
	
	public void addPaciente(String s) throws IOException{
		//// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			////execute query
			time = 0;
			rowsNumber = 0;
			long timeBefore = System.currentTimeMillis();
			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
				
				List<String> all_id = getIdPaciente(rs);
				for(String id : all_id) {
					ResultSet rsPaciente = stmt.executeQuery("SELECT p.idPaciente, p.NUSS, p.Nombre , p.Apellidos, p.Sexo, p.Fecha_Nacimiento, p.Domicilio, p.Localidad, p.Correo_electronico, p.Telefono, p.Embarazada FROM PACIENTE p WHERE idPaciente="+id);
					xmlPaciente(rsPaciente);

					ResultSet rsHistorial = stmt.executeQuery("SELECT h.idHistorial, h.Fecha_primera_consulta, h.Vacunas FROM HISTORIAL h WHERE h.idPaciente="+id);
					xmlHistorial(rsHistorial);
					
					try(ResultSet rsFRP = stmt.executeQuery("SELECT f.Antecedentes_familiares, f.Factores_psicosociales, f.Antecedentes_obstetricos, f.Antecedentes_personales, f.Patologia_materna, f.Riesgos_especificos, f.Exposicion_a_teratogenos " + 
							" FROM HISTORIAL h FACTOR_DE_RIESGO_PRENATAL f WHERE h.idPaciente="+id +" and h.idHistorial=f.idHistorial"))
					{xmlFRP(rsFRP);}
					catch(SQLException e) {
						xmlFRP(null);
					}
					
					pw.write(endLabel("FACTOR_DE_RIESGO_PRENATAL"));
					System.out.println(endLabel("FACTOR_DE_RIESGO_PRENATAL"));
					
					

										
					ResultSet rsInforme = stmt.executeQuery("SELECT idInforme FROM INFORME WHERE idHistorial=\"H-"+id + "\";");
					
					List<String> all_id_Informe = new ArrayList<String>();
					all_id_Informe.addAll(getIdInforme(rsInforme));
					
					if(all_id_Informe.isEmpty()) {
						
						xmlInforme(null);
						xmlPrueba(null);
						
						pw.write(endLabel("Informe"));
						System.out.println(endLabel("Informe"));
					}
					
					for(String idInforme : all_id_Informe) {
												
						rsInforme = stmt.executeQuery("SELECT i.idInforme, i.Estado_paciente, i.Diagnostico, i.idConsulta, i.Fecha_consulta, a.Es_urgente, a.Sintomas" + 
								" FROM asiste_a a, informe i where a.idConsulta=i.idConsulta and a.Fecha_consulta=i.Fecha_consulta and i.idInforme=\"" + idInforme + "\" ;");
						xmlInforme(rsInforme);						
						
						ResultSet rsPrueba = stmt.executeQuery("SELECT p.idPrueba, p.Nombre, p.Observaciones, p.Tipo FROM PRUEBA p WHERE p.idInforme=\""+idInforme+"\";");
						
						xmlPrueba(rsPrueba);
						
						 
						pw.write(endLabel("Informe"));
						System.out.println(endLabel("Informe"));
					}
					
					pw.write(endLabel("Historial"));
					System.out.println(endLabel("Historial"));
					
					pw.write(endLabel("Paciente"));
					System.out.println(endLabel("Paciente"));


				}
				System.out.println(rs.toString());
				
			}
		} catch (SQLException e) {
			e.getMessage();
		}
	}

	public GenericSqlConnection(String file) throws SQLException, IOException {
		File fichero = new File(file);
       	pw = new FileWriter(fichero, true);
		String connectionString = "jdbc:mysql://localhost/bbTrack?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC"; 
		
		connection = DriverManager.getConnection(connectionString, "root", "bbtrack123");

	}
		
	public String getTime() {
		return ""+time;
	}

	public String getRows() {
		return ""+rowsNumber;
	}
	
	public String toString() {
		return connection.toString();
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
        }
        
        idHash.put("idPaciente", idPaciente);
        idHash.put("NUSS", NUSS);
		pw.write(startLabel("Paciente", idHash));
		pw.write(startEndLabel("Nombre", Nombre));
		pw.write(startEndLabel("Apellidos", Apellidos));
		pw.write(startEndLabel("Sexo", Sexo));
		pw.write(startEndLabel("Fecha_nacimiento", Fecha_nacimiento));
		pw.write(startEndLabel("Domicilio", Domicilio));
		pw.write(startEndLabel("Localidad", Localidad));
		pw.write(startEndLabel("Correo_electronico", Correo_electronico));
		pw.write(startEndLabel("Telefono", Telefono));
		
		System.out.println(startLabel("Paciente", idHash));
		System.out.println(startEndLabel("Nombre", Nombre));
		System.out.println(startEndLabel("Apellidos", Apellidos));
		System.out.println(startEndLabel("Sexo", Sexo));
		System.out.println(startEndLabel("Fecha_nacimiento", Fecha_nacimiento));
		System.out.println(startEndLabel("Domicilio", Domicilio));
		System.out.println(startEndLabel("Localidad", Localidad));
		System.out.println(startEndLabel("Correo_electronico", Correo_electronico));
		System.out.println(startEndLabel("Telefono", Telefono));
		
	}
	
	public void xmlHistorial(ResultSet result) throws IOException, SQLException {
        HashMap<String,String> idHash = new HashMap<>();
       
        String idHistorial = null;
        String Fecha_primera_consulta = null;
        String Vacunas = null;

        
        if (result.getRow()==1) {
        	idHistorial = result.getString("idHistorial");
        	Fecha_primera_consulta = result.getString("Fecha_primera_consulta");
        	Vacunas = result.getString("Vacunas");
        	
            idHash.put("idHistorial", idHistorial);

        }
        
		pw.write(startLabel("Historial", idHash));
		pw.write(startEndLabel("Fecha_primera_consulta", Fecha_primera_consulta));
		pw.write(startEndLabel("Vacunas", Vacunas));
		
		System.out.println(startLabel("Historial", idHash));
		System.out.println(startEndLabel("Fecha_primera_consulta", Fecha_primera_consulta));
		System.out.println(startEndLabel("Vacunas", Vacunas));
		
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

		pw.write(startLabel("FACTOR_DE_RIESGO_PRENATAL"));
		pw.write(startEndLabel("Antecedentes_familiares", Antecedentes_familiares));
		pw.write(startEndLabel("Factores_psicosociales", Factores_psicosociales));
		pw.write(startEndLabel("Antecedentes_obstetricos", Antecedentes_obstetricos));
		pw.write(startEndLabel("Antecedentes_personales", Antecedentes_personales));
		pw.write(startEndLabel("Patologia_materna", Patologia_materna));
		pw.write(startEndLabel("Riesgos_especificos", Riesgos_especificos));
		pw.write(startEndLabel("Exposicion_a_teratogenos", Exposicion_a_teratogenos));
		
		System.out.println(startLabel("FACTOR_DE_RIESGO_PRENATAL"));
		System.out.println(startEndLabel("Antecedentes_familiares", Antecedentes_familiares));
		System.out.println(startEndLabel("Factores_psicosociales", Factores_psicosociales));
		System.out.println(startEndLabel("Antecedentes_obstetricos", Antecedentes_obstetricos));
		System.out.println(startEndLabel("Antecedentes_personales", Antecedentes_personales));
		System.out.println(startEndLabel("Patologia_materna", Patologia_materna));
		System.out.println(startEndLabel("Riesgos_especificos", Riesgos_especificos));
		System.out.println(startEndLabel("Exposicion_a_teratogenos", Exposicion_a_teratogenos));
		
	}
	
	public void xmlInforme(ResultSet result) throws IOException, SQLException {

        HashMap<String,String> idHash = new HashMap<>();

        String idInforme = null;
        String Estado_paciente= null;
        String Diagnostico = null;
        String idConsulta = null;
		String Fecha_consulta = null;
		String Es_urgente = null;
		String Sintomas = null;
		
		
		if(result!=null) {
        	while(result.next()) {
        	idInforme = result.getString("idInforme");
        	Estado_paciente = result.getString("Estado_paciente");
        	Diagnostico = result.getString("Diagnostico");
        	idConsulta = result.getString("idConsulta");
        	Fecha_consulta = result.getString("Fecha_consulta");
        	Es_urgente = result.getString("Es_urgente");
        	Sintomas = result.getString("Sintomas");

            idHash.put("Informe", idInforme);
    		pw.write(startLabel("Informe", idHash));
    		pw.write(startEndLabel("Estado_paciente", Estado_paciente));
    		pw.write(startEndLabel("Diagnostico", Diagnostico));
    		pw.write(startEndLabel("idConsulta", idConsulta));
    		pw.write(startEndLabel("Fecha_consulta", Fecha_consulta));
    		pw.write(startEndLabel("Es_urgente", Es_urgente));
    		pw.write(startEndLabel("Sintomas", Sintomas));
    		
    		System.out.println(startLabel("Informe", idHash));
    		System.out.println(startEndLabel("Estado_paciente", Estado_paciente));
    		System.out.println(startEndLabel("Diagnostico", Diagnostico));
    		System.out.println(startEndLabel("idConsulta", idConsulta));
    		System.out.println(startEndLabel("Fecha_consulta", Fecha_consulta));
    		System.out.println(startEndLabel("Es_urgente", Es_urgente));
    		System.out.println(startEndLabel("Sintomas", Sintomas));
    		
        	}}else {
        		pw.write(startLabel("Informe", idHash));
        		pw.write(startEndLabel("Estado_paciente", Estado_paciente));
	    		pw.write(startEndLabel("Diagnostico", Diagnostico));
	    		pw.write(startEndLabel("idConsulta", idConsulta));
	    		pw.write(startEndLabel("Fecha_consulta", Fecha_consulta));
	    		pw.write(startEndLabel("Es_urgente", Es_urgente));
	    		pw.write(startEndLabel("Sintomas", Sintomas));
	    		
	    		System.out.println(startLabel("Informe", idHash));
	    		System.out.println(startEndLabel("Estado_paciente", Estado_paciente));
	    		System.out.println(startEndLabel("Diagnostico", Diagnostico));
	    		System.out.println(startEndLabel("idConsulta", idConsulta));
	    		System.out.println(startEndLabel("Fecha_consulta", Fecha_consulta));
	    		System.out.println(startEndLabel("Es_urgente", Es_urgente));
	    		System.out.println(startEndLabel("Sintomas", Sintomas));

			}



		
	}
	
	public void xmlPrueba(ResultSet result) throws IOException, SQLException {

        HashMap<String,String> idHash = new HashMap<>();

        String idPrueba = null;
        String Nombre= null;
        String Observaciones = null;
        String Tipo = null;
        
        boolean cnt = false;
		
		if(result!=null) {
			
        	while(result.next()) {
        		idPrueba = result.getString("idPrueba");
        		Nombre = result.getString("Nombre");
        		Observaciones = result.getString("Observaciones");
        		Tipo = result.getString("Tipo");

            idHash.put("Prueba", idPrueba);
    		pw.write(startLabel("Prueba", idHash)); 
    		pw.write(startEndLabel("Nombre", Nombre));
    		pw.write(startEndLabel("Observaciones", Observaciones));
    		pw.write(startEndLabel("Tipo", Tipo));
    		pw.write(endLabel("Prueba"));

    		System.out.println(startLabel("Prueba", idHash));
    		System.out.println(startEndLabel("Nombre", Nombre));
    		System.out.println(startEndLabel("Observaciones", Observaciones));
    		System.out.println(startEndLabel("Tipo", Tipo));
    		System.out.println(endLabel("Prueba"));
        	
    		cnt = true;
    		
        	}
        }
		
		
		if (!cnt){
    		pw.write(startLabel("Prueba", idHash)); 
    		pw.write(startEndLabel("Nombre", Nombre));
    		pw.write(startEndLabel("Observaciones", Observaciones));
    		pw.write(startEndLabel("Tipo", Tipo));
    		pw.write(endLabel("Prueba"));

    		System.out.println(startLabel("Prueba", idHash));
    		System.out.println(startEndLabel("Nombre", Nombre));
    		System.out.println(startEndLabel("Observaciones", Observaciones));
    		System.out.println(startEndLabel("Tipo", Tipo));
    		System.out.println(endLabel("Prueba"));
        }
        	


		
	}
	
	String startLabel(String id) {
		return "<" + id + ">";
	}

	String startLabel(String id, HashMap<String,String> Attributes) {
		
		String result = null;
		
		if(!Attributes.keySet().isEmpty()) {
		
		StringBuilder tag = new StringBuilder("<" + id);
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

	String endLabel(String id) {
		return "</" + id + ">\n";
	}
	
	String startEndLabel(String id, String info) {
		if(info==null)
			info="";
		return startLabel(id) + info + endLabel(id);
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
        
        while(result.next()) {
            	all_id.add(result.getString("idPaciente"));
        }
        
        
        
        return(all_id);
    }
    
    public void closeFW() throws IOException {
    	pw.close();
    }
	
}
