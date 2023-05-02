from dimanify import *
import re

class функ:
  def __init__(self, name, *args):
    self.name = name
    self.args = args
    self.args_count = len(args)
    self.code = []
    
  def добавить(self, codes):
    for code in codes:
      self.code.append(code)
      
  def выполнить(self, *args):
    if len(self.code) > 0:
      if self.args_count == len(args):
        for c in self.code:
          for arg in self.args:
            c = re.sub(r"(?<!\\);{}(?!\w)".format(re.escape(arg)), str(args[self.args.index(arg)]), c)
          exec(c.replace(f"\;", f";"))
      else:
        текст("Argument Error").вывести()
        
  def название(self):
    return self.name