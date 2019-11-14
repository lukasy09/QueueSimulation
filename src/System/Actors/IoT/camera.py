from System.Actors.IoT.sensor import Sensor


"""Recognizing human's age, sex, pregnancy, disability"""


class Camera(Sensor):
    instance = None

    @staticmethod
    def get_instance():
        if self.instance is None:
            return Camera()

        return self.instance

    def record(self):
        pass