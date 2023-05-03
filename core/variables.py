from dimanify import *

class переменная:
    types = {
        "str": str,
        "int": int,
        "list": list,
        "bool": bool
    }

    def __init__(self, var_type, content):
        if var_type not in self.types:
            raise ValueError(f"Неизвестный тип переменной {var_type}")

        if not isinstance(content, self.types[var_type]):
            raise TypeError(f"Недопустимый тип {type(content).__name__} для переменной типа {var_type}")

        self.type = var_type
        self.content = content

    def присвоить(self, value):
        if not isinstance(value, self.types[self.type]):
            raise TypeError(f"Недопустимый тип {type(value).__name__} для переменной типа {self.type}")

        self.content = self.content + value
        return self.content

    def прибавить(self, value):
        if not isinstance(value, self.types[self.type]):
            raise TypeError(f"Недопустимый тип {type(value).__name__} для переменной типа {self.type}")

        if self.type == "str":
            return self.content + value
        elif self.type == "list":
            return self.content + [value]
        else:
            return self.content + value

    def уравнить(self, value):
        if not isinstance(value, self.types[self.type]):
            raise TypeError(f"Недопустимый тип {type(value).__name__} для переменной типа {self.type}")

        self.content = value
        self.type = type(value).__name__
        return self.content

    def вывести(self):
        вывод(self.content)

    def значение(self):
        return self.content

    def __str__(self):
        return str(self.content)
