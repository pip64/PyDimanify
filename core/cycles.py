from dimanify import *

class когда:
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

class для:
    def __init__(self, iterable, arg):
        self.iterable = iterable
        self.body = []
        self.arg_name = arg
        self.arg_content = None

    def добавить(self, codes):
        for code in codes:
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
