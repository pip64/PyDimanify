import requests
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

class запрос:
    def __init__(self, url):
        self.url = url
        
    def получить(self, **kwargs):
        try:
            response = requests.get(self.url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
    
    def пост(self, данные=None, жсон=None, **kwargs):
        try:
            response = requests.post(self.url, data=данные, json=жсон, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
    
    def положить(self, данные=None, **kwargs):
        try:
            response = requests.put(self.url, data=данные, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
    
    def удалить(self, **kwargs):
        try:
            response = requests.delete(self.url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
