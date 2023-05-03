from dimanify import *

class условие:
    def __init__(self, condition):
        self.condition = condition
        self.body_if = []
        self.body_else = []

    def если(self, codes):
        for code in codes:
            self.body_if.append(code)

    def иначе(self, codes):
        for code in codes:
            self.body_else.append(code)

    def выполнить(self):
        if self.condition():
            for c in self.body_if:
                c()
        else:
            for c in self.body_else:
                c()
