from System.Actors.IoT.sensor import Sensor


"""Recognizing human's age, sex, pregnancy, disability"""


class ThermalCamera:
    instance = None

    @staticmethod
    def get_instance():
        if ThermalCamera.instance is None:
            ThermalCamera.instance = ThermalCamera()
            return ThermalCamera.instance
        return ThermalCamera.instance

    def record(self):
        pass