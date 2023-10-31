from src import App
import os
from pathlib import Path
from src.dbHandler.dbModule import DBModule
from customtkinter import *
from utils.driveHandler import driveConnection


def __init__():
    service = driveConnection()
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()

    file_metadata = {
        'name': 'Consultorio',
        'mimeType': 'application/vnd.google-apps.folder'
    }

    # pylint: disable=maybe-no-member
    if not os.path.exists("folder_id"):
        folder = service.files().create(body=file_metadata, fields='id').execute()
        print(F'Folder ID: "{folder.get("id")}".')
        file = open("folder_id", '+a')
        file.write(folder.get("id"))

    app = App()
    app.mainloop()


if __name__ == "__main__":
    __init__()
