from Hardware_Manager.Hardware_Manager import CameraComponent

class Camera(CameraComponent):
    def get_info(self):
        return {
            "id":"vcam01",
            "name":"Virtual Camera Driver",
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

        print(f"Virtual Photo saved to {path}")

        return True

    def take_video(self, length_int):
        pass

    def camera_reset(self):
        pass