from ....Views import Heranca
from customtkinter import *
from src.controllers.pacientesController import PacientesController
from ....Views.Components.formInput import InputForm

class FormCadastro(Heranca):
    def __init__(self, master: any):
        super().__init__(master)
        self.nome = InputForm(self, "Nome do Paciente")
        self.nome.grid(row=0, column=0)
        self.botaoCadastro = CTkButton(self, text="Cadastrar", command=self.cadastrar)
        self.botaoCadastro.grid(row=2, column=0)

    def cadastrar(self):
        nome = f"'{self.nome.getValue()}'"
        controller = PacientesController()
        controller.insertOne(["NOME_COMPLETO", "TPADULTO"], [nome, "1"])
        self.master.destroy()
