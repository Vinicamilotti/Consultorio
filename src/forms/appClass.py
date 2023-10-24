from customtkinter import *
from ..components import SelecionarPaciente
from pathlib import Path


class App(CTk):
    def __init__(self, appPath: Path):
        super().__init__()
        self.appPath = appPath
        self.geometry("1024x768")
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
        self.tabela = SelecionarPaciente(self)
        self.tabela.grid(column=1, row=3)
