from src import App
import os
from pathlib import Path
from src.dbHandler.dbModule import DBModule

appPath = os.path.join(os.getcwd())
DataFolder = Path(os.path.join(appPath, "Data"))
DBFolder = Path(os.path.join(DataFolder.absolute(), "DB"))
PacienteFolder = Path(os.path.join(DataFolder.absolute(), "Pacientes"))
AtividadesFolder = Path(os.path.join(DataFolder.absolute(), "Atividades"))
FolderStruct: list[Path] = []
FolderStruct.append(DataFolder)
FolderStruct.append(DBFolder)
FolderStruct.append(PacienteFolder)
FolderStruct.append(AtividadesFolder)


def createDataDirectory():
    for Folder in FolderStruct:
        Folder.mkdir(exist_ok=True)


def VerificarPastas():
    db = DBModule()
    listaPacientes = db.cursor.execute("SELECT NOME_COMPLETO FROM PACIENTES").fetchall()
    for paciente in listaPacientes:
        pacientePath = Path(os.path.join(DataFolder, PacienteFolder, str(paciente[0]), "Laudos"))
        pacientePath.mkdir(exist_ok=True, parents=True)


def __init__():
    createDataDirectory()
    VerificarPastas()
    app = App(appPath)
    app.mainloop()


if __name__ == "__main__":
    __init__()
