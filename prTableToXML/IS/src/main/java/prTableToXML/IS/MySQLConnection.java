package prTableToXML.IS;

import java.sql.SQLException;

public class MySQLConnection extends GenericSqlConnection{
	public MySQLConnection() {
		url = "jdbc:mysql://localhost:3306";
		props.setProperty("user","root");
		props.setProperty("password","bbtrack");
		databases.add("bbtrack");
	}

	@Override
	public int dbAdapt(String dbName) {
		switch(dbName){
		case "bbtrack": return 0;
		default: return -1;
		}
	}
}
