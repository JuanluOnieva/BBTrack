import mysqlConnection as conn

class Historial:
    def __init__(self):
        self.idHistorial = None
        self.Fecha_primera_consulta = None
        self.idPaciente = None
        self.Vacunas = None
        self.informes = None
        self.FRR = None

    def new_historial(self, idHistorial, Fecha_primera_consulta, idPaciente, Vacunas, informes = None, FRR = None):
        self.idHistorial = idHistorial is None and 'H-' + idPaciente or idHistorial
        self.Fecha_primera_consulta = Fecha_primera_consulta
        self.idPaciente = idPaciente
        self.Vacunas = Vacunas
        if informes is None:
            self.informes = get_informes(self.idHistorial)
        else:
            self.informes = informes
        if FRR is None:
            self.FRR = get_FRR(self.idHistorial)
        else:
            self.FRR = FRR


def lista_historial():
    query = "SELECT * FROM Historial;"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    historiales = list()
    conn.close_connection(connection)
    for (idHistorial, Fecha_primera_consulta, idPaciente, Vacunas) in result:
        historial = Historial()
        historial.new_historial(idHistorial, Fecha_primera_consulta, idPaciente, Vacunas, None, None)
        historiales.append(historial)
    return historiales

def get_informes(idHistorial):
    query = "SELECT idInforme FROM Informe WHERE idHistorial ='" + str(idHistorial) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    informes = list()
    if result:
        for(idInforme) in result:
            informes.append(str(idInforme[0]))
    return informes

def get_FRR(idHistorial):
    query = "SELECT * FROM FACTOR_DE_RIESGO_PRENATAL WHERE idHistorial ='" + str(idHistorial) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    FRR = dict()
    for(Antecedentes_familiares, Factores_psicosociales, Antecedentes_obstetricos,
        Antecedentes_personales, Patologia_materna, Riesgos_especificos, Exposicion_a_teratogenos, idHistorial) in result:
        FRR['Antecedentes_familiares'] = Antecedentes_familiares
        FRR['Factores_psicosociales'] = Factores_psicosociales
        FRR['Antecedentes_obstetricos'] = Antecedentes_obstetricos
        FRR['Antecedentes_personales'] = Antecedentes_personales
        FRR['Patologia_materna'] = Patologia_materna
        FRR['Riesgos_especificos'] = Riesgos_especificos
        FRR['Exposicion_a_teratogenos'] = Exposicion_a_teratogenos
    return FRR

def get_historial(idHistorial):
    query = "SELECT * FROM Historial WHERE idHistorial ='" + str(idHistorial) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    for(idHistorial, Fecha_primera_consulta, idPaciente, Vacunas) in result:
        historial = Historial()
        historial.new_historial(idHistorial, Fecha_primera_consulta, idPaciente, Vacunas, None, None)
    return historial