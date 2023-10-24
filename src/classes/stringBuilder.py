class StringBuilder:
    def __init__(self):
        self.stringList = []
    def append(self,string:str) -> None:
        self.stringList.append(string.strip())
    def toString(self) -> str:
        string = ' '.join(self.stringList)
        return string
    def clear(self) -> None:
        self.stringList = [];
