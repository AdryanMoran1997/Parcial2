import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import matplotlib.pyplot as plt

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'e'
}

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Control")

        self.tabControl = ttk.Notebook(root)
        self.tab_estudiantes = ttk.Frame(self.tabControl)
        self.tab_tramites = ttk.Frame(self.tabControl)
        self.tab_admins = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab_estudiantes, text="Estudiantes")
        self.tabControl.add(self.tab_tramites, text="Trámites")
        self.tabControl.add(self.tab_admins, text="Admins")
        self.tabControl.pack(expand=1, fill="both")

        # Estudiantes Tab
        self.estudiantes_tree = ttk.Treeview(self.tab_estudiantes, columns=("curp", "nombre", "paterno", "materno", "municipio", "escuela", "tramite", "telefono", "correo"))
        self.estudiantes_tree.heading("#1", text="CURP")
        self.estudiantes_tree.heading("#2", text="Nombre")
        self.estudiantes_tree.heading("#3", text="Paterno")
        self.estudiantes_tree.heading("#4", text="Materno")
        self.estudiantes_tree.heading("#5", text="Municipio")
        self.estudiantes_tree.heading("#6", text="Escuela")
        self.estudiantes_tree.heading("#7", text="Trámite")
        self.estudiantes_tree.heading("#8", text="Teléfono")
        self.estudiantes_tree.heading("#9", text="Correo")
        self.estudiantes_tree.pack()

        # Trámites Tab
        self.tramites_tree = ttk.Treeview(self.tab_tramites, columns=("curp", "tramite", "turno", "fecha", "hora"))
        self.tramites_tree.heading("#1", text="CURP")
        self.tramites_tree.heading("#2", text="Trámite")
        self.tramites_tree.heading("#3", text="Turno")
        self.tramites_tree.heading("#4", text="Fecha")
        self.tramites_tree.heading("#5", text="Hora")
        self.tramites_tree.pack()

        # Admins Tab
        self.admins_tree = ttk.Treeview(self.tab_admins, columns=("id", "usuario", "nombre", "paterno", "materno", "telefono"))
        self.admins_tree.heading("#1", text="ID")
        self.admins_tree.heading("#2", text="Usuario")
        self.admins_tree.heading("#3", text="Nombre")
        self.admins_tree.heading("#4", text="Paterno")
        self.admins_tree.heading("#5", text="Materno")
        self.admins_tree.heading("#6", text="Teléfono")
        self.admins_tree.pack()

        # Cargar datos desde la base de datos
        self.load_data()

    def load_data(self):
        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

        
            cursor.execute("SELECT * FROM estudiante")
            estudiantes_data = cursor.fetchall()
            for estudiante in estudiantes_data:
                self.estudiantes_tree.insert("", "end", values=estudiante)


            cursor.execute("SELECT * FROM tramite")
            tramites_data = cursor.fetchall()
            for tramite in tramites_data:
                self.tramites_tree.insert("", "end", values=tramite)

      
            cursor.execute("SELECT * FROM admin")
            admins_data = cursor.fetchall()
            for admin in admins_data:
                self.admins_tree.insert("", "end", values=admin)

        
            self.plot_tramite_data(tramites_data)

            db.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def plot_tramite_data(self, tramites_data):
        turnos = {}
        estados = {}

        for tramite in tramites_data:
            turno = tramite[2]
            estado = tramite[5]

            if turno in turnos:
                turnos[turno] += 1
            else:
                turnos[turno] = 1

            if estado in estados:
                estados[estado] += 1
            else:
                estados[estado] = 1

        plt.figure(figsize=(8, 4))
        plt.bar(turnos.keys(), turnos.values())
        plt.xlabel("Turno")
        plt.ylabel("Cantidad")
        plt.title("Distribución de Turnos de Trámites")
        plt.show()

        # Crear un gráfico de barras para los estados
        plt.figure(figsize=(8, 4))
        plt.bar(estados.keys(), estados.values())
        plt.xlabel("Estado del Trámite")
        plt.ylabel("Cantidad")
        plt.title("Distribución de Estados de Trámites")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
