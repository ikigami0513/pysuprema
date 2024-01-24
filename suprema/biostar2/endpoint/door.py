from suprema.biostar2 import *

class Door(AbstractEndpoint):
    collection = "DoorCollection"
    endpoint = 'api/doors'

    def get_all(self, limit=0, order_by_id=True):
        return super().get_all(params=f'limit={limit}&order_by=id:{"true" if order_by_id else "false"}')
    
    def get(self, door):
        return self.biostar2.get(
            endpoint=f'{self.endpoint}/{door}',
            headers=self.init_headers()
        )
    
    def create(
        self, name: str, door_group_id: int, 
        relayOutputId_deviceId_id: int, relayOutputId_relayIndex: int,
        exitButtonInputId_deviceId_id: int, exitButtonInputId_inputIndex: int, exitButtonInputId_type: bool,
        sensorInputId_deviceId_id: int, sensorInputId_inputIndex: int, sensorInputId_type: bool, sensorInputId_ApbUseDoorSensor: bool,
        description: str=None, open_timeout: int=None, open_duration: int=None, open_once: bool=None, unconditional_lock: bool=None
    ):
        not_required = dict()
        if description is not None:
            not_required["description"] = description
        if open_timeout is not None:
            not_required["open_timeout"] = open_timeout
        if open_duration is not None:
            not_required["open_duration"] = open_duration
        if open_once is not None:
            not_required["open_once"] = open_once
        if unconditional_lock is not None:
            not_required["unconditional_lock"] = unconditional_lock

        return super().create({
            "Door": {
                "name": name,
                "door_group_id": {"id": door_group_id},
                "entry_device_id": {"id": relayOutputId_deviceId_id},
                "relay_output_id": {
                    "device_id": {"id": relayOutputId_deviceId_id},
                    "relay_index": relayOutputId_relayIndex,
                },
                "exit_button_input_id": {
                    "device_id": {"id": exitButtonInputId_deviceId_id},
                    "input_index": exitButtonInputId_inputIndex,
                    "type": exitButtonInputId_type
                },
                "sensor_input_id": {
                    "device_id": {"id": sensorInputId_deviceId_id},
                    "input_index": sensorInputId_inputIndex,
                    "type": sensorInputId_type,
                    "apb_use_door_sensor": sensorInputId_ApbUseDoorSensor
                },
                **not_required
            }
        })
    
    def update(self, door, data):
        return super().update(door, data=data)
    
    def delete(self, doors):
        if isinstance(doors, list):
            doors = " ".join(doors)

        return super().delete(doors)
    
    def open_door(self, door):
        return self.biostar2.post(
            endpoint=f'{self.endpoint}/open',
            headers=self.init_headers(),
            data={
                "DoorCollection": {
                    "rows": [
                        {
                            "id": door
                        }
                    ]
                }
            }
        )