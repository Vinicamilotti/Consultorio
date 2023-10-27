from src.Views.Heranca import Heranca
from customtkinter import *


class SearchBar(Heranca):
    def __init__(self, master: any, w: int, searchFunc):
        super().__init__(master)
        self.txtBox = CTkEntry(
            master=self,
            placeholder_text="Procurar",
            width=w,
            height=25,
            border_width=2,
            corner_radius=10,
        )
        self.searchFunc = searchFunc
        self.txtBox.grid(column=0, row=0, sticky="sw")
        self.btnBuscar = CTkButton(self, text="Buscar", command=self.searchGrid)
        self.btnBuscar.grid(column=1, row=0, sticky="se")

    def searchGrid(self) -> list:
        self.searchFunc()
