import tkinter as tk
from tkinter import ttk
from dbHandler import connection
from .cadastro import Cadastro


def App():
    db = connection()
    cursor = db.cursor()

    cdsPacientes = cursor.execute(
        "SELECT ID_PACIENTE, NOME_COMPLETO FROM PACIENTES"
    ).fetchall()

    root = tk.Tk()
    root.title("Treeview demo")
    root.geometry("1024x768")

    root.columnconfigure([0, 1, 2], weight=1)
    root.rowconfigure([0, 1, 2], weight=1)

    title = ttk.Label(root, text="Consultório", justify="center")
    title.grid(row=0, column=1)
    # define columns

    treeConteiner = ttk.Frame(root)
    treeConteiner.grid(row=1, column=1, sticky="n", ipady=5)

    columns = ("codigo", "nome")
    tree = ttk.Treeview(treeConteiner, columns=columns, show="headings")
    tree.propagate(True)
    # define headings
    tree.heading("codigo", text="Codigo")
    tree.heading("nome", text="Nome")
    tree.grid(
        row=0,
        column=0,
        sticky="nsew",
    )

    # generate sample data

    for dados in cdsPacientes:
        tree.insert("", tk.END, values=dados)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item["values"]
            # show a message

    def openCadastro():
        Cadastro(root)

    tree.bind("<<TreeviewSelect>>", item_selected)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(treeConteiner, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    buttonConteiner = ttk.Frame(treeConteiner)
    buttonConteiner.grid(column=0, row=1, sticky="n")

    btnCadastro = ttk.Button(buttonConteiner, text="Cadastro", command=openCadastro)
    btnCadastro.grid(row=0, column=0, sticky="n")
    btnTeste = ttk.Button(buttonConteiner, text="Selecionar", command=openCadastro)
    btnTeste.grid(row=0, column=1, sticky="n")
    # run the app
    root.mainloop()
