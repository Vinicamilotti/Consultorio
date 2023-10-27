from customtkinter import *
from ..Views.Pages.MainPage.SelecionarPaciente import SelecionarPaciente
from pathlib import Path


class App(CTk):
    def __init__(self, appPath: Path):
        super().__init__()
        self.appPath = appPath
        self.geometry("1024x768")
        # noinspection PyTypeChecker
        self.columnconfigure((0, 1, 2), weight=1)
        # noinspection PyTypeChecker
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.titleStyle = CTkFont(size=48)
        self.apptitle = CTkLabel(self, text="Pacientes", font=self.titleStyle)
        self.apptitle.grid(row=2, column=1)
        self.tabela = SelecionarPaciente(self)
        self.tabela.grid(column=1, row=3)
