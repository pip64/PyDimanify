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

class условие:
    def __init__(self, condition):
        if not callable(condition):
            raise TypeError("condition должно быть callable")
        self.condition = condition
        self.body_if = []
        self.body_else = []

    def если(self, codes):
        if not isinstance(codes, list):
            raise TypeError("codes должен быть списком")
        for code in codes:
            if not callable(code):
                raise TypeError("все элементы codes должны быть callable")
            self.body_if.append(code)

    def иначе(self, codes):
        if not isinstance(codes, list):
            raise TypeError("codes должен быть списком")
        for code in codes:
            if not callable(code):
                raise TypeError("все элементы codes должны быть callable")
            self.body_else.append(code)

    def выполнить(self):
        try:
            if self.condition():
                for c in self.body_if:
                    c()
            else:
                for c in self.body_else:
                    c()
        except Exception as e:
            текст(str(e)).вывести()