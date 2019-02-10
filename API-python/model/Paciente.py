import mysqlConnection as conn

class Paciente:
    def __init__(self):
        self.idPaciente = None
        self.Nombre = None
        self.NUSS = None
        self.Sexo = None
        self.Fecha_nacimiento = None
        self.Localidad = None
        self.Domicilio = None
        self.Apellidos = None
        self.Telefono = None
        self.Correo_electronico = None
        self.Embarazada = None
        self.FPP = None
        self.historial = None
        self.Licencia = None

    def new_paciente(self, idPaciente, Nombre, NUSS, Sexo, Fecha_nacimiento, Localidad, Domicilio, Apellidos, Telefono, Correo_electronico, Embarazada, FPP, historial=None, Licencia = None):
        self.idPaciente = idPaciente is None and len(lista_pacientes())+1 or idPaciente
        self.Nombre = Nombre
        self.NUSS = NUSS
        self.Sexo = Sexo
        self.Fecha_nacimiento = Fecha_nacimiento
        self.Localidad = Localidad
        self.Domicilio = Domicilio
        self.Apellidos = Apellidos
        self.Telefono = Telefono
        self.Correo_electronico = Correo_electronico
        self.Embarazada = Embarazada
        self.FPP = FPP
        if historial is None:
            self.historial = get_historial(self.idPaciente)
        else:
            self.historial = historial
        if Licencia is None:
            self.Licencia = get_Licencia(self.idPaciente)
        else:
            self.Licencia = Licencia

    def update_paciente(self, Localidad, Domicilio, Telefono, Correo_electronico, Embarazada, FPP):
        self.Localidad = Localidad is None and self.Localidad or Localidad
        self.Domicilio = Domicilio is None and self.Domicilio or Domicilio
        self.Telefono = Telefono is None and self.Telefono or Telefono
        self.Correo_electronico = Correo_electronico is None and self.Correo_electronico or Correo_electronico
        self.Embarazada = Embarazada is None and self.Embarazada or Embarazada
        self.FPP = FPP is None and self.FPP or FPP
        query = list()
        query.append("UPDATE Paciente SET "\
                + "Localidad='" + self.Localidad + "', "\
                + "Domicilio='" + self.Domicilio + "', "\
                + "Telefono='" + self.Telefono + "', "\
                + "Correo_electronico='" + str(self.Correo_electronico) + "', "\
                + "Embarazada=" + str(self.Embarazada) + ", "\
                #+ "FPP='" + self.FPP.strftime('%Y-%m-%d') + "' "\
                + "FPP='" + str(self.FPP) + "' "\
                + "WHERE idPaciente = " + str(self.idPaciente) + ";")
        connection = conn.get_connection()
        conn.update_query(query, connection)
        conn.close_connection(connection)


def lista_pacientes():
    query = "SELECT * FROM Paciente;"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    pacientes = list()
    conn.close_connection(connection)
    for (idPaciente, Nombre, NUSS, Sexo, Fecha_nacimiento, Localidad, Domicilio, Apellidos, Telefono, Correo_electronico,
         Embarazada, FPP) in result:
        paciente = Paciente()
        paciente.new_paciente(idPaciente, Nombre, NUSS, Sexo, Fecha_nacimiento, Localidad, Domicilio, Apellidos, Telefono, Correo_electronico,
         str(Embarazada), FPP)
        pacientes.append(paciente)
    return pacientes

def lista_pacientes_embarazadas():
    query = "SELECT * FROM Paciente;"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    pacientes = list()
    conn.close_connection(connection)
    for (idPaciente, Nombre, NUSS, Sexo, Fecha_nacimiento, Localidad, Domicilio, Apellidos, Telefono, Correo_electronico,
         Embarazada, FPP) in result:
        paciente = Paciente()
        print(Embarazada)
        if Embarazada==1:
            paciente.new_paciente(idPaciente, Nombre, NUSS, Sexo, Fecha_nacimiento, Localidad, Domicilio, Apellidos, Telefono, Correo_electronico,
                                  str(Embarazada), FPP)
            pacientes.append(paciente)
    return pacientes

def get_historial(idPaciente):
    query = "SELECT idHistorial FROM Historial WHERE idPaciente =" + str(idPaciente) + ";"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    hist = None
    for(idHistorial) in result:
        hist = idHistorial[0]
    return hist

def get_Licencia(idPaciente):
    query = "SELECT Licencia FROM es_atendido WHERE idPaciente =" + str(idPaciente) + ";"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    licencias = list()
    for (Licencia) in result:
        licencias.append(str(Licencia[0]))
    return licencias

def pacientes_filter(pacientes, idPaciente, Apellidos, Embarazada):
    res = list()
    for paciente in pacientes:
        if idPaciente is None:
            isID = True
        else:
            isID = idPaciente.upper() in paciente.idPaciente.upper()
        if Apellidos is None:
            isApellidos = True
        else:
            isApellidos = Apellidos.upper() in paciente.genero.upper()
        if Embarazada is None:
            isEmbarazada = True
        else:
            isEmbarazada = Embarazada in str(paciente.Embarazada)
        if isApellidos and isID and isEmbarazada:
            res.append(paciente)
    return res


def get_paciente(idPaciente):
    query = "SELECT * FROM Paciente WHERE idPaciente =" + str(idPaciente) + ";"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    for(idPaciente, Nombre, NUSS, Sexo, Fecha_nacimiento, Localidad, Domicilio, Apellidos, Telefono, Correo_electronico, Embarazada, FPP) in result:
        paciente = Paciente()
        paciente.new_paciente(idPaciente, Nombre, NUSS, Sexo, Fecha_nacimiento, Localidad, Domicilio, Apellidos, Telefono, Correo_electronico, str(Embarazada), FPP, None, None)
    return paciente

"""
def peliculas_filter(peliculas, titulo, genre, year):
    res = list()
    for pelicula in peliculas:
        if titulo is None:
            isTitulo = True
        else:
            isTitulo = titulo.upper() in pelicula.titulo.upper()
        if genre is None:
            isGenre = True
        else:
            isGenre = genre.upper() in pelicula.genero.upper()
        if year is None:
            isYear = True
        else:
            isYear = year in str(pelicula.fecha_de_lanzamiento)
        if isGenre and isTitulo and isYear:
            res.append(pelicula)
    return res


    def insert_pelicula(self):
        self.oid_pelicula = len(lista_peliculas())+1
        query = list()
        query.append("INSERT INTO Pelicula VALUES(" + str(self.oid_pelicula) + ", '" + self.genero + "', " + str(self.votacion) + ", '" \
                + self.fecha_de_lanzamiento + "', '" + "image" + "', '" + self.sinopsis + "', '" + self.pais \
                + "', '" + self.titulo + "', " + str(self.director) + " );")
        for actor in self.actores:
            query.append("INSERT INTO es_interpretada VALUES(" + str(self.oid_pelicula)  + ", "  + str(actor) +  " );")
        connection = conn.get_connection()
        conn.update_query(query, connection)
        conn.close_connection(connection)


    def delete_pelicula(self):
        query = list()
        query.append("DELETE FROM Pelicula WHERE oid_pelicula =" + str(self.oid_pelicula)  + ";")
        query.append("DELETE FROM es_interpretada WHERE pelicula_oid =" + str(self.oid_pelicula)  + ";")
        connection = conn.get_connection()
        conn.update_query(query, connection)
        conn.close_connection(connection)
        self.oid_pelicula = None
        self.genero = None
        self.votacion = None
        self.fecha_de_lanzamiento = None
        self.imagen = None
        self.sinopsis = None
        self.pais = None
        self.titulo = None
        self.director = None
        self.actores = None
"""