from src.controllers.pacientesController import PacientesController
from src.Views.Components.gridView import GridView
from tkinter.filedialog import askopenfilename
from utils.fileOpener import openFile
from src.Views import Heranca
from customtkinter import *
from pathlib import Path
import datetime
import shutil
import os


class PacientePage(Heranca):
    def __init__(self, master: any, idPaciente: int):
        super().__init__(master)
        self.id = idPaciente
        self.controller = PacientesController()
        self.dados = self.getDados()
        self.nome = self.dados[0][1]
        self.caminho = os.path.join(os.getcwd(), "Data", "Pacientes", self.nome, "Laudos")
        self.titulo = CTkLabel(self, text=self.nome)
        self.titulo.grid(row=0, column=0)
        self.topBtns = CTkFrame(self)
        self.topBtns.grid(column=0, row=1, sticky="wn")

        self.btimportar = CTkButton(self.topBtns, command=self.importarLaudo, text="Importar Laudo")
        self.btimportar.grid(row=0, column=1, sticky="ne")

        self.btnexportar = CTkButton(self.topBtns, command=self.abrirLaudo, text="Compartilhar")
        self.btnexportar.grid(row=0, column=3, sticky="ne", padx=5)

        self.tree = GridView(self, columns=["laudo"], headings=["laudo"], data=self.getLaudos())
        self.tree.grid(
            row=2,
            column=0,
            sticky="nsew",
        )
        self.frBotoes = CTkFrame(self)
        self.frBotoes.grid(row=3, column=0, sticky="nw")

        self.btnNovoLaudo = CTkButton(self.frBotoes, command=self.novoLaudo, text="Novo Laudo")
        self.btnNovoLaudo.grid(row=0, column=0, sticky="nw")
        self.btnAbrirLaudo = CTkButton(self.frBotoes, command=self.abrirLaudo, text="Abrir Laudo")
        self.btnAbrirLaudo.grid(row=0, column=1, sticky="nw")

    def getDados(self):
        return self.controller.getById(self.id)

    def getLaudos(self):
        return self.controller.getLaudos(Path(self.caminho))

    def novoLaudo(self):
        timestamp = str(datetime.datetime.now()).replace(" ", "").replace(":", "-").replace(".", "")
        name = f"{self.nome}{timestamp}.docx"
        novoLaudoPath = Path(os.path.join(self.caminho, name))
        openFile(novoLaudoPath)
        self.tree.state.setState(self.getLaudos())
        self.tree.showGrid()

    def abrirLaudo(self):
        item = self.tree.getSelecionado()
        arquivo = f"{item[0]}.docx"
        abrir = Path(os.path.join(self.caminho, arquivo))
        openFile(abrir)

    def importarLaudo(self):
        dialog = askopenfilename(filetypes=[("Docs", ["*.docx", "*.doc", "*.odt"])])
        shutil.copy(dialog, self.caminho)
        self.tree.state.setState(self.getLaudos())
        self.tree.showGrid()
