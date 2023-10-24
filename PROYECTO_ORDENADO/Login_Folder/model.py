import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'e'
}

class Modelo:
    def __init__(self):
        self.db = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.db.cursor()

    def validar_usuario(self, usuario, contrasena):
        query = "SELECT id, nombre, paterno, materno FROM admin WHERE usuario = %s AND contraseña = %s"
        self.cursor.execute(query, (usuario, contrasena))
        result = self.cursor.fetchone()
        return result
