import requests
import json

class api_call(object):
    def __init__(self, key, url):
        self.key = key
        self.url = url

    def call(self, keyvar, **kwargs):
        params = {}
        params[keyvar] = self.key
    
        for key in kwargs.keys():
            params[key] = kwargs[key]
    
        r = requests.get(self.url, params=params)
        results = json.loads(r.text)
        return results


