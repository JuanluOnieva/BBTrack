package prTableToXML.IS;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Properties;

/**
 * 
 * @author marcomunozperez
 * TODO Add query exceptions
 */

public abstract class GenericSqlConnection implements DBDriverInterface {
	
	protected Connection connection;
	protected long time = 0;
	protected int rowsNumber = 0;
	protected String url;
	protected Properties props = new Properties();
	public ArrayList<String> databases = new ArrayList<String>();
	protected boolean moreDB = true;
	
	public void executeQuery(String s) throws IOException{
		// create a Statement
		try (Statement stmt = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY)){	
			//execute query
			time = 0;
			rowsNumber = 0;
			long timeBefore = System.currentTimeMillis();
			try (ResultSet rs = stmt.executeQuery(s)){
			    //Generate XML from query result
				xml _xml = new addPaciente();
				_xml.addValues(rs);
				((addPaciente) _xml).xmlEnd();
				time = System.currentTimeMillis() - timeBefore;
				
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	public void connect(String db) throws SQLException {
		connection = DriverManager.getConnection(url+"/" + db, props);
	}
	
	public abstract int dbAdapt(String dbName);
	
	public String getTime() {
		return ""+time;
	}

	public String getRows() {
		return ""+rowsNumber;
	}

	public ArrayList<String> availableDbs() {
		return databases;
	}
	
	public boolean hasMoreDB(){
		return this.moreDB;
	}
}
