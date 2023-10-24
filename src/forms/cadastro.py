import tkinter as tk
from tkinter import ttk
from dbHandler import connection


def Cadastro(master):
    window = tk.Toplevel(master)
    window.geometry("1024x768")
    title = ttk.Label(window, text="TESTE")
    title.grid(column=1, row=0)
