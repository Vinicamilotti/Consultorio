import os
from pathlib import Path
class Paciente:
    def __init__(self, nome:str, contato:str, tp:int, cpf: str | None = None, id_responsavel: int | None = None, id: int | None = None):
        self.id = id
        self.nome = nome
        self.contato = contato
        self.cpf = cpf
        self.id_responsavel = id_responsavel
        self.caminho = Path(os.path.join(os.getcwd(), "Data", "Pacientes", nome))
        self.tpadulto = tp


