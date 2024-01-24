from suprema.biostar2 import *

class User(AbstractEndpoint):
    collection = 'UserCollection'
    endpoint = 'api/users'

    def get_all(self, group_id, limit=0, offset=0, order_by_user_id='false', last_modified=0):
        params = f'group_id={group_id}&limit={limit}&offset={offset}&order_by=user_id:{order_by_user_id}&last_modified={last_modified}'
        return super().get_all(params=params)
    
    def get(self, user_id):
        return self.biostar2.get(
            f'{self.endpoint}/{user_id}',
            headers=self.init_headers,
        )

    def create(self, user_id, user_group_id, start_datetime, expiry_datetime, **kwargs):
        return super().create(
            data={
                "User": {
                    "user_id": user_id,
                    "user_group_id": {
                        "id": user_group_id
                    },
                    "start_datetime": start_datetime,
                    "expiry_datetime": expiry_datetime,
                    **kwargs
                }
            }
        )
    
    def delete(self, id):
        if isinstance(id, list):
            params = ''
            for each in id:
                params += f'{each}+'
            id = params[:-1]

        return self.biostar2.delete(
            f'{self.endpoint}?id={id}',
            headers=self.init_headers()
        )
    
    def attribute_card(self, user_id, card_id):
        return self.biostar2.put(
            f'{self.endpoint}/{user_id}',
            headers=self.init_headers(),
            data={
                "User": {
                    "cards": card_id
                }
            }
        )
    
    def update(self, user_id, **kwargs):
        return self.biostar2.put(
            f'{self.endpoint}/{user_id}',
            headers=self.init_headers,
            data={
                "User": {
                    **kwargs
                }
            }
        )