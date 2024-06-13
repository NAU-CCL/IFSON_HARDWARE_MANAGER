import os
from Hardware_Manager.Hardware_Manager import NetworkComponent

class Network(NetworkComponent):
    def get_info(self):
        return {
            "name":"Raspberry Pi Wireless Driver",
            "id":"wlan0",
            "version":"0.1",
            "type":"WLAN"
        }
        
    def nic_power_on(self):
        os.system('sudo ifconfig wlan0 up')
        os.system('sudo rfkill unblock wlan')
        return True

    def nic_power_off(self):
        os.system('sudo ifconfig wlan0 down')
        os.system('sudo rfkill block wlan')
        return True