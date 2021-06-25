import this
import bla


class A:
    @staticmethod
    def do_stuff() -> str:
        x = bla.bla()


class B:
    @staticmethod
    def do_other_stuff() -> int:
        return len(A.do_stuff())


class C(A):
    def do_this(self):
        return this
