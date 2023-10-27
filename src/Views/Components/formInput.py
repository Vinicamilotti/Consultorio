from customtkinter import *
from src.Views.Heranca import Heranca


class InputForm(Heranca):
    def __init__(self, master, fieldName: str):
        super().__init__(master)
        self.txtField = CTkEntry(self, width=300)
        self.txtField.grid(row=1, column=0)
        self.nomeLabel = CTkLabel(self, text=fieldName)
        self.nomeLabel.grid(column=0, row=0, sticky="nw")

    def getValue(self):
        return self.txtField.get()
