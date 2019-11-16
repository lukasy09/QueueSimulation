from System.Actors.IoT.sensor import Sensor
from Utils.GeneratorUtil import GeneratorUtil


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
            return GeneratorUtil.generate_customer_data()