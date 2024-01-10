import json
from suprema.biostar2 import *

class AbstractEndpoint:
    collection: str = None
    endpoint: str = None

    def __init__(self, biostar2):
        self.biostar2 = biostar2

    def get_all(self, params=''):
        data = self.biostar2.get(
            f'{self.endpoint}?{params}',
            headers={
                'bs-session-id': self.biostar2.user.session_id
            }
        )
        return data.get(self.collection).get('rows')
    
    def get(self, item, params=''):
        queryset = self.get_all(params)
        for query in queryset:
            if query.get('id') == str(item) or query.get('name') == item:
                return query
            
        return None
    
    def create(self, data):
        return self.biostar2.post(
            self.endpoint,
            headers={
                'bs-session-id': self.biostar2.user.session_id
            },
            data=json.dumps(data)
        )
    
    def update(self, item, data):
        if not isinstance(item, dict):
            item = self.get(item)

        return self.biostar2.put(
            f'{self.endpoint}/{item.get("id")}',
            headers={
                'bs-session-id'
            },
            data=json.dumps(data)
        )
    
    def delete(self, item):
        if not isinstance(item, dict):
            item = self.get(item)

        return self.biostar2.delete(
            f'{self.endpoint}?id={item.get("id")}',
            headers={
                'bs-session-id': self.biostar2.user.session_id
            }
        )