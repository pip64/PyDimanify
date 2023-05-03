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

class когда:
    def __init__(self, condition):
        if not callable(condition):
            raise TypeError("Условие должно быть функцией")
        self.condition = condition
        self.body = []

    def добавить(self, codes):
        if not isinstance(codes, (list, tuple)):
            raise TypeError("Тело должно быть списком или кортежом")
        for code in codes:
            if not callable(code):
                raise TypeError("Тело должно состоять из функций")
            self.body.append(code)

    def выполнить(self):
        while self.condition():
            for c in self.body:
                c()


class для:
    def __init__(self, iterable, arg):
        if not isinstance(iterable, (list, tuple)):
            raise TypeError("Итерируемый объект должен быть списком или кортежом")
        if not isinstance(arg, str):
            raise TypeError("Название аргумента должно быть строкой")
        self.iterable = iterable
        self.body = []
        self.arg_name = arg
        self.arg_content = None

    def добавить(self, codes):
        if not isinstance(codes, (list, tuple)):
            raise TypeError("Тело должно быть списком или кортежом")
        for code in codes:
            if not callable(code):
                raise TypeError("Тело должно состоять из функций")
            self.body.append(code)

    def вернуть_аргумент(self):
        return self.arg_content

    def вернуть_название_аргумента(self):
        return self.arg_name

    def выполнить(self):
        for i in self.iterable:
            self.arg_content = i
            for c in self.body:
                c()