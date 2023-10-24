import tkinter as tk
import mysql.connector
from tkinter import ttk
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

        # Crear pestañas
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

        # Botón para mostrar gráfica de municipios
        self.show_municipios_button = tk.Button(self.tab_estudiantes, text="Mostrar Gráfica de Municipios", command=self.show_municipios_chart)
        self.show_municipios_button.pack()

        # Cargar datos desde la base de datos
        self.load_data()

    def load_data(self):
        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

            # Cargar datos de estudiantes
            cursor.execute("SELECT * FROM estudiante")
            estudiantes_data = cursor.fetchall()
            for estudiante in estudiantes_data:
                self.estudiantes_tree.insert("", "end", values=estudiante)

            # Cargar datos de trámites
            cursor.execute("SELECT * FROM tramite")
            tramites_data = cursor.fetchall()
            for tramite in tramites_data:
                self.tramites_tree.insert("", "end", values=tramite)

            # Cargar datos de admins
            cursor.execute("SELECT * FROM admin")
            admins_data = cursor.fetchall()
            for admin in admins_data:
                self.admins_tree.insert("", "end", values=admin)

            db.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def show_municipios_chart(self):
        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

            cursor.execute("SELECT municipio FROM estudiante")
            municipios_data = cursor.fetchall()

            municipios = {}

            for municipio in municipios_data:
                municipio = municipio[0]
                if municipio in municipios:
                    municipios[municipio] += 1
                else:
                    municipios[municipio] = 1

            # Crear un gráfico de barras para los municipios
            plt.figure(figsize=(10, 6))
            plt.bar(municipios.keys(), municipios.values())
            plt.xlabel("Municipio")
            plt.ylabel("Cantidad de Estudiantes")
            plt.title("Distribución de Estudiantes por Municipio")
            plt.xticks(rotation=90)
            plt.show()

            db.close()
        except mysql.connector.Error as err:
            print("Error:", err)

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
