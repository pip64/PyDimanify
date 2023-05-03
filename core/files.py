class файл:
  def __init__(self, путь, режим):
    self.dir = путь
    self.mode = режим

  def читать(self, сколько: int = None):
    try:
        with open(self.dir, self.mode) as file:
            return file.read(сколько)
    except IOError:
        print(f"Ошибка при чтении файла {self.dir}")
        return ""
        
  def читать_строки(self):
    try:
        with open(self.dir, self.mode) as file:
            return file.readlines()
    except IOError:
        print(f"Ошибка при чтении файла {self.dir}")
        return []
    
  def записать(self, что):
    try:
        with open(self.dir, self.mode) as file:
            return file.write(str(что))
    except IOError:
        print(f"Ошибка при записи в файл {self.dir}")
        return 0
        
  def записать_строку(self, что):
    try:
        with open(self.dir, self.mode) as file:
            return file.writelines(str(что))
    except IOError:
        print(f"Ошибка при записи в файл {self.dir}")
        return 0
