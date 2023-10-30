from typing import Optional, Tuple, Union
from customtkinter import *


class TopLevel(CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.geometry("1024x768")
        self.open = True
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)