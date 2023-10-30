from customtkinter import *
class GenericTitle(CTkFrame):
    def __init__(self, master, text: str, size: int):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.font = CTkFont(size=size)
        self.txt = CTkLabel(self, text=text, font=self.font)
        self.txt.grid(column=0, row=0)


class Header1(GenericTitle):
    def __init__(self, master, text):
        super().__init__(master=master, text=text, size=34)


class Header2(GenericTitle):
    def __init__(self, master, text):
        super().__init__(master=master, text=text, size=30)


class Header3(GenericTitle):
    def __init__(self, master, text):
        super().__init__(master=master, text=text, size=24)


class Header4(GenericTitle):
    def __init__(self, master, text):
        super().__init__(master=master, text=text, size=20)