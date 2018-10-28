package prTableToXML.IS;

import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.mysql.cj.xdevapi.Statement;

public class addPaciente extends xml {
    
	HashMap<String,String> table_id;
	List<String> all_id;
    
    public addPaciente() throws SQLException, IOException {
        all_id = new ArrayList<String>();
     
    }

    @Override
    public void addValues(ResultSet result) throws SQLException, IOException {
        String type;
        String value;
        //int num = result.getMetaData().getColumnCount();
        
        while(result.next()) {
            	all_id.add(result.getString("idPaciente"));
        }
//        while (result.next()) {
//            if(id.equals(result.getString("compound_id"))) {
//                type = result.getString("type");
//                value = result.getString("chemical_data");
//                pw.write(startLabel(type));
//                System.out.print(startLabel(type));
//                pw.write(value);
//                System.out.print(value);
//                pw.write(endLabel(type));
//                System.out.print(endLabel(type));
//            }else{
//                if(idInit){
//                    pw.write(endLabel("id"));
//                }else{
//                    idInit = true;
//                }
//                id = result.getString("compound_id");
//                idHash.put("Value",id);
//                pw.write(startLabel("id", idHash));
//                System.out.print(startLabel("id", idHash));
//            }
//        }
    }

    public void xmlEnd() throws IOException {
        pw.write(endLabel("table"));
        System.out.print(endLabel("table"));
        pw.close();
    }
    
	public List<String> getId(){
		return all_id;
	}
}