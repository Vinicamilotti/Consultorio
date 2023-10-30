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
        self.caminho = os.path.join(os.getcwd(), "Data", "Pacientes", self.nome, "Laudos")

        self.topBtns = CTkFrame(self.tabview.tab("Laudos"))
        self.topBtns.grid(column=0, row=1, sticky="wn")

        self.btimportar = CTkButton(self.topBtns, command=self.importarLaudo, text="Importar Laudo")
        self.btimportar.grid(row=0, column=1, sticky="ne")

        self.btnexportar = CTkButton(self.topBtns, command=self.abrirLaudo, text="Compartilhar")
        self.btnexportar.grid(row=0, column=3, sticky="ne", padx=5)

        self.tree = GridView(self.tabview.tab("Laudos"), columns=["laudo"], headings=["laudo"], data=self.getLaudos())
        self.tree.grid(
            row=2,
            column=0,
            sticky="nsew",
        )
        self.tree.configure(fg_color="transparent")
        self.frBotoes = CTkFrame(self.tabview.tab("Laudos"))
        self.frBotoes.grid(row=3, column=0, sticky="nw")

        self.btnNovoLaudo = CTkButton(self.frBotoes, command=self.novoLaudo, text="Novo Laudo")
        self.btnNovoLaudo.grid(row=0, column=0, sticky="nw")
        self.btnAbrirLaudo = CTkButton(self.frBotoes, command=self.abrirLaudo, text="Abrir Laudo")
        self.btnAbrirLaudo.grid(row=0, column=1, sticky="nw")

    def getDados(self):
        return self.controller.getById(self.id)

    def getLaudos(self):
        return self.controller.getLaudos(self.dados)

    def novoLaudo(self):
        timestamp = str(datetime.datetime.now()).replace(" ", "").replace(":", "-").replace(".", "")
        name = self.nome.replace(" ","-")
        filename = f"{name}{timestamp}.docx"
        novoLaudoPath = Path(os.path.join(self.caminho, filename))
        openFile(novoLaudoPath)
        self.tree.state.redefineState(self.getLaudos())
        self.tree.showGrid()

    def abrirLaudo(self):
        item = self.tree.getSelecionado()
        arquivo = f"{item[0]}.docx"
        abrir = Path(os.path.join(self.caminho, arquivo))
        openFile(abrir)

    def importarLaudo(self):
        dialog = askopenfilename(filetypes=[("Docs", ["*.docx", "*.doc", "*.odt"])], title="Selecione um laudo para importar")
        shutil.copy(dialog, self.caminho)
        self.tree.state.redefineState(self.getLaudos())
        self.tree.showGrid()
