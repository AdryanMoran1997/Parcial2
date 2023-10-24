import mysql.connector

class Model:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="E"
        )
        self.cursor = self.db.cursor()
        self.current_turno = 0

    def insert_data(self, curp, name, paterno, materno, municipality, escuela, tramite, telefono, correo, estado_tramite):

        student_query = "INSERT INTO estudiante (curp, nombre, paterno, materno, municipio, escuela, tramite, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        student_values = (curp, name, paterno, materno, municipality, escuela, tramite, telefono, correo)
        self.cursor.execute(student_query, student_values)

      
        tramite_query = "INSERT INTO tramite (curp, tramite, turno, fecha, hora, estado_tramite) VALUES (%s, %s, %s, NOW(), NOW(), %s)"
        tramite_values = (curp, tramite, self.current_turno, estado_tramite)
        self.cursor.execute(tramite_query, tramite_values)
        self.db.commit()

    def view_students(self):
        self.cursor.execute("SELECT * FROM estudiante")
        result = self.cursor.fetchall()
        return result