import requests

class запрос:
    def __init__(self):
        pass
    
    def гет(self, url, **kwargs):
        response = requests.get(url, **kwargs)
        return response
    
    def пост(self, url, data=None, json=None, **kwargs):
        response = requests.post(url, data=data, json=json, **kwargs)
        return response
    
    def положить(self, url, data=None, **kwargs):
        response = requests.put(url, data=data, **kwargs)
        return response
    
    def удалить(self, url, **kwargs):
        response = requests.delete(url, **kwargs)
        return response