from suprema.biostar2 import *

class Card(AbstractEndpoint):
    collection = "CardCollection"
    endpoint = "api/cards"

    def get_card_types(self):
        return self.biostar2.get(
            f'{self.endpoint}/types',
            self.init_headers()
        )