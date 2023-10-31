from .controller import Controller
import os
from pathlib import Path
from ..Models.Pacientes import Paciente


class PacientesController(Controller):
    def __init__(self):
        super().__init__(table="PACIENTES")
        self.path = Path(os.path.join(os.getcwd(), "Data", "Pacientes"))

    def __montarPaciente(self, consulta: list) -> Paciente:
        id = consulta[0]
        id_responsavel = consulta[1]
        nome = consulta[2]
        contato = consulta[3]
        cpf = consulta[4]
        email = consulta[5]
        tipo = consulta[6]

        pacienteObj = Paciente(id=id, id_responsavel=id_responsavel, nome=nome, contato=contato,email=email, cpf=cpf, tp=tipo)
        return pacienteObj

    def getAll(self) -> list[Paciente]:
        consulta = super().getAll()
        pacientes = []
        for paciente in consulta:
            pacienteObj = self.__montarPaciente(paciente)
            pacientes.append(pacienteObj)
        return pacientes

    def getById(self, id: int) -> Paciente:
        paciente = super().select(["*"], f"WHERE ID_PACIENTE={id}")
        return self.__montarPaciente(paciente[0])

    def novoPaciente(self, paciente: Paciente) -> None:
        campos = ["ID_RESPONSAVEL", "NOME_COMPLETO", "CONTATO","EMAIL", "CPF", "TPADULTO"]
        valores = [paciente.id_responsavel, f"'{paciente.nome}'", f"'{paciente.contato}'",f"'{paciente.email}'" ,f"'{paciente.cpf}'",
                   paciente.tpadulto]

        super().insertOne(campos, valores)
        pasta = Path(os.path.join(self.path, paciente.nome, 'Laudos'))
        pasta.mkdir(parents=True)

    def getLaudos(self, paciente: Paciente):
        caminho = Path(os.path.join(self.path, paciente.nome, "Laudos"))
        files = os.listdir(caminho)
        nomes = []
        for file in files:
            nome = file.split(".docx")
            nomes.append(nome[0])
        return nomes
