from Hardware_Manager.Hardware_Manager import SensorComponent
import random

class Sensor(SensorComponent):

    device_id = '/dev/930snteut9u-49usnewuosnew'

    def get_reading(self):
        return random.randrange(1,5)

    def get_info(self):
        return {
            "id":self.device_id,
            "name":"Virtual Solar Controller",
            "version":"0.1",
            "type":"SOLAR_PANEL"
        }