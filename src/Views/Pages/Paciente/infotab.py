import os
import shutil
import datetime
from pathlib import Path
from customtkinter import *
from tkinter.simpledialog import Dialog
from tkinter.ttk import Label
from utils.fileOpener import openFile
from src.Views import Heranca
from src.Views.Components.gridView import GridView
from src.controllers.pacientesController import PacientesController
from src.Views.Components.Lables.titles import *
from src.Models.Pacientes import Paciente
from utils.whatsappHandler import Whatsapp

class InfoTab(Heranca):
    def __init__(self, master, paciente:Paciente):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.paciente = paciente
        self.infoTopLeft = CTkFrame(self)
        self.infoTopLeft.grid(column=0, row=0, pady=10, padx=10, sticky='nsew')
        self.nome = CTkLabel(self.infoTopLeft, text=f"Nome: {self.paciente.nome}")
        self.nome.grid(column=0, row=0)
        self.infoTopRight = CTkFrame(self)
        self.infoTopRight.grid(column=1, row=0, pady=10, padx=10, sticky='nsew')
        self.cpf = CTkLabel(self.infoTopRight, text=f"CPF: {self.paciente.cpf}")
        self.cpf.grid(column=0, row=0)
        self.infoBottomLeft = CTkFrame(self)
        self.infoBottomLeft.grid(column=0, row=2, pady=10, padx=10, sticky='nsew')
        self.contato = CTkLabel(self.infoBottomLeft, text=f"Celular: {self.paciente.contato}")
        self.contato.configure(cursor='hand2')
        self.contato.grid(column=0, row=0)
        self.contato.bind('<Button-1>', self.contatoClick)
        self.infoBottomRight = CTkFrame(self)
        self.infoBottomRight.grid(column=1, row=2, pady=10, padx=10, sticky='nsew')
        self.email = CTkLabel(self.infoBottomRight, text=f"Email: {self.paciente.email}")
        self.email.configure(cursor='hand2')
        self.email.grid(column=0, row=0)


    def contatoClick(self, event):
        whatsapp = Whatsapp()
        whatsapp.openchat(self.paciente.contato)
