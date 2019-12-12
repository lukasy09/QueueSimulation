from System.Actors.IoT.sensor import Sensor
from Utils.GeneratorUtil import GeneratorUtil
from System.Agents.GeneratorAgent.agent import GeneratorAgent


"""Recognizing human's age, sex, pregnancy, disability"""


class Camera(Sensor):
    instance = None

    @staticmethod
    def get_instance():
        if Camera.instance is None:
            Camera.instance = Camera()
            return Camera.instance
        return Camera.instance


    def detect(self):
        if self.instance is not None:
            return GeneratorAgent.generate_customer_data()