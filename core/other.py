from dimanify import *


def диапазон(число):
    if not isinstance(число, int):
        raise TypeError("Число должно быть целым числом")
    return [i for i in range(число)]

def считать(что):
    if not isinstance(что, (list, str)):
        raise TypeError("Аргумент должен быть списком или строкой")
    return len(что)
