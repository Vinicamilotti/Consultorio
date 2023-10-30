import os
import sqlite3
from pathlib import Path


class DBModule:
    def __init__(self):
        self.path = Path(os.path.join(os.getcwd(), "Data", "DB", "consultorio.db"))
        sqlite3.connect(self.path)
        self.db = sqlite3.connect(self.path.absolute())
        self.cursor = self.db.cursor()

    def createTables(self, tables: list[str]):
        for table in tables:
            qry = table
            self.db.cursor().execute(qry)
            self.db.commit()


    def closeConnection(self):
        self.db.close()
