from dimanify import *


class попытка:
    def __init__(self, try_block):
      self.try_block = [code for code in try_block]
      self.except_block = []
      self.finally_block = []
    
    def выполнить(self):
        try:
          for code in self.try_block:
            code()
        except Exception as e:
          for code in self.except_block:
            code()
        finally:
          for code in self.finally_block:
            code()

    def добавить_кроме(self, codes):
      for code in codes:
        self.except_block.append(code)
    
    def добавить_окончательно(self, codes):
      for code in codes:
        self.finally_block.append(code)
