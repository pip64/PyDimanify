from dimanify import *
from core.markov import *
from core.tryexcept import *
from core.conditions import *
from core.files import *
from core.variables import *
from core.texts import *
from core.randoms import *
from core.funcs import *
from core.other import *
from core.requests import *
from core.cycles import *
#from core.disetify import *
import re

class функ:
    def __init__(self, name, *args):
        if not isinstance(name, str):
            raise TypeError("Название функции должно быть строкой")
        if not all(isinstance(arg, str) for arg in args):
            raise TypeError("Аргументы должны быть строками")
        self.name = name
        self.args = args
        self.args_count = len(args)
        self.code = []

    def добавить(self, codes):
        if not isinstance(codes, (list, tuple)):
            raise TypeError("Аргумент должен быть списком или кортежом")
        for code in codes:
            self.code.append(code)

    def выполнить(self, *args):
        if self.args_count != len(args):
            raise TypeError(f"Неверное количество аргументов. Ожидалось {self.args_count}, получено {len(args)}")
        if len(self.code) == 0:
            raise ValueError("Отсутствует код функции")
        for c in self.code:
            for arg in self.args:
                c = re.sub(r"(?<!\\);{}(?!\w)".format(arg), str(args[self.args.index(arg)]), c)
            exec(c.replace(f"\;", f";"))

    def название(self):
        return self.name
