import mysqlConnection as conn

class ICD10:
    def __init__(self):
        self.Codigo = None
        self.Nombre = None
        self.informes = None

    def new_ICD10(self, Codigo, Nombre, informes = None):
        self.Codigo = Codigo
        self.Nombre = Nombre
        if informes is None:
            self.informes = get_informes(self.Codigo)
        else:
            self.informes = informes


def lista_ICD10():
    query = "SELECT * FROM ICD_10;"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    codigos = list()
    conn.close_connection(connection)
    for (Codigo, Nombre) in result:
        icd10 = ICD10()
        icd10.new_ICD10(Codigo, Nombre, None)
        codigos.append(icd10)
    return codigos

def get_informes(Codigo):
    query = "SELECT IdInforme FROM INFORME_ICD_10 WHERE Codigo ='" + str(Codigo) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    informes = list()
    for(idInforme) in result:
        informes.append(str(idInforme[0]))
    return informes

def get_ICD10(Codigo):
    query = "SELECT * FROM ICD_10 WHERE Codigo ='" + str(Codigo) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    for(Codigo, Nombre) in result:
        icd10 = ICD10()
        icd10.new_ICD10(Codigo, Nombre, None)
    return icd10

def create_ICD10(Codigo, Nombre):
    icd10s = lista_ICD10()
    is_include = False
    icd10_result = ICD10()
    print("createICD10")
    print(Codigo)
    for icd10 in icd10s:
        if Codigo == icd10.Codigo:
            is_include = True
            icd10_result = icd10
    if not is_include:
        print("leggoooooo")
        query = "INSERT INTO ICD_10 (Codigo, Nombre) VALUES (\"" + str(Codigo) + "\", \"" + str(Nombre) + "\");"
        connection = conn.get_connection()
        conn.update_query(query, connection)
        conn.close_connection(connection)
        print(query)
        icd10_result.new_ICD10(Codigo, Nombre)
    else:
        icd10_result
    return icd10_result
