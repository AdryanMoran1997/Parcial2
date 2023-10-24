import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'e'
}

class TramiteForm:
    _instance = None

    def __new__(cls, main_window, user_id):
        if cls._instance is None:
            cls._instance = super(TramiteForm, cls).__new__(cls)
            cls._instance.main_window = main_window
            cls._instance.user_id = user_id
            cls._instance.tramite_window = tk.Toplevel(cls._instance.main_window)
            cls._instance.tramite_window.title("Gestión de Trámites")
            cls._instance.create_ui()
        return cls._instance

    def create_ui(self):
        self.curp_label = tk.Label(self.tramite_window, text="Buscar por CURP:")
        self.curp_label.grid(row=0, column=0)
        self.curp_entry = tk.Entry(self.tramite_window)
        self.curp_entry.grid(row=0, column=1)

        search_button = tk.Button(self.tramite_window, text="Buscar", command=self.search_tramite)
        search_button.grid(row=0, column=2)

        self.details_label = tk.Label(self.tramite_window, text="Detalles:")
        self.details_label.grid(row=1, column=0)
        self.details_text = tk.Text(self.tramite_window, width=40, height=10)
        self.details_text.grid(row=2, column=0, columnspan=3)

        view_details_button = tk.Button(self.tramite_window, text="Ver Detalles", command=self.show_details)
        view_details_button.grid(row=3, column=0)

        self.new_state_label = tk.Label(self.tramite_window, text="Nuevo Estado:")
        self.new_state_label.grid(row=4, column=0)
        self.new_state_entry = tk.Entry(self.tramite_window)
        self.new_state_entry.grid(row=4, column=1)

        self.new_turno_label = tk.Label(self.tramite_window, text="Nuevo Turno:")
        self.new_turno_label.grid(row=5, column=0)
        self.new_turno_entry = tk.Entry(self.tramite_window)
        self.new_turno_entry.grid(row=5, column=1)

        self.new_fecha_label = tk.Label(self.tramite_window, text="Nueva Fecha:")
        self.new_fecha_label.grid(row=6, column=0)
        self.new_fecha_entry = tk.Entry(self.tramite_window)
        self.new_fecha_entry.grid(row=6, column=1)

        self.new_hora_label = tk.Label(self.tramite_window, text="Nueva Hora:")
        self.new_hora_label.grid(row=7, column=0)
        self.new_hora_entry = tk.Entry(self.tramite_window)
        self.new_hora_entry.grid(row=7, column=1)

        update_data_button = tk.Button(self.tramite_window, text="Actualizar Datos", command=self.update_tramite)
        update_data_button.grid(row=8, column=0)

        # Botón para obtener información detallada
        get_info_button = tk.Button(self.tramite_window, text="Obtener Información Detallada", command=self.get_info)
        get_info_button.grid(row=9, column=0)

        # Botón para actualizar estado
        update_state_button = tk.Button(self.tramite_window, text="Actualizar Estado", command=self.update_state)
        update_state_button.grid(row=10, column=0)

        close_button = tk.Button(self.tramite_window, text="Cerrar", command=self.close_window)
        close_button.grid(row=11, column=1)

    def search_tramite(self):
        curp = self.curp_entry.get()
        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

            query = "SELECT * FROM tramite WHERE curp = %s"
            cursor.execute(query, (curp,))
            result = cursor.fetchone()

            if result:
                self.details_text.delete(1.0, tk.END)
                self.details_text.insert(tk.END, f"CURP: {result[0]}\n")
                self.details_text.insert(tk.END, f"Trámite: {result[1]}\n")
                self.details_text.insert(tk.END, f"Turno: {result[2]}\n")
                self.details_text.insert(tk.END, f"Fecha: {result[3]}\n")
                self.details_text.insert(tk.END, f"Hora: {result[4]}\n")
                self.details_text.insert(tk.END, f"Estado Trámite: {result[5]}\n")
            else:
                messagebox.showinfo("Búsqueda de Trámite", "Trámite no encontrado.")

            db.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def show_details(self):
        curp = self.curp_entry.get()
        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

            query = "SELECT * FROM tramite WHERE curp = %s"
            cursor.execute(query, (curp,))
            result = cursor.fetchone()

            if result:
                details = "Detalles completos del Trámite:\n"
                for i, column_name in enumerate(cursor.column_names):
                    details += f"{column_name}: {result[i]}\n"

                self.details_text.delete(1.0, tk.END)
                self.details_text.insert(tk.END, details)
            else:
                messagebox.showinfo("Detalles de Trámite", "Trámite no encontrado.")

            db.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def update_tramite(self):
        curp = self.curp_entry.get()
        new_state = self.new_state_entry.get()
        new_turno = self.new_turno_entry.get()
        new_fecha = self.new_fecha_entry.get()
        new_hora = self.new_hora_entry.get()

        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

            query = "UPDATE tramite SET estado_tramite = %s, turno = %s, fecha = %s, hora = %s WHERE curp = %s"
            cursor.execute(query, (new_state, new_turno, new_fecha, new_hora, curp))
            db.commit()

            messagebox.showinfo("Actualización de Trámite", "Datos del trámite actualizados con éxito.")

            db.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def update_state(self):
        curp = self.curp_entry.get()
        new_state = self.new_state_entry.get()

        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

            query = "UPDATE tramite SET estado_tramite = %s WHERE curp = %s"
            cursor.execute(query, (new_state, curp))
            db.commit()

            messagebox.showinfo("Actualización de Estado", "Estado del trámite actualizado con éxito.")

            db.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def get_info(self):
        curp = self.curp_entry.get()
        try:
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

            query = "SELECT * FROM tramite WHERE curp = %s"
            cursor.execute(query, (curp,))
            result = cursor.fetchone()

            if result:
                details = "Información detallada del Trámite:\n"
                for i, column_name in enumerate(cursor.column_names):
                    details += f"{column_name}: {result[i]}\n"

                self.details_text.delete(1.0, tk.END)
                self.details_text.insert(tk.END, details)
            else:
                messagebox.showinfo("Información Detallada del Trámite", "Trámite no encontrado.")

            db.close()
        except mysql.connector.Error as err:
            print("Error:", err)

    def close_window(self):
        messagebox.showinfo("Cierre Exitoso", "La ventana de trámite se ha cerrado exitosamente.")

        self.tramite_window.destroy()
        

if __name__ == "__main__":
    root = tk.Tk()
    user_id = 1  # Reemplaza con el ID de usuario después de iniciar sesión
    tramite_form = TramiteForm(root, user_id)
    root.mainloop()
