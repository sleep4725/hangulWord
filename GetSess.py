import requests

class GetSess:
    @classmethod
    def reqObjGet(cls):
        sess = requests.Session()
        return sess