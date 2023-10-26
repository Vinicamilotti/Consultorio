from ..components.Heranca import Heranca
from customtkinter import *
from ..controllers.pacientesController import PacientesController


class FormCadastro(Heranca):
    def __init__(self, master: any):
        super().__init__(master)
        self.nome = CTkEntry(self, width=300)
        self.nome.grid(row=1, column=1)
        self.botaoCadastro = CTkButton(self, text="Cadastrar", command=self.cadastrar)
        self.botaoCadastro.grid(row=1, column=2)

    def cadastrar(self):
        nome = f"'{self.nome.get()}'"
        controller = PacientesController()
        controller.insertOne(["NOME_COMPLETO", "TPADULTO"], [nome, "1"])
        self.master.destroy()
