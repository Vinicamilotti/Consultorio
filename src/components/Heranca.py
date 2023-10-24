from typing import Optional, Tuple, Union
from customtkinter import *
from ..dbHandler import connection


class Heranca(CTkFrame):
    db = connection()
    cursor = db.cursor()

    def __init__(self, master: any):
        super().__init__(master)
