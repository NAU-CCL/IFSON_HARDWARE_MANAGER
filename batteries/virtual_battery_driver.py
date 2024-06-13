from Hardware_Manager.Hardware_Manager import BatteryComponent

class Battery(BatteryComponent):
    def get_info(self):
        return {
            "id":"vbat01",
            "name":"Virtual Battery Driver",
            "version":"0.1",
            "chemistry": "Lithium-ion"
        }

    def get_voltage(self):
        return 11.9

    def get_remaining_percent(self):
        pass
    
    def get_current(self):
        pass