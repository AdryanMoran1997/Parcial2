from model import Model
from controller import Controller
from view import View
import tkinter as tk

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