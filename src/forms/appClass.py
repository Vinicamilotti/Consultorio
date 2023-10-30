from customtkinter import *
from ..Views.Pages.MainPage.SelecionarPaciente import SelecionarPaciente
from pathlib import Path
from src.Views.Components.Lables.titles import Header1


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Consultório")
        self.geometry("1024x768")
        # noinspection PyTypeChecker
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        # noinspection PyTypeChecker
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.apptitle = Header1(self, text="Pacientes")
        self.apptitle.grid(row=2, column=3)
        self.tabela = SelecionarPaciente(self)
        self.tabela.grid(column=3, row=3, sticky= "n")
        self.sideBar = CTkFrame(self)
        self.sideBar.grid(column=4, row=3, sticky="nw")
        self.btnAtividades = CTkButton(self.sideBar, text="Abrir Atividades")
        self.btnAtividades.grid(column=0, row=0, pady=10)
        self.btnBackup = CTkButton(self.sideBar, text="Fazer Backup")
        self.btnBackup.grid(column=0, row=1, pady=10)
        self.btnRestore = CTkButton(self.sideBar, text="Importar Backup")
        self.btnRestore.grid(column=0, row=2, pady=10)