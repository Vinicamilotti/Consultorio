from .controller import Controller
import os
from pathlib import Path


class PacientesController(Controller):
    def __init__(self):
        super().__init__(table="PACIENTES")
        self.path = Path(os.path.join(os.getcwd(), "Data", "Pacientes"))

    def getAll(self) -> list:
        return super().getAll()

    def getById(self, id):
        return super().select(["*"], f"WHERE ID_PACIENTE={id}")

    def insertOne(self, campos: list[str], valores: list[str]):
        super().insertOne(campos, valores)
        nome = str(valores[0])
        gravar = nome[1:len(nome) - 1]
        pasta = Path(os.path.join(self.path, gravar, 'Laudos'))
        pasta.mkdir(parents=True)

    def getLaudos(self, caminho:Path):
        files = os.listdir(caminho)
        nomes = []
        for file in files:
            nome = file.split(".docx")
            nomes.append(nome[0])
        return nomes
