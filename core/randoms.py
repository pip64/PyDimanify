import random
from dimanify import *

class рандом:
  @staticmethod
  def выбор(массив):
    return random.choice(массив)

  @staticmethod
  def число(от, до):
    return random.randint(int(от), int(до))