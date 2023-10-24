import tkinter as tk
from tkinter import ttk
from customtkinter import *
from .Heranca import Heranca
from ..dbHandler import connection
from ..components import SearchBar
from ..classes.stateManager import State


class SelecionarPaciente(Heranca):
    def __init__(self, master: any):
        super().__init__(master=master)

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

        self.search = SearchBar(self, 400)
        self.search.grid(column=0, row=0, sticky="nw")

        self.search.btnBuscar.bind("<<MouseClick>>", command=self.searchGrid)

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
            buttonConteiner, text="Selecionar", command=self.openCadastro
        )
        btnTeste.grid(row=0, column=1, sticky="n")

    def buscarDados(self) -> list:
        cdsPacientes = self.cursor.execute(
            "SELECT ID_PACIENTE, NOME_COMPLETO FROM PACIENTES"
        ).fetchall()
        return cdsPacientes

    def showGrid(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        state = self.tableState.getState()
        for dados in state:
            self.tree.insert("", tk.END, values=dados)

    def searchGrid(self, value: str):
        print("helo")
        query = value
        state = self.tableState.getState()
        newState = []
        for itens in state:
            for fields in itens:
                if str(query) in str(fields):
                    newState.append(itens)
        self.tableState.setState(newState)
        self.showGrid()

    def openCadastro(self):
        print("hello")
