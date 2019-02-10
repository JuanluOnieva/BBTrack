import mysqlConnection as conn
import Prueba

class Informe:
    def __init__(self):
        self.idInforme = None
        self.Estado_paciente = None
        self.Diagnostico = None
        self.idHistorial = None
        self.idConsulta = None
        self.Fecha_consulta = None
        self.Licencia_medico = None
        self.Pruebas = None
        self.ICD10s = None

    def new_informe(self, idInforme,  Estado_paciente, Diagnostico, idHistorial, Fecha_consulta, idConsulta, Licencia_medico, Pruebas = None, ICD10s = None):
        self.idInforme = idInforme is None and idHistorial + "-" + idConsulta.replace("-", "") + "-" \
                         + str(Fecha_consulta).replace("-", "") or idInforme
        self.Estado_paciente = Estado_paciente
        self.Diagnostico = Diagnostico
        self.idHistorial = idHistorial
        self.idConsulta = idConsulta
        self.Fecha_consulta = Fecha_consulta
        self.Licencia_medico = Licencia_medico
        if Pruebas is None:
            self.Pruebas = get_prueba(self.idInforme)
        else:
            self.Pruebas = Pruebas
        if ICD10s is None:
            self.ICD10s = get_ICD10(self.idInforme)
        else:
            self.ICD10s = ICD10s

    def insert_informe(self):
        query = "INSERT INTO Informe (idInforme, Estado_paciente, Diagnostico, idHistorial, Fecha_consulta, idConsulta, Licencia_medico)" \
                "  VALUES('" + str(self.idInforme) + "', '" + self.Estado_paciente + "', '" + str(
                self.Diagnostico) + "', '" + self.idHistorial + "', '" + self.Fecha_consulta + "', '" + self.idConsulta \
            + "', '" + self.Licencia_medico + "' );"
        print(query)
        connection = conn.get_connection()
        conn.update_query(query, connection)
        conn.close_connection(connection)

    def delete_informe(self):
        query = list()
        query.append("DELETE FROM Informe WHERE idInforme = '" + str(self.idInforme)  + "';")
        print("DELETE FROM Informe WHERE idInforme = '" + str(self.idInforme)  + "';")
        query.append("DELETE FROM Prueba WHERE idInforme = '" + str(self.idInforme)  + "';")
        query.append("DELETE FROM INFORME_ICD_10 WHERE idInforme = '" + str(self.idInforme)  + "';")
        connection = conn.get_connection()
        conn.update_query(query, connection)
        conn.close_connection(connection)
        self.idInforme = None
        self.Estado_paciente = None
        self.Diagnostico = None
        self.idHistorial = None
        self.idConsulta = None
        self.Fecha_consulta = None
        self.Licencia_medico = None
        self.Pruebas = None
        self.ICD10s = None

    def insert_icd10(self, codes):
        query = list()
        print("Aquiiiii" + str(len(codes)))
        for code in codes:
            if code not in self.ICD10s:
                query.append("INSERT INTO INFORME_ICD_10 (IdInforme, Codigo) VALUES ('" + self.idInforme + "', '" \
              + code + "');")
        print(query)
        connection = conn.get_connection()
        conn.update_query(query, connection)
        conn.close_connection(connection)

def lista_informes():
    query = "SELECT * FROM Informe;"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    informes = list()
    conn.close_connection(connection)
    for (idInforme, Estado_paciente, Diagnostico, idHistorial, Fecha_consulta, idConsulta, Licencia_medico) in result:
        informe = Informe()
        informe.new_informe(idInforme,  Estado_paciente, Diagnostico, idHistorial, Fecha_consulta, idConsulta, Licencia_medico, None, None)
        informes.append(informe)
    return informes

def get_prueba(idInforme):
    query = "SELECT idPrueba FROM Prueba WHERE idInforme ='" + str(idInforme) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    pruebas = list()
    if result:
        for(idPrueba) in result:
            pruebas.append(str(idPrueba[0]))
    return pruebas

def get_ICD10(idInforme):
    query = "SELECT Codigo FROM INFORME_ICD_10 WHERE idInforme ='" + str(idInforme) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    ICD10s = list()
    if result:
        for(Codigo) in result:
            ICD10s.append(str(Codigo[0]))
    return ICD10s

def get_informe(idInforme):
    query = "SELECT * FROM Informe WHERE idInforme = '" + str(idInforme) + "';"
    print(query)
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    for(idInforme, Estado_paciente, Diagnostico, idHistorial, idConsulta,
                    Fecha_consulta, Licencia_medico) in result:
        informe = Informe()
        informe.new_informe(idInforme, Estado_paciente, Diagnostico, idHistorial, idConsulta,
                    Fecha_consulta, Licencia_medico, None, None)
    return informe

def get_consultas():
    informes = lista_informes()
    consultas = list()
    for informe in informes:
        if informe.idConsulta not in consultas:
            consultas.append(informe.idConsulta)
    return consultas

def get_informe_historial(idHistorial):
    query = "SELECT * FROM Informe WHERE idHistorial = '" + str(idHistorial) + "';"
    print(query)
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    informes = list()
    conn.close_connection(connection)
    for (idInforme, Estado_paciente, Diagnostico, idHistorial, Fecha_consulta, idConsulta, Licencia_medico) in result:
        informe = Informe()
        informe.new_informe(idInforme,  Estado_paciente, Diagnostico, idHistorial, Fecha_consulta, idConsulta, Licencia_medico, None, None)
        informes.append(informe)
    return informes