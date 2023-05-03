import requests

class запрос:
    def __init__(self, url):
        self.url = url
        
    def гет(self, **kwargs):
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
