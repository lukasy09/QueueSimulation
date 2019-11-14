from System.Actors.IoT.sensor import Sensor


"""Recognizing human's age, sex, pregnancy, disability"""


class ThermalCamera:
    instance = None

    @staticmethod
    def get_instance():
        if self.instance is None:
            return ThermalCamera()
        return self.instance

    def record(self):
        pass