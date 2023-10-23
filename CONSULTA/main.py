import tkinter as tk
from tramite_form import TramiteForm

if __name__ == "__main__":
    root = tk.Tk()
    user_id = 1  # Reemplaza con el ID de usuario después de iniciar sesión
    tramite_form = TramiteForm(root, user_id)
    root.mainloop()
