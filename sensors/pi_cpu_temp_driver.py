from Hardware_Manager.Hardware_Manager import SensorComponent
import subprocess

class Sensor(SensorComponent):

    def get_reading(self):
        output = subprocess.run(['vcgencmd','measure_temp'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        temp_only = output.split("=",1)[1]
        no_cel = temp_only.split("'",1)[0]
        return no_cel

    def get_info(self):
        return {
            "id":'CPU_TEMP',
            "name":"Pi CPU Temp",
            "version":"0.1",
            "type":"CPU_TEMP"
        }