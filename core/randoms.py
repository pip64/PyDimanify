import random
from dimanify import *

class рандом:
  @staticmethod
  def выбор(массив):
    if not массив:
      raise ValueError("Массив не может быть пустым.")
    return random.choice(массив)

  @staticmethod
  def число(от, до):
    try:
      от = int(от)
      до = int(до)
    except ValueError:
      raise ValueError("Аргументы должны быть числами.")
    if от > до:
      raise ValueError("От должно быть меньше или равно до.")
    return random.randint(от, до)

