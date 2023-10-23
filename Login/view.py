import tkinter as tk
from tkinter import messagebox

class VistaLogin:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Inicio de Sesión")

        self.create_ui()

    def create_ui(self):
        self.username_label = tk.Label(self.root, text="Usuario:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Contraseña:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        login_button = tk.Button(self.root, text="Iniciar Sesión", command=self.controlador.login)
        login_button.pack()

        register_button = tk.Button(self.root, text="Registrarse", command=self.controlador.register)
        register_button.pack()

    def get_credentials(self):
        return self.username_entry.get(), self.password_entry.get()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)