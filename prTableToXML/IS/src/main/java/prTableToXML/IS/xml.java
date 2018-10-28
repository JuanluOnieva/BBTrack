package prTableToXML.IS;


import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

import javax.xml.stream.events.Attribute;

public abstract class xml {

	String idprev;
	FileWriter pw;
	String id = "";
	Boolean idInit;

	public xml () throws SQLException, IOException {
		idprev = "nada";
    	File fichero = new File("prueba.txt");
       	pw = new FileWriter(fichero, true);
       	idInit = false;
	}
	
public abstract void addValues(ResultSet result) throws SQLException, IOException;
	
	String startLabel(String id) {
		return "<" + id + ">\n";
	}

	String startLabel(String id, HashMap<String,String> Attributes) {
		//Creates a label with attributes
		StringBuilder tag = new StringBuilder("<" + id);
		for (String key : Attributes.keySet()){
			tag.append(' ').append(key).append("=\"").append(Attributes.get(key)).append('\"');
		}
		tag.append(">\n");
		return tag.toString();
	}

	String endLabel(String id) {
		return "</" + id + ">\n";
	}
	
	void escribir(List<String> list) throws IOException {
		for(String l : list)
			pw.write(l+"\n");
		
	}
	


}
