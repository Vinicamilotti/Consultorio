from ....Views import Heranca
from customtkinter import *
from src.controllers.pacientesController import PacientesController
import os
from tkinter import ttk
from utils.fileOpener import openFile
import tkinter as tk
import datetime
from pathlib import Path

class PacientePage(Heranca):
    def __init__(self, master: any, idPaciente: int):
        super().__init__(master)
        self.id = idPaciente
        self.controller = PacientesController()
        self.dados = self.getDados()
        self.nome = self.dados[0][1]
        self.caminho = os.path.join(os.getcwd(),"Data", "Pacientes", self.nome, "Laudos")
        self.columns = ("laudo")
        self.titulo = CTkLabel(self,text=self.nome)
        self.titulo.grid(row=0, column=0)
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")
        self.tree.propagate(True)
        self.tree.heading("laudo", text="Laudo")
        self.tree.grid(
            row=1,
            column=0,
            sticky="nsew",
        )
        self.tree.insert("", tk.END, values=self.getLaudos())
        self.btnNovoLaudo = CTkButton(self, command=self.novoLaudo, text="novo")
        self.btnNovoLaudo.grid(row=2, column=0)

    def getDados(self):
        return self.controller.getById(self.id)

    def getLaudos(self):
        return os.listdir(self.caminho)

    def novoLaudo(self):
        timestamp = f"{datetime.date.today()}{datetime.time.hour}{datetime.time.minute}"
        name = f"{self.nome}{timestamp}.docx"
        novoLaudoPath = Path(os.path.join(self.caminho, name))
        openFile(novoLaudoPath)
