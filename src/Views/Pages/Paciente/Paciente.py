import os
import shutil
import datetime
from pathlib import Path
from customtkinter import *
from tkinter.filedialog import askopenfilename
from utils.fileOpener import openFile
from src.Views import Heranca
from src.Views.Components.gridView import GridView
from src.controllers.pacientesController import PacientesController
from src.Views.Components.Lables.titles import *
from src.Views.Pages.Paciente.tablaudos import TabLaudos
from src.Views.Pages.Paciente.infotab import InfoTab
class PacientePage(Heranca):
    def __init__(self, master: any, idPaciente: int):
        super().__init__(master)
        self.id = idPaciente
        self.controller = PacientesController()
        self.configure(fg_color="transparent")
        self.dados = self.getDados()
        self.nome = self.dados.nome
        self.titulo = Header2(self, self.nome)
        self.titulo.grid(row=0, column=0)
        self.tabview = CTkTabview(master=self)
        self.tabview.grid(row=1,column=0)
        self.tabview.add("Paciente")  # add tab at the end
        self.tabview.add("Laudos")
        self.tabInfo = InfoTab(self.tabview.tab("Paciente"), paciente=self.dados)
        self.table = TabLaudos(self.tabview.tab("Laudos"), paciente=self.dados)
        self.tabInfo.grid(column=0,row=0, pady=30, padx= 50)
        self.table.grid(column=0, row=0)

    def getDados(self):
        return self.controller.getById(self.id)