import tkinter as tk
from vista_login import VistaLogin
from Login_Folder.model import Modelo
from tramite_form.Tramite_Form import TramiteForm
from registro_form.RegistroForm import RegistroForm

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
