from . import A

class B:
    @staticmethod
    def do_other_stuff() -> int:
        return len(A.do_stuff())
