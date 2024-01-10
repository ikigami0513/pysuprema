from suprema.biostar2 import *

class AccessGroup(AbstractEndpoint):
    collection = 'AccessGroupCollection'
    endpoint = 'api/access_groups'

    def get_all(self):
        return super().get_all()
    
    def get(self, access_group_id):
        return self.biostar2.get(
            f'{self.endpoint}/{access_group_id}',
            headers={
                'bs-session-id': self.biostar2.user.session_id
            }
        )
    
    def get_users(self, access_group_id):
        return self.biostar2.get(
            f'{self.endpoint}/{access_group_id}/users',
            headers={
                'bs-session-id': self.biostar2.user.session_id
            }
        ).get('UserCollection').get('rows')
    
    def create(self, name, description=None, users=[], user_group=[], access_levels=[]):
        return super().create(
            data={
                "AccessGroup": {
                    "name": name,
                    "description": description,
                    "users": [{"user_id": id} for id in users],
                    "user_group": [{"id": id} for id in user_group],
                    "access_levels": [{"id": id} for id in access_levels]
                }
            }
        )
    
    def update(self, id, name, description=None, users=None, user_group=None, access_levels=None):
        data = {"name": name}
        if description is not None: data["description"] = description
        if users is not None: data["users"] = [{"user_id": id} for id in users]
        if user_group is not None: data["user_group"] = [{"id": id} for id in user_group]
        if access_levels is not None: data["access_levels"] = [{"id": id} for id in access_levels]

        return super().update(item=id, data=data)
    
    def delete(self, access_group_id):
        return super().delete(access_group_id)