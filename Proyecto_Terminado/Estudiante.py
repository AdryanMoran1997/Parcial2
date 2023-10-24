import tkinter as tk
import tkinter.messagebox
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
            tk.messagebox.showinfo("Éxito", "Estudiante registrado Exitoso")
        else:
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


class View:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Registro Estudiante")
        self.controller = controller 

        self.current_row = 0
        self.create_labels_and_entries()
        self.create_radio_buttons()
        self.create_buttons()
        self.create_result_text()

    def create_labels_and_entries(self):
        labels_and_entries = [
            ("CURP", "curp_entry"),
            ("Nombre", "name_entry"),
            ("Paterno", "paterno_entry"),
            ("Materno", "materno_entry"),
            ("Municipo", "municipality_entry"),
            ("Escuela", "escuela_entry"),
            ("Tramite", "tramite_entry"),
            ("Telefono", "telefono_entry"),
            ("Correo", "correo_entry"),
        ]

        for label_text, entry_name in labels_and_entries:
            label = tk.Label(self.root, text=label_text)
            label.grid(row=self.current_row, column=0)

            entry = tk.Entry(self.root)
            entry.grid(row=self.current_row, column=1)
            setattr(self, entry_name, entry)

            self.current_row += 1

    def create_radio_buttons(self):
        self.estado_tramite_var = tk.IntVar()
        resolved_radio = tk.Radiobutton(self.root, text="Resuelto", variable=self.estado_tramite_var, value=1)
        pending_radio = tk.Radiobutton(self.root, text="Pendiente", variable=self.estado_tramite_var, value=0)
        resolved_radio.grid(row=self.current_row, column=0, columnspan=2)
        pending_radio.grid(row=self.current_row + 1, column=0, columnspan=2)
        self.current_row += 2

    def create_buttons(self):
        insert_curp_and_tramite_button = tk.Button(self.root, text="Insert CURP and Tramite", command=self.controller.insert_curp_and_tramite)
        insert_curp_and_tramite_button.grid(row=self.current_row, column=0, columnspan=2)

        view_students_button = tk.Button(self.root, text="Ver Lista de estudiantes", command=self.controller.view_students)
        view_students_button.grid(row=self.current_row + 1, column=0, columnspan=2)

    def create_result_text(self):
        self.result_text = tk.Text(self.root, height=10, width=40)
        self.result_text.grid(row=self.current_row + 2, column=0, columnspan=2)

    def clear_entry_fields(self):
        self.curp_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.paterno_entry.delete(0, tk.END)
        self.materno_entry.delete(0, tk.END)
        self.municipality_entry.delete(0, tk.END)
        self.escuela_entry.delete(0, tk.END)
        self.tramite_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)

    def display_students(self, students):
        self.result_text.delete("1.0", tk.END)
        for row in students:
            student_info = f"CURP: {row[0]}, Nombre: {row[1]}, Paterno: {row[2]}, Materno: {row[3]}, Municipio: {row[4]}, Escuela: {row[5]}, Tramite: {row[6]}, Telefono: {row[7]}, Correo: {row[8]}\n"
            self.result_text.insert(tk.END, student_info + "\n")

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.controller = Controller(self.model, None)  
        self.view = View(self.root, self.controller)  
        self.controller.view = self.view 

    def run(self):
        self.root.mainloop()


app = MyApp()
app.run()
