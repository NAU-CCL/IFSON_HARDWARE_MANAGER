import os
from Hardware_Manager.Hardware_Manager import NetworkComponent

class Network(NetworkComponent):
    def get_info(self):
        return {
            "name":"Raspberry Pi Eithernet Driver",
            "id":"eth0",
            "version":"0.1",
            "type":"ETH"
        }
        
    def nic_power_on(self):
        os.system('sudo ifconfig eth0 up')
        return True

    def nic_power_off(self):
        os.system(' sudo ifconfig eth0 down')
        return True