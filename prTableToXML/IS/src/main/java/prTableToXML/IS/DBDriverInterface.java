package prTableToXML.IS;

import java.io.IOException;
import java.sql.SQLException;
import java.util.List;

public interface DBDriverInterface {
	void executeQuery(String query) throws SQLException, IOException;
	String getTime();
	String getRows();
	boolean hasMoreDB();
	List<String> availableDbs();
	void connect(String db) throws SQLException;
	int dbAdapt(String dbName);

}
