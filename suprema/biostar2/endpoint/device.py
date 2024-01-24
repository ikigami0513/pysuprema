from suprema.biostar2 import *

class Device(AbstractEndpoint):
    endpoint = "api/devices"

    def get_all(self, params=''):
        return super().get_all(params)
    
    def get_information(self, device):
        return self.biostar2.get(
            endpoint=f'{self.endpoint}/{device}',
            headers=self.init_headers()
        )
    
    def get_configuration(self, device):
        return self.biostar2.get(
            endpoint=f'{self.endpoint}/{device}/config',
            headers=self.init_headers()
        )
    
    def connect(self, device):
        return self.biostar2.post(
            endpoint=f'{self.endpoint}/{device}/connect',
            headers=self.init_headers()
        )
    
    def disconnect(self, device):
        return self.biostar2.post(
            endpoint=f'{self.endpoint}/{device}/disconnect',
            headers=self.init_headers()
        )

    def create(self, id, name, deviceGroupId_id, lan_ip, lan_devicePort=None, isDisabled=None, lan_enableDhcp=None):
        return super().create({
            "Device": {
                "id": id,
                "name": name,
                "device_type_id": {
                    "id": deviceGroupId_id
                },
                "connection": {
                    "status": "3"
                },
                "lan": {
                    "ip": lan_ip,
                    "connection_mode": "1"
                },
                "system": {},
                "capacity": {
                    "support_alphanumeric": "true"
                },
                "support_occupancy": "false",
                "pktversion": "3",
                "device_group_id": {
                    "id": deviceGroupId_id
                }
            }
        })
    
    def update(self, device, data):
        return super().update(device, data)