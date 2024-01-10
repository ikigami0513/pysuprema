import requests
import json
from suprema.biostar2 import *

class Authorization(AbstractEndpoint):
    def login(self, **credentials) -> Biostar2User:
        login_id = credentials.pop('login_id')
        password = credentials.pop('password')

        try:
            with requests.post(
                f'{self.biostar2.host}/api/login',
                data=json.dumps({
                    'User': {
                        'login_id': login_id,
                        'password': password
                    }
                }),
                headers={
                    'Content-Type': "application/json"
                }
            ) as response:
                response.raise_for_status()
                if response.status_code == 200:
                    session_id = response.headers.get('bs-session-id')
                    user = Biostar2User(session_id=session_id, user=response.json().get('User'))
                    return user
                
                return None

        except requests.exceptions.HTTPError as e:
            print(f"Http Error : {e}")
            return None
        
    def logout(self):
        return self.biostar2.post(
            f'api/logout/',
            headers={},
            data=json.dumps({})
        )
