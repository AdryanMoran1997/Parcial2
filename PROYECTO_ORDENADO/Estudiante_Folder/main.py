import tkinter as tk
from Estudiante_Folder.model import Model
from Estudiante_Folder.controller import Controller
from Estudiante_Folder.view import View
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