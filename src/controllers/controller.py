from ..dbHandler.dbModule import DBModule


class Controller:
    def __init__(self, table: str):
        self.table = table
        self.conn = DBModule()
        self.db = self.conn.db
        self.cursor = self.conn.cursor

    def getAll(self) -> list:
        cdsBuscar = self.cursor.execute(f"SELECT * FROM {self.table}").fetchall()
        return cdsBuscar

    def select(
        self, campos: list[str], where: str | None = None, join: str | None = None
    ) -> list:
        qry = f"SELECT {','.join(campos)} FROM {self.table}"
        if join != None:
            qry = f"{qry} {join}"
        if where != None:
            qry = f"{qry} {where}"
        cdsBuscar = self.cursor.execute(qry).fetchall()
        return cdsBuscar

    def insertOne(self, campos: list[str], valores: list[str]):
        if len(campos) != len(valores):
            raise Exception("Numero de campos diferente do numero de valores")
        try:
            qry = f"INSERT INTO {self.table}({','.join(campos)}) VALUES ({','.join(valores)})"
            self.cursor.execute(qry)
            self.db.commit()
        except self.db.Error as er:
            print("SQLite error: %s" % (" ".join(er.args)))
            print("Exception class is: ", er.__class__)

    def update(self, setStr: str, where: str | None = None):
        try:
            qry = f"UPDATE {self.table} SET {setStr}"
            if where != None:
                qry = f"{qry} {where}"
            self.cursor.execute(qry)
            self.db.commit()
        except self.db.Error as er:
            print("SQLite error: %s" % (" ".join(er.args)))
            print("Exception class is: ", er.__class__)

    def delete(self, setStr: str, where: str | None = None):
        try:
            qry = f"DELETE FROM {self.table}"
            if where != None:
                qry = f"{qry} {where}"
            self.cursor.execute(qry)
            self.db.commit()
        except self.db.Error as er:
            print("SQLite error: %s" % (" ".join(er.args)))
            print("Exception class is: ", er.__class__)
