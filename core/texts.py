from dimanify import *

def вывод(текст):
    print(str(текст))

class текст:
    def __init__(self, text):
        self.text = str(text)

    def вывести(self):
        try:
            вывод(self.text)
        except Exception as e:
            print(f"Ошибка при выводе текста: {e}")
        return self.text

    def капс(self):
        try:
            self.text = self.text.upper()
        except Exception as e:
            print(f"Ошибка при преобразовании текста в верхний регистр: {e}")
        return self.text

    def низ(self):
        try:
            self.text = self.text.lower()
        except Exception as e:
            print(f"Ошибка при преобразовании текста в нижний регистр: {e}")
        return self.text

    def спросить(self):
        try:
            return input(self.text)
        except Exception as e:
            print(f"Ошибка при получении ввода пользователя: {e}")

    def вернуть(self):
        return self.text

    def __str__(self):
        return self.text
