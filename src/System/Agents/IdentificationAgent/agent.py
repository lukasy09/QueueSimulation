from System.Actors.IoT.fingerprint_reader import FingerprintReader
from Database.DAO.customer_dao import CustomerDao


class IdentificationAgent:

    # IoT objects, sensors
    fingerprint_reader = FingerprintReader()

    # Other
    dao = None  # Data access object

    def set_dao(self, dao):
        self.dao = dao

    def identify(self, customer):
        biometric = self.fingerprint_reader.read(customer)
        self.dao.get_customer_by_biometric(biometric)

