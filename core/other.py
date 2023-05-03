from dimanify import *
from core.markov import *
from core.tryexcept import *
from core.conditions import *
from core.files import *
from core.variables import *
from core.texts import *
from core.randoms import *
from core.funcs import *
from core.other import *
from core.requests import *
from core.cycles import *
#from core.disetify import *


def диапазон(число):
    if not isinstance(число, int):
        raise TypeError("Число должно быть целым числом")
    return range(число)


def считать(что):
    if not isinstance(что, (list, str)):
        raise TypeError("Аргумент должен быть списком или строкой")
    return len(что)
