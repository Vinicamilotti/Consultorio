from ....Views import Heranca
from customtkinter import *
from src.controllers.pacientesController import PacientesController
from ....Views.Components.formInput import InputForm
from src.Models.Pacientes import Paciente

class FormCadastro(Heranca):
    def __init__(self, master: any):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.nome = InputForm(self, "Nome do Paciente")
        self.nome.grid(row=0, column=0)
        self.cpf = InputForm(self, "CPF do Paciente")
        self.cpf.grid(row=1, column=0)
        self.celConteiner = CTkFrame(self)
        self.celConteiner.configure(fg_color="transparent"
                                             "")
        self.celConteiner.grid(row=2, column=0)
        self.ddd = InputForm(self.celConteiner, "DDD", 50)
        self.ddd.grid(row=0, column=0)
        self.contato = InputForm(self.celConteiner, "Celular", 250)
        self.contato.grid(row=0, column=1)
        self.email = InputForm(self, "Email")
        self.email.grid(row=3, column=0)
        self.tp = CTkSwitch(self, text="Cirança ou adulto")
        self.tp.grid(row=4, column=0)
        self.botaoCadastro = CTkButton(self, text="Cadastrar", command=self.cadastrar)
        self.botaoCadastro.grid(row=4, column=0, pady=20)


    def cadastrar(self):
        nome = self.nome.getValue()
        cpf = self.cpf.getValue()
        contato = f"55{self.ddd.getValue()}{self.contato.getValue()}"
        email = self.email.getValue()
        paciente = Paciente(nome=nome, cpf=cpf, contato=contato, email=email, tp=1)
        controller = PacientesController()

        controller.novoPaciente(paciente)
        self.master.destroy()
