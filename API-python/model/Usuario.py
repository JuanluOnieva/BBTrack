import mysqlConnection as conn

class Usuario:
    def __init__(self):
        self.idUsuario = None
        self.PSS = None

    def new_usuario(self, idUsuario, PSS):
        self.idUsuario = idUsuario
        self.PSS = PSS


def lista_usuarios():
    query = "SELECT * FROM Usuario;"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    usuarios = list()
    conn.close_connection(connection)
    for (idUsuario, PSS) in result:
        usuario = Usuario()
        usuario.new_usuario(idUsuario, PSS)
        usuarios.append(usuario)
    return usuarios

def get_usuario(idUsuario):
    query = "SELECT * FROM Usuario WHERE idUsuario ='" + str(idUsuario) + "';"
    connection = conn.get_connection()
    result = conn.execute_query(query, connection)
    conn.close_connection(connection)
    for (idUsuario, PSS) in result:
        usuario = Usuario()
        usuario.new_usuario(idUsuario, PSS)
    return usuario