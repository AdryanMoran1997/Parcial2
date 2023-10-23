import tkinter as tk
import tkinter.messagebox

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def insert_curp_and_tramite(self):
        curp = self.view.curp_entry.get()
        tramite = self.view.tramite_entry.get()

        estado_tramite = "Resolved" if self.view.estado_tramite_var.get() == 1 else "Pending"

        if self.validate_curp(curp):
            self.model.insert_data(
                curp, 
                self.view.name_entry.get(),
                self.view.paterno_entry.get(),
                self.view.materno_entry.get(),
                self.view.municipality_entry.get(),
                self.view.escuela_entry.get(),
                tramite,
                self.view.telefono_entry.get(),
                self.view.correo_entry.get(),
                estado_tramite
            )
            self.view.clear_entry_fields()
        else:
            # Mostrar un mensaje de error en la interfaz si la CURP no es válida
            tk.messagebox.showerror("Error", "La CURP no es válida")

    def view_students(self):
        students = self.model.view_students()
        self.view.display_students(students)

    def validate_curp(self, curp):
        # Validar la longitud de la CURP
        if len(curp) != 18:
            return False

        # Verificar que los primeros 4 caracteres sean letras mayúsculas
        if not curp[:4].isalpha():
            return False

        # Verificar que los siguientes 6 caracteres sean dígitos
        if not curp[4:10].isdigit():
            return False

        # Verificar que el siguiente carácter sea 'H' o 'M'
        if curp[10] not in ('H', 'M'):
            return False

        # Verificar que los siguientes 5 caracteres sean letras mayúsculas
        if not curp[11:16].isalpha():
            return False

        # Verificar que los últimos 2 caracteres sean números o letras
        last_two_chars = curp[-2:]
        if not last_two_chars.isalnum():
            return False
        return True