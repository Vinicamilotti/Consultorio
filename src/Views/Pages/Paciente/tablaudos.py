import os
import shutil
import datetime
from pathlib import Path
from customtkinter import *
from tkinter.filedialog import askopenfilename
from utils.fileOpener import openFile
from src.Views import Heranca
from src.Views.Components.gridView import GridView
from src.controllers.pacientesController import PacientesController
from src.Views.Components.Lables.titles import *
from src.Models.Pacientes import Paciente
from utils.driveHandler import driveConnection
from utils.whatsappHandler import Whatsapp
from googleapiclient.http import MediaFileUpload
from src.forms.topLevel import TopLevel

class TabLaudos(Heranca):
    def __init__(self, master, paciente: Paciente):
        super().__init__(master)
        self.dados = paciente
        self.nome = self.dados.nome
        self.controller = PacientesController()
        self.topBtns = CTkFrame(self)
        self.topBtns.grid(column=0, row=1, sticky="wn")
        self.btimportar = CTkButton(self.topBtns, command=self.importarLaudo, text="Importar Laudo")
        self.btimportar.grid(row=0, column=1, sticky="ne")

        self.btnexportar = CTkButton(self.topBtns, command=self.compartilharLaudo, text="Compartilhar")
        self.btnexportar.grid(row=0, column=3, sticky="ne", padx=5)

        self.tree = GridView(self, columns=["laudo"], headings=["laudo"], data=self.getLaudos())
        self.tree.grid(
            row=2,
            column=0,
            sticky="nsew",
        )
        self.tree.configure(fg_color="transparent")
        self.frBotoes = CTkFrame(self)
        self.frBotoes.grid(row=3, column=0, sticky="nw")

        self.btnNovoLaudo = CTkButton(self.frBotoes, command=self.novoLaudo, text="Novo Laudo")
        self.btnNovoLaudo.grid(row=0, column=0, sticky="nw")
        self.btnAbrirLaudo = CTkButton(self.frBotoes, command=self.abrirLaudo, text="Abrir Laudo")
        self.btnAbrirLaudo.grid(row=0, column=1, sticky="nw")

    def getLaudos(self):
        return self.controller.getLaudos(self.dados)

    def novoLaudo(self):
        timestamp = str(datetime.datetime.now()).replace(" ", "").replace(":", "-").replace(".", "")
        name = self.dados.nome.replace(" ", "-")
        filename = f"{name}{timestamp}.docx"
        novoLaudoPath = Path(os.path.join(self.dados.caminho, "Laudos", filename))
        openFile(novoLaudoPath)
        self.tree.state.redefineState(self.getLaudos())
        self.tree.showGrid()

    def abrirLaudo(self):
        item = self.tree.getSelecionado()
        arquivo = f"{item[0]}.docx"
        abrir = Path(os.path.join(self.dados.caminho,"Laudos", arquivo))
        openFile(abrir)

    def importarLaudo(self):
        dialog = askopenfilename(filetypes=[("Docs", ["*.docx", "*.doc", "*.odt"])],
                                 title="Selecione um laudo para importar")
        caminho = Path(os.path.join(self.dados.caminho, "Laudos"))
        shutil.copy(dialog, caminho)
        self.tree.state.redefineState(self.getLaudos())
        self.tree.showGrid()

    def compartilharLaudo(self):
        item = self.tree.getSelecionado()
        arquivo = f"{item[0]}.docx"
        abrir = Path(os.path.join(self.dados.caminho,"Laudos", arquivo))
        folder_id = open('folder_id').read()
        service = driveConnection()
        file_metadata = {
            'name': arquivo,
            'parents':[folder_id],
            'type':'anyone',
            'role':'writer',
        }
        media = MediaFileUpload(abrir, mimetype='text/plain', resumable=True)
        file = service.files().create(body=file_metadata, media_body=media).execute()
        body = {'role':'writer', 'type':'anyone'}
        service.permissions().create(fileId=file.get('id'),body=body, fields='files(id, name, parents, webViewLink)')
        result = f"https://docs.google.com/file/d/{file.get('id')}/"
        whatsapp = Whatsapp()
        msg = f"Segue o laudo: {result}"
        whatsapp.sendmessage(self.dados.contato, msg)
