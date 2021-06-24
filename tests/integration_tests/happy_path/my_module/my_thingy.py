from dangle import Dungle


class MyThingy:
    def __init__(self, a: Dungle) -> None:
        self.a = a

    def do_stuff(self, b) -> str:
        return str(self.a + b)
