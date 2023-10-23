import tkinter as tk
from tkinter import messagebox
from database import DatabaseSingleton
import mysql.connector

class RegistroForm:
    def __init__(self, register_window):
        self.register_window = register_window
        self.register_window.title("Registro de Nuevo Usuario")

        self.create_ui()
        self.db_singleton = DatabaseSingleton()

    def create_ui(self):
        # Etiquetas y campos de entrada para el registro de nuevo usuario
        username_label = tk.Label(self.register_window, text="Usuario:")
        username_label.pack()
        self.username_entry = tk.Entry(self.register_window)
        self.username_entry.pack()

        password_label = tk.Label(self.register_window, text="Contraseña:")
        password_label.pack()
        self.password_entry = tk.Entry(self.register_window, show="*")
        self.password_entry.pack()

        nombre_label = tk.Label(self.register_window, text="Nombre:")
        nombre_label.pack()
        self.nombre_entry = tk.Entry(self.register_window)
        self.nombre_entry.pack()

        paterno_label = tk.Label(self.register_window, text="Apellido Paterno:")
        paterno_label.pack()
        self.paterno_entry = tk.Entry(self.register_window)
        self.paterno_entry.pack()

        materno_label = tk.Label(self.register_window, text="Apellido Materno:")
        materno_label.pack()
        self.materno_entry = tk.Entry(self.register_window)
        self.materno_entry.pack()

        telefono_label = tk.Label(self.register_window, text="Teléfono:")
        telefono_label.pack()
        self.telefono_entry = tk.Entry(self.register_window)
        self.telefono_entry.pack()

        # Botón para realizar el registro
        register_button = tk.Button(self.register_window, text="Registrar", command=self.register)
        register_button.pack()

    def register(self):
        usuario = self.username_entry.get()
        contrasena = self.password_entry.get()
        nombre = self.nombre_entry.get()
        paterno = self.paterno_entry.get()
        materno = self.materno_entry.get()
        telefono = self.telefono_entry.get()

        try:
            db = self.db_singleton.get_connection()
            cursor = db.cursor()

            query = "INSERT INTO admin (usuario, contraseña, nombre, paterno, materno, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (usuario, contrasena, nombre, paterno, materno, telefono))
            db.commit()

            messagebox.showinfo("Registro Exitoso", "El nuevo usuario ha sido registrado con éxito.")

        except mysql.connector.Error as err:
            print("Error:", err)

    def close(self):
        self.register_window.destroy()
