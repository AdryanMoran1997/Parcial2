import tkinter as tk
from tkinter import ttk
from Estudiante import Model
from Estudiante import Controller
from Estudiante import View
from Login import Controlador

class MyAppFactory:
    def create_my_app(self):
        app = MyApp()
        app.create_controller()
        return app

class ControladorFactory:
    def create_controlador(self):
        app = Controlador()
        return app

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.Controller = None
        self.view = None

    def create_controller(self):
        self.controller = Controller(self.model, None)
        self.view = View(self.root, self.controller)
        self.controller.view = self.view

    def run(self):
        self.root.mainloop()

def open_my_app():
    my_app_factory = MyAppFactory()
    app = my_app_factory.create_my_app()
    app.run()

root = tk.Tk()
root.title("Menu Principal")
root.geometry("400x200")

label = tk.Label(root, text="Menu Principal", font=("Arial", 14))
label.pack()

style = ttk.Style()

# Configurar la fuente, el tamaño de letra y el color del texto para los botones
style.configure("TButton", padding=10, relief="flat", background="#3498db", foreground="black", font=("Helvetica", 12))
style.map("TButton",
    background=[("active", "#2980b9")],
    foreground=[("active", "black")]
)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

def create_button(text, command):
    button = ttk.Button(button_frame, text=text, command=command)
    button.pack(side="left", padx=10, pady=10)
    return button

def open_controlador():
    controlador_factory = ControladorFactory()
    app = controlador_factory.create_controlador()
    app.run()

button1 = create_button("Registro de estudiante", open_my_app)
button2 = create_button("Acceso admin", open_controlador)

root.mainloop()
