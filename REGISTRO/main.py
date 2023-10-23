import tkinter as tk
from registro_form import RegistroForm

if __name__ == "__main__":
    register_root = tk.Tk()
    registro_form = RegistroForm(register_root)
    register_root.mainloop()