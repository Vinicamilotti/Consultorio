from typing import Tuple
from customtkinter import *
from ..forms.topLevel import TopLevel
from ..Views.Pages.Cadastro import FormCadastro
from pathlib import Path
from src.Views.Components.Lables.titles import *

class Cadastro(TopLevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.form = FormCadastro(self)
        self.form.grid(row=1, column=1)
        self.title("Novo paciente")
        self.titulo = Header2(self, "Cadastrar novo paciente")
        self.titulo.grid(row=0, column= 1)
