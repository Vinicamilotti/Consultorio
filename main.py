from src import App
import os
from pathlib import Path


def createDataDirectory(appPath: str):
    FolderStruct: list[Path] = []
    DataFolder = Path(os.path.join(appPath, "Data"))
    DBFolder = Path(os.path.join(DataFolder.absolute(), "DB"))
    PacienteFolder = Path(os.path.join(DataFolder.absolute(), "Pacientes"))
    AtividadesFolder = Path(os.path.join(DataFolder.absolute(), "Atividades"))

    FolderStruct.append(DataFolder)
    FolderStruct.append(DBFolder)
    FolderStruct.append(PacienteFolder)
    FolderStruct.append(AtividadesFolder)

    for Folder in FolderStruct:
        Folder.mkdir(exist_ok=True)


def __init__():
    appPath = os.path.join(os.getcwd())
    createDataDirectory(appPath)
    app = App(appPath)
    app.mainloop()


if __name__ == "__main__":
    __init__()
