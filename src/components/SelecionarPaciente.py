import tkinter as tk
from tkinter import ttk
from customtkinter import *
from .Heranca import Heranca
from ..controllers.pacientesController import PacientesController
from ..components import SearchBar
from ..classes.stateManager import State
from ..forms.cadastro import Cadastro


class SelecionarPaciente(Heranca):
    def __init__(self, master: any):
        super().__init__(master=master)
        self.controller = PacientesController()
        self.columns = ("codigo", "nome")
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")
        self.tree.propagate(True)
        self.tree.heading("codigo", text="Codigo")
        self.tree.heading("nome", text="Nome")
        self.tree.grid(
            row=1,
            column=0,
            sticky="nsew",
        )
        self.cdsPacientes = self.buscarDados()
        self.tableState = State(self.cdsPacientes)
        self.showGrid()

        self.search = SearchBar(self, 400, lambda: self.searchGrid())
        self.search.grid(column=0, row=0, sticky="nw")

        scrollbar = CTkScrollbar(self, orientation="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky="ns")
        buttonConteiner = CTkFrame(self)
        buttonConteiner.grid(column=0, row=2, sticky="nw")
        btnCadastro = CTkButton(
            buttonConteiner,
            text="Cadastro",
            command=self.openCadastro,
        )
        btnCadastro.grid(row=0, column=0, sticky="nw")
        btnTeste = CTkButton(
            buttonConteiner, text="Selecionar", command=self.selecionarPaciente
        )
        btnTeste.grid(row=0, column=1, sticky="n")

    def buscarDados(self) -> list:
        cdsPacientes = self.controller.getAll()
        return cdsPacientes

    def showGrid(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        state = self.tableState.getState()
        for dados in state:
            self.tree.insert("", tk.END, values=dados)

    def searchGrid(self):
        self.tableState.resetState()
        query = self.search.txtBox.get()
        state = self.tableState.getState()
        newState = []
        for itens in state:
            for fields in itens:
                if str(query).lower() in str(fields).lower() and fields == itens[1]:
                    newState.append(itens)
        self.tableState.setState(newState)
        self.showGrid()

    def openCadastro(self):
        cadastro = Cadastro(self)
        cadastro.wait_window()
        self.tableState.setState(self.buscarDados())
        self.showGrid()

    def selecionarPaciente(self):
        current = self.tree.focus()
        item = self.tree.item(current)
        print(item)
