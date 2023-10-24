import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tramite_form import TramiteForm
from Registro_form import RegistroForm

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

class VistaLogin:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Inicio de Sesión")

        self.create_ui()

    def create_ui(self):
        # Aumentar el tamaño de la fuente
        font = ('Helvetica', 16)

        self.username_label = tk.Label(self.root, text="Usuario:", font=font)
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root, font=font)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Contraseña:", font=font)
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*", font=font)
        self.password_entry.pack()

        login_button = tk.Button(self.root, text="Iniciar Sesión", command=self.controlador.login, font=font)
        login_button.pack()

        register_button = tk.Button(self.root, text="Registrarse", command=self.controlador.register, font=font)
        register_button.pack()

    def get_credentials(self):
        return self.username_entry.get(), self.password_entry.get()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

class Controlador:
    def __init__(self):
        self.model = Modelo()
        self.login_window = tk.Tk()
        self.login_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.view = VistaLogin(self.login_window, self)

    def login(self):
        usuario, contrasena = self.view.get_credentials()
        result = self.model.validar_usuario(usuario, contrasena)
        if result:
            self.view.show_message("Inicio de Sesión", f"Inicio de sesión exitoso. Bienvenido, {result[1]} {result[2]} {result[3]}")
            self.login_window.destroy()
            self.open_tramite_form(result[0])
        else:
            self.view.show_message("Inicio de Sesión", "Inicio de sesión fallido. Inténtalo de nuevo")

    def register(self):
        register_window = tk.Toplevel(self.login_window)
        register_form = RegistroForm(register_window)
        register_window.mainloop()

    def open_tramite_form(self, user_id):
        main_window = tk.Tk()
        tramite_form = TramiteForm(main_window, user_id)
        main_window.mainloop()

    def on_closing(self):
        # Cerrar la base de datos de manera segura
        self.model.db.close()
        # Destruir la ventana de la aplicación
        self.login_window.destroy()

    def run(self):
        self.login_window.mainloop()

if __name__ == "__main__":
    app = Controlador()
    app.run()
