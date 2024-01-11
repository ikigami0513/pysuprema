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