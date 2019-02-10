import mysqlConnection as conn

class Prueba:
    def __init__(self):
        self.idPrueba = None
        self.Observaciones = None
        self.idPrueba_Externo = None
        self.Tipo = None
        self.idInforme = None
        self.Nombre = None

    def new_prueba(self, idPrueba, Observaciones, idPrueba_Externo, Tipo, idInforme = None, Nombre = None):
        self.idPrueba = idPrueba is None and len(lista_pruebas())+1 or idPrueba
        self.Observaciones = Observaciones
        self.idPrueba_Externo =  idPrueba is None and  "P-" + idInforme + "-" + str(len(lista_pruebas())+1) or idPrueba
        self.Tipo = Tipo
        self.Nombre = Nombre
        self.idInforme = idInforme

    def insert_prueba(self):
        query = "INSERT INTO Prueba (idPrueba, Observaciones, idPrueba_externo, Tipo, idInforme, Nombre)" \
                "  VALUES('" + str(self.idPrueba) + "', '" + self.Observaciones + "', '" + str(
            self.idPrueba_Externo) + "', '" + self.Tipo + "', '" + self.idInforme + "', '" + self.Nombre + "' );"
        print(query)
        connection = conn.get_connection()
        conn.update_query(query, connection)
        conn.close_connection(connection)


def lista_pruebas():
    query = "SELECT * FROM Prueba;"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    pruebas = list()
    conn.close_connection(connection)
    for (idPrueba, Observaciones, idPrueba_Externo, Tipo, idInforme, Nombre) in result:
        prueba = Prueba()
        prueba.new_prueba(idPrueba, Observaciones, idPrueba_Externo, Tipo, idInforme, Nombre)
        pruebas.append(prueba)
    return pruebas

def get_prueba(idPrueba):
    query = "SELECT * FROM Prueba WHERE idPrueba ='" + str(idPrueba) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    for(idPrueba, Observaciones, idPrueba_Externo, Tipo, idInforme, Nombre) in result:
        prueba = Prueba()
        prueba.new_prueba(idPrueba, Observaciones, idPrueba_Externo, Tipo, idInforme, Nombre)
    return prueba

def get_prueba_from_informe(idInforme):
    query = "SELECT * FROM Prueba WHERE idInforme ='" + str(idInforme) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    pruebas = list()
    for(idPrueba, Observaciones, idPrueba_Externo, Tipo, idInforme, Nombre) in result:
        prueba = Prueba()
        prueba.new_prueba(idPrueba, Observaciones, idPrueba_Externo, Tipo, idInforme, Nombre)
        pruebas.append(prueba)
    return pruebas