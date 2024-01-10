from suprema.biostar2 import *

class AccessLevel(AbstractEndpoint):
    collection = 'AccessLevelCollection'
    endpoint = 'api/access_levels'

    def get_all(self, limit=50, offset=0, order_by_id=False):
        return super().get_all(params=f'limit={limit}&offset={offset}&order_by=id:{order_by_id}')
    
    def get(self, access_level):
        return super().get(item=access_level, params='limit=0&offset=0&order_by=id:True')
    
    def create(self, name, description=None, access_level_items=None):
        return super().create(
            data={
                "AccessLevel": {
                    "name": name,
                    "description": description,
                    "access_level_items": access_level_items
                }
            }
        )
    
    def update(self, access_level, name=None, description=None, access_level_items=None):
        if not isinstance(access_level, dict):
            access_level = self.get(access_level)

        return super().update(
            access_level,
            data={
                "AccessLevel": {
                    "name": name if name is not None else access_level.get('name'),
                    "description": description if description is not None else access_level.get('description'),
                    "access_level_items": access_level_items if access_level_items is not None else access_level.get('access_level_items')
                }
            }
        )
    
    def delete(self, access_level):
        return super().delete(access_level)
