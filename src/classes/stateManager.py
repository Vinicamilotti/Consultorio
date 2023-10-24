class State:
    def __init__(self, initSate: list | str | int | bool) -> None:
        self.initialState = initSate
        self.state = initSate

    def setState(self, newState: list | str | int | bool) -> None:
        self.state = newState

    def getState(self) -> list | str | int | bool:
        return self.state

    def resetState(self) -> None:
        self.setState(self.initialState)
