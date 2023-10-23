import tkinter as tk
class View:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Registro Estudiante")
        self.controller = controller  # Pass the controller to the view

        self.current_row = 0
        self.create_labels_and_entries()
        self.create_radio_buttons()
        self.create_buttons()
        self.create_result_text()

    def create_labels_and_entries(self):
        labels_and_entries = [
            ("CURP", "curp_entry"),
            ("Name", "name_entry"),
            ("Paterno", "paterno_entry"),
            ("Materno", "materno_entry"),
            ("Municipality", "municipality_entry"),
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

        view_students_button = tk.Button(self.root, text="View Students", command=self.controller.view_students)
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
