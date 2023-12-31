import tkinter as tk
from tkinter import ttk
from customtkinter import *
from src.Views.Heranca import Heranca
from src.controllers.pacientesController import PacientesController
from src.Views.Components.SearchBar import SearchBar
from src.classes.stateManager import State
from src.forms.cadastro import Cadastro
from src.forms.paciente import PacienteForm
from src.Views.Components.gridView import GridView
from tkinter.messagebox import showerror
from src.Models.Pacientes import Paciente
from src.Views.Components.Lables.titles import *

class SelecionarPaciente(Heranca):
    def __init__(self, master: any):
        super().__init__(master=master)
        self.controller = PacientesController()
        self.listaPacientes = self.buscarDados()
        self.tree = GridView(self, columns=("codigo", "nome"), headings=("codigo", "nome"), data=self.listaPacientes)
        self.tree.grid(row=1,column=0,sticky="nsew", padx=10, pady=10)
        self.buttonConteiner = CTkFrame(self)
        self.buttonConteiner.configure(fg_color="transparent")
        self.buttonConteiner.grid(column=0, row=2, sticky="nw", padx=10, pady=10)
        self.btnSelecionar = CTkButton(
           self.buttonConteiner,
           text="Selecionar",
           command=self.selecionarPaciente
        )
        self.btnSelecionar.grid(row=0, column=0, sticky="nw")
        self.btnCadastro = CTkButton(
            self.buttonConteiner,
            text="Cadastro",
            command=self.openCadastro,
        )
        self.btnCadastro.grid(row=0, column=1, sticky="nw", padx=5)

    def buscarDados(self) -> list:
        consulta = self.controller.getAll()
        cdsPacientes = []
        for paciente in consulta:
            id = paciente.id,
            nome = paciente.nome,
            pacienteTupla = (id, nome)
            cdsPacientes.append(pacienteTupla)
        return cdsPacientes
    def openCadastro(self):
        cadastro = Cadastro(self)
        cadastro.wait_window()
        self.tree.state.redefineState(self.buscarDados())
        self.tree.showGrid()

    def selecionarPaciente(self):
        item = self.tree.getSelecionado()
        if item != None:
            janela = PacienteForm(self, paciente=item[0])
        else:
            showerror("Ops", "Selecione um paciente")