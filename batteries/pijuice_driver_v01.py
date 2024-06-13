from Hardware_Manager.Hardware_Manager import BatteryComponent

# Docs - https://github.com/PiSupply/PiJuice/tree/master/Software
from pijuice import PiJuice # Import pijuice module


class Battery(BatteryComponent):
    def get_info(self):
        return {
            "id":"pijuice",
            "name":"PiJuice Pi-Hat",
            "version":"0.1",
            "chemistry": "Lithium-ion"
        }

    def get_voltage(self):
        pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
        results = pijuice.status.GetBatteryVoltage()
        return results['data']

    def get_remaining_percent(self):
        pijuice = PiJuice(1, 0x14)
        results = pijuice.status.GetChargeLevel()
        return results['data']
    
    def get_current(self):
        pass