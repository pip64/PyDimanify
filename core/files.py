from dimanify import *

class файл:
  def __init__(self, путь, режим):
    self.dir = путь
    self.mode = режим

  def читать(self, сколько: int = None):
    file = open(self.dir, self.mode)
    return file.read(сколько)
    file.close()
  def читать_строки(self):
    file = open(self.dir, self.mode)
    return file.readlines()
    file.close()
  def записать(self, что):
    file = open(self.dir, self.mode)
    return file.write(str(что))
    file.close()
  def записать_строку(self, что):
    file = open(self.dir, self.mode)
    return file.writelines(str(что))
    file.close()
