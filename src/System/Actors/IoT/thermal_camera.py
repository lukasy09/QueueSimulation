from System.Actors.IoT.sensor import Sensor
from Utils.GeneratorUtil import GeneratorUtil


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
        if self.instance is not None:
            return GeneratorUtil.generate_thermal_data()