import sqlite3
import pathlib
import os


def connection() -> sqlite3.Connection:
    path = pathlib.Path(os.path.join(os.getcwd(), "Data", "DB", "consultorio.db"))
    con = sqlite3.connect(path)
    return con
