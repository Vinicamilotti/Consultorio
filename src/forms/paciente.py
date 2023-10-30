from typing import Tuple
from customtkinter import *
from ..forms.topLevel import TopLevel
from ..Views.Pages.Paciente.Paciente import PacientePage
from pathlib import Path
from src.Views.Components.Lables.titles import *


class PacienteForm(TopLevel):
    def __init__(self, *args, paciente:int, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.form = PacientePage(self, idPaciente=paciente)
        self.form.grid(row=1, column=1)
        self.title("Paciente")
