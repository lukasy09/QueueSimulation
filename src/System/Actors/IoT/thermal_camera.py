from System.Actors.IoT.sensor import Sensor
from Utils.GeneratorUtil import GeneratorUtil
from System.Agents.GeneratorAgent.agent import GeneratorAgent


"""Recognizing human's age, sex, pregnancy, disability"""


class ThermalCamera:
    instance = None

    @staticmethod
    def get_instance():
        if ThermalCamera.instance is None:
            ThermalCamera.instance = ThermalCamera()
            return ThermalCamera.instance
        return ThermalCamera.instance


    def detect(self):
        if self.instance is not None:
            return GeneratorAgent.generate_thermal_data()