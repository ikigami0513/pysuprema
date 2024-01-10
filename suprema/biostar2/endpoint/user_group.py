from suprema.biostar2 import *

class UserGroup(AbstractEndpoint):
    collection = 'UserGroupCollection'
    endpoint = 'api/user_groups'

    def get_all(self, params=''):
        return super().get_all()
    
    def get(self, user_group, params=''):
        return super().get(user_group, params)

    def create(self, ug_name:str, parent_id:int=1, depth:int=None):
        return super().create(
            data={
                "UserGroup": {
                    "parent_id": {
                        "id": parent_id
                    },
                    "name": ug_name,
                    "depth": depth
                }
            }
        )
    
    def update(self, user_group, ug_new_name):
        if not isinstance(user_group, dict):
            user_group = self.get(user_group)
        
        return self.biostar2.put(
            user_group,
            data={
                "UserGroup": {
                    "name": ug_new_name
                }
            }
        )
    
    def delete(self, user_group):
        return super().delete(user_group)
