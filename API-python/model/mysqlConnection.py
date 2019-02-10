import mysql.connector
from mysql.connector import errorcode


def get_connection():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password='bbtrack123',
                                      host='127.0.0.1',
                                      database='bbTrack')
        '''Conexion Paloma'''
        '''
        cnx = mysql.connector.connect(
            host="localhost",
            port="33061",
            user="root",
            passwd="secret",
            database="bbTrack"
        )'''

        #print("Conexion establecida")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def close_connection(connection):
    if connection.is_connected():
        connection.close()
        #print("MySQL connection is closed")


def execute_query(query, connection):
    result = None
    try:
        cursor = connection.cursor()
        if type(query) is list:
            for q in query:
                cursor.execute(q)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        #print("Sentencia sql ejecutada correctamente")
        return result
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Error en la ejecucion de la sentencia sql".format(error))


def update_query(query, connection):
    result = None
    try:
        cursor = connection.cursor()
        if type(query) is list:
            for q in query:
                cursor.execute(q)
        else:
            cursor.execute(query)
        connection.commit()
        #print("Sentencia sql ejecutada correctamente")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Error en la ejecucion de la sentencia sql".format(error))