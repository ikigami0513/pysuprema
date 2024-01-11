import json
from suprema.biostar2 import *

class Card(AbstractEndpoint):
    collection = "CardCollection"
    endpoint = "api/cards"

    def get_card_types(self):
        data = self.biostar2.get(
            f'{self.endpoint}/types',
            self.init_headers()
        )

        return data.get('CardTypeCollection').get('rows')
    
    def get_card_type(self, type):
        types = self.get_card_types()
        for each in types:
            if each.get('id') == type or each.get('name') == type:
                return each
            
        return None
    
    def create(self, id, card_type):
        return super().create(
            data={
                "CardCollection": {
                    "rows": [
                        {
                            "card_id": str(id),
                            "card_type": card_type
                        }
                    ]
                }
            }
        )
    
    def __create_type_card(self, id, type_id):
        card_type = self.get_card_type(type_id)
        return self.create(id, card_type)
    
    def create_csn_card(self, id):
        return self.__create_type_card(id, 0)
    
    def create_csn_wiegand_card(self, id):
        return self.__create_type_card(id, 1)
    
    def create_secure_credential_card(self, id):
        return self.__create_type_card(id, 2)
    
    def create_access_on_card(self, id):
        return self.__create_type_card(id, 3)
    
    def create_csn_mobile(self, id):
        return self.__create_type_card(id, 4)
    
    def create_wiegand_mobile(self, id):
        return self.__create_type_card(id, 5)
    
    def create_qr(self, id):
        return self.__create_type_card(id, 6)
    
    def create_biostar2_qr(self, id):
        return self.__create_type_card(id, 7)
    
    def create_custom_smart_card(self, id):
        return self.__create_type_card(id, 8)
    
    def create_access_on_card(self, id):
        return self.__create_type_card(id, 9)
    
    def create_secure_credential_card(self, id):
        return self.__create_type_card(id, 10)
    
    def blacklist_card(self, card_id):
        return self.biostar2.post(
            f'{self.endpoint}/blacklist',
            headers=self.init_headers(),
            data=json.dumps({
                "Blacklist": {
                    "card_id": {
                        "id": str(card_id)
                    }
                }
            })
        )
    
    def get_card(self, card_id):
        return self.biostar2.get(
            f'{self.endpoint}?query={card_id}',
            headers=self.init_headers()
        )
    
    def get_all(self, card_type, limit=0, offset=0):
        params = f'card_type={card_type}&limit={limit}&offset={offset}'
        return super().get_all()