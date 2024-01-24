from suprema.biostar2 import *

class DoorGroup(AbstractEndpoint):
    collection = 'DoorGroupCollection'
    endpoint = 'api/door_groups'

    def create(self, parent_id, depth, name):
        return super().create(
            data={
                "DoorGroup": {
                    "parent_id": {
                        "id": parent_id
                    },
                    "depth": {depth},
                    "name": name
                }
            }
        )
    
    def get_all(self, params=''):
        data = self.biostar2.post(
            f'{self.endpoint}/search',
            headers=self.init_headers()
        )
        if data.get(self.collection):
            return data.get(self.collection).get('rows')
        else:
            return None
    
    def get(self, door_group, params=''):
        return super().get(door_group, params)

    def delete(self, door_group):
        if not isinstance(door_group, dict):
            door_group = self.get(door_group)

        return super().delete(door_group)
    
    def update(self, door_group, name=None, parent_id=None):
        data = {
            "DoorGroup": {}
        }
        if name is not None:
            data["DoorGroup"]["name"] = name
        if parent_id is not None:
            data["DoorGroup"]["parent_id"] = {"id": parent_id}
        return super().update(door_group, data=data)