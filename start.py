import os
from dimanify import *
import re
import sys

путь = sys.argv[1]

код = файл(путь, "r").читать()

код = re.sub(r"использовать '(.+?)'", r"from \1 import *", код, flags=re.MULTILINE)
код = re.sub(r'^\s*переменная\s+(\w+)\s*=\s*(\w+)?,\s*(.+)$', r'\1 = переменная("\2", \3)', код, flags=re.MULTILINE)
код = re.sub(r"лямбд", "lambda", код)

exec(compile(код, '<string>', 'exec'))