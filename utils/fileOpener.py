import subprocess, os, platform
from pathlib import Path

def openFile(path:Path):
    filepath = path.absolute()
    file = open(filepath, '+a')
    file.close()
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))