from dimanify import *

def вывод(текст):
  print(str(текст))

class текст:
  def __init__(self, text):
    self.text = str(text)
    
  def вывести(self):
    вывод(self.text)
    return self.text
    
  def капс(self):
    self.text = self.text.upper()
    return self.text
    
  def низ(self):
    self.text = self.text.lower()
    return self.text
    
  def спросить(self):
    return input(self.text)
    
  def вернуть(self):
    return self.text
    
  def __str__(self):
    return self.text