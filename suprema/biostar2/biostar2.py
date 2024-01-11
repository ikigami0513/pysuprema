import requests
from typing import Dict, Type
from suprema.biostar2 import *


class Biostar2:
    server_ip: str = None
    port: int = None
    host: str = None
    user: Biostar2User = None

    __endpoint: Dict[Type, AbstractEndpoint] = None

    def __init__(self, **kwargs):
        self.server_ip = kwargs.pop('server_ip')
        self.port = kwargs.pop('port', None)
        self.host = f'{self.server_ip}:{self.port}' if self.port is not None else f"{self.server_ip}"

        self.__endpoint = {
            Authorization: Authorization(self),
            UserGroup: UserGroup(self),
            AccessLevel: AccessLevel(self),
            AccessGroup: AccessGroup(self),
            Card: Card(self)
        }

        login_id = kwargs.pop('login_id', None)
        password = kwargs.pop('password', None)
        if login_id is not None and password is not None:
            self.user = self.endpoint(Authorization).login(login_id=login_id, password=password)

    def endpoint(self, type: Type) -> AbstractEndpoint:
        return self.__endpoint.get(type)
        
    def get(self, endpoint, headers={}, params=None):
        with requests.get(f"{self.host}/{endpoint}", headers=headers, params=params) as response:
            return response.json()

    def post(self, endpoint, headers={}, data={}):
        with requests.post(f"{self.host}/{endpoint}", headers=headers, data=data) as response:
            return response.json()
        
    def put(self, endpoint, headers={}, data={}):
        with requests.put(f"{self.host}/{endpoint}", headers=headers, data=data) as response:
            return response.json()
        
    def delete(self, endpoint, headers={}, data={}):
        with requests.delete(f"{self.host}/{endpoint}", headers=headers, data=data) as response:
            return response.json()
        