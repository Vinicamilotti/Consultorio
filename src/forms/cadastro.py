from typing import Tuple
from customtkinter import *
from ..forms.topLevel import TopLevel
from ..components.Cadastro import FormCadastro
from pathlib import Path


class Cadastro(TopLevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.form = FormCadastro(self)
        self.form.grid(row=1, column=1)
