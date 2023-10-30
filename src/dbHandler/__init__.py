from .tableList import tableList
from .dbModule import DBModule
import os
from pathlib import Path

appPath = os.path.join(os.getcwd())
DataFolder = Path(os.path.join(appPath, "Data"))
DBFolder = Path(os.path.join(DataFolder.absolute(), "DB"))
PacienteFolder = Path(os.path.join(DataFolder.absolute(), "Pacientes"))
AtividadesFolder = Path(os.path.join(DataFolder.absolute(), "Atividades"))

def createDataDirectory():
    DBFolder.mkdir(exist_ok=True, parents=True)
    PacienteFolder.mkdir(exist_ok=True, parents=True)
    AtividadesFolder.mkdir(exist_ok=True, parents=True)

def VerificarPastas(db:DBModule):
    listaPacientes = db.cursor.execute("SELECT NOME_COMPLETO FROM PACIENTES").fetchall()
    for paciente in listaPacientes:
        pacientePath = Path(os.path.join(DataFolder, PacienteFolder, str(paciente[0]), "Laudos"))
        pacientePath.mkdir(exist_ok=True, parents=True)


createDataDirectory()
db = DBModule()
db.createTables(tableList())
VerificarPastas(db)
db.closeConnection()
