import mysqlConnection as conn

class Medico:
    def __init__(self):
        self.Licencia = None
        self.Nombre = None
        self.Apellidos = None
        self.Sexo = None
        self.Especialidad = None
        self.informes = None
        self.Pacientes = None


    def new_medico(self, Licencia, Nombre, Apellidos, Sexo, Especialidad, informes = None, Pacientes = None):
        self.Licencia = Licencia is None and len(lista_medicos()) + 1 or Licencia
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Sexo = Sexo
        self.Especialidad = Especialidad
        if informes is None:
            self.informes = get_informes(self.Licencia)
        else:
            self.informes = informes
        if Pacientes is None:
            self.Pacientes = get_pacientes(self.Licencia)
        else:
            self.Pacientes = Pacientes


def lista_medicos():
        query = "SELECT * FROM Medico;"
        connection = conn.get_connection()
        result = conn.execute_query(query, connection)
        medicos = list()
        conn.close_connection(connection)
        for (Licencia, Nombre, Apellidos, Sexo, Especialidad) in result:
            medico = Medico()
            medico.new_medico(Licencia, Nombre, Apellidos, Sexo, Especialidad, None, None)
            medicos.append(medico)
        return medicos

def get_informes(Licencia):
    query = "SELECT idInforme FROM Informe WHERE Licencia_medico ='" + str(Licencia) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    informes = list()
    if result:
        for (idInforme) in result:
            informes.append(str(idInforme[0]))
    return informes

def get_pacientes(Licencia):
    query = "SELECT idPaciente FROM es_atendido WHERE Licencia ='" + str(Licencia) + "';"
    print(query)
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    pacientes = list()
    if result:
        for (idPaciente) in result:
            pacientes.append(str(idPaciente[0]))
            print(idPaciente)
    return pacientes

def get_medico(Licencia):
    query = "SELECT * FROM Medico WHERE Licencia ='" + str(Licencia) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    for(Licencia, Nombre, Apellidos, Sexo, Especialidad) in result:
        medico = Medico()
        medico.new_medico(Licencia, Nombre, Apellidos, Sexo, Especialidad, None, None)
    return medico