from .controller import Controller


class PacientesController(Controller):
    def __init__(self):
        super().__init__(table="PACIENTES")

    def getAll(self) -> list:
        return super().getAll()

    def getById(self, id):
        return super().select(["*"], f"WHERE ID_PACIENTE={id}")
