package prTableToXML.IS;

import java.io.IOException;
import java.sql.SQLException;
import java.util.List;

public interface DBDriverInterface {
	void addPaciente(String query) throws SQLException, IOException;
	String getTime();
	String getRows();
//	void connect() throws SQLException;

}
