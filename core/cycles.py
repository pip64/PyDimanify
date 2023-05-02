from dimanify import *

class цикл:
    def __init__(self, condition):
        self.condition = condition
        self.body = []

    def добавить(self, codes):
      for code in codes:
        self.body.append(code)

    def выполнить(self):
        while self.condition():
            for c in self.body:
                c()