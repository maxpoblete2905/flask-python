import mysql.connector

def conectar():
    try:
        # Establece la conexión con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="example_user",
            password="example_password",
            database="example_database",
            port=3306
        )
        print("Conexión establecida correctamente")
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectarse a MySQL:", error)
        return None

def cerrar(conexion):
    if conexion:
        conexion.close()
        print("Conexión cerrada")
