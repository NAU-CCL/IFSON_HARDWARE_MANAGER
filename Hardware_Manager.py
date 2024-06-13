from abc import ABC, abstractmethod
import importlib
import os, inspect
from fnmatch import fnmatch
from typing import TypedDict

# Define minimum return values for get info
class HardwareInfo(TypedDict):
    id: str
    name: str
    version: float

# Component interface, to define what methods we need for each component
class Component(ABC):
    @abstractmethod
    def get_info(self) -> HardwareInfo:
        pass

class Hardware_Manager(Component):

    id = ''
    name = ''
    version = ''

    _screens = []
    _cameras = []
    _batteries = []
    _network_interfaces = []
    _storage = []
    _sensors = []
    _buttons = []
    _indicators = []

    def __init__(self, hardware_manifest):
        print('Hardware manager is setting up....')
        print(hardware_manifest)

        # iterate the hardware manifest and find specific modules
        for hardware_driver in hardware_manifest:

            # clawl directories and find matching drivers
            root = './Hardware_Manager'
            pattern = "*.py"

            for path, subdirs, files in os.walk(root):
                for name in files:
                    if fnmatch(name, pattern):
                        if hardware_driver == name:

                            # Import values. No *.py and no / in path
                            module_folder = path.split('/')[-1:][0]
                            module_name = name.split('.py')[0]

                            # Dynamically import module
                            module = importlib.import_module(f"Hardware_Manager.{module_folder}.{module_name}")
                            module_primary_class = inspect.getmembers(module)[0][0] #Main class of driver
                            # 
                            driver_class = getattr(module, module_primary_class) #setup
                            driver_instance = driver_class()

                            # print([module_folder, module_name, module_primary_class])
                            # self.[module_folder].append(driver_instance)

                            # Push the module to the correct array
                            if hasattr(self, "_"+module_folder):
                                getattr(self, "_"+module_folder).append(driver_instance)

    @property
    def screens(self):
        return self._screens

    @property
    def cameras(self):
        return self._cameras

    @property
    def batteries(self):
        return self._batteries

    @property
    def network_interfaces(self):
        return self._network_interfaces

    @property
    def storage(self):
        return self._storage

    @property
    def sensors(self):
        return self._sensors

    @property
    def buttons(self):
        return self._buttons

    @property
    def indicators(self):
        return self._indicators

    @property
    def system_uptime(self):
        pass
    @property
    def system_shutdown(self):
        pass
    @property
    def system_reboot(self):
        pass
    @property
    def get_power_source(self):
        pass
    @property
    def get_active_network_interface(self):
        pass

    def get_info(self):
        return {
            "id":self.id,
            "name":self.name,
            "version":self.version
        }

class ScreenComponent(Component):
    @abstractmethod
    def display_text(self):
        pass
    @abstractmethod
    def clear(self):
        pass
    @abstractmethod
    def backlight_power_on(self):
        pass
    @abstractmethod
    def backlight_power_off(self):
        pass

class SensorComponent(Component):
    @abstractmethod
    def get_reading(self):
        pass

class CameraComponent(Component):

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def is_powered_on(self):
        pass

    @abstractmethod
    def take_photo(self, path):
        pass

    @abstractmethod
    def take_video(self, length_int):
        pass

    @abstractmethod
    def camera_reset(self):
        pass

class BatteryComponent(Component):
    @abstractmethod
    def get_voltage(self):
        pass
    @abstractmethod
    def get_remaining_percent(self):
        pass
    @abstractmethod
    def get_current(self):
        pass

class NetworkComponent(Component):
    @abstractmethod
    def nic_power_on(self):
        pass
    @abstractmethod
    def nic_power_off(self):
        pass

class StorageComponent(Component):
    @abstractmethod
    def get_rootpath(self):
        pass
    @abstractmethod
    def storage_type(self):
        pass
    @abstractmethod
    def get_capacity(self):
        pass
    @abstractmethod
    def get_free_space(self):
        pass
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def unmount(self):
        pass
    @abstractmethod
    def mount(self):
        pass
    @abstractmethod
    def is_mounted(self):
        pass

class ButtonComponent(Component):
    @abstractmethod
    def press(self):
        pass
    @abstractmethod
    def release(self):
        pass