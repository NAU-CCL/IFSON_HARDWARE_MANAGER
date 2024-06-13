from Hardware_Manager.Hardware_Manager import CameraComponent

from picamera2 import Picamera2
import time

class Camera(CameraComponent):
    def get_info(self):
        return {
            "name":"PiCamera V2",
            "id":"picamv2",
            "version":"0.1",
            "type":"CAMERA"
        }

    def power_on(self):
        pass

    def power_off(self):
        pass

    def is_powered_on(self):
        pass

    def take_photo(self, path):

        picam2 = Picamera2()

        picam2.start()
        time.sleep(2)

        picam2.capture_file(path)

        time.sleep(2)
        picam2.close()

        return True

    def take_video(self, length_int):
        pass

    def camera_reset(self):
        pass