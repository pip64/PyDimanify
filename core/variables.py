from dimanify import *

class переменная:
  types = {
      "str": str,
      "int": int,
      "list": list,
      "bool": bool
  }
  
  def __init__(self, var_type, content):
    self.type = var_type
    self.content = content
    if not isinstance(self.content, self.types[self.type]):
        self.content = False
        self.type = "bool"
        print("Type Error")
      
  def присвоить(self, value):
    if isinstance(value, self.types[self.type]):
        self.content = self.content + 1
        return self.content
    else:
        print("Type Error")
        return None
      
  def прибавить(self, value):
      if isinstance(value, self.types[self.type]):
        return self.content + value
        
  def уравнить(self, value):
    if isinstance(value, self.types[self.type]):
        self.content = value
        self.type = type(value).__name__
        return self.content
    else:
        print("Type Error")
        return None
    
  def вывести(self):
    вывод(self.content)

  def значение(self):
    return self.content
    
  def __str__(self):
    return str(self.content)