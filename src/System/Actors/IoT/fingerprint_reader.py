from System.Actors.IoT.sensor import Sensor


class FingerprintReader(Sensor):

    biometric = None

    def read(self, customer):
        self.biometric = customer.biometric

    def send(self):
        return self.biometric
