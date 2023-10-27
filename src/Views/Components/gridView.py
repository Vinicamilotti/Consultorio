from customtkinter import *
from tkinter.ttk import Treeview
from src.Views.Components.SearchBar import SearchBar
from src.Views.Heranca import Heranca
import tkinter as tk
from src.classes.stateManager import State

class GridView(Heranca):
    def __init__(self, master: any, data:list, columns:list[str], headings:list[str]):
        super().__init__(master)
        self.state = State(data)
        self.table = Treeview(self, columns=columns, show="headings")
        for head in headings:
            self.table.heading(head, text=head.capitalize())
        self.table.grid(column=0, row=0)
        self.showGrid()
        self.search = SearchBar(self, 400, lambda: self.searchGrid())
        self.search.grid(column=0, row=0, sticky="nw")

        self.scrollbar = CTkScrollbar(self, orientation="vertical", command=self.tree.yview)
        self.table.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=2, sticky="ns")
    def showGrid(self):
        for i in self.table.get_children():
            self.table.delete(i)

        state = self.state.getState()
        for dados in state:
            self.table.insert("", tk.END, values=dados)