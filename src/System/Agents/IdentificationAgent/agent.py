from System.Actors.IoT.fingerprint_reader import FingerprintReader
from Database.DAO.customer_dao import CustomerDao

"""Identification agent,cooperating with fingerprint reader(s). 
    It manages them, responsible for customer identification and registering if he/she is not known to the system """


class IdentificationAgent:

    # Instance
    instance = None

    # IoT objects, sensors
    fingerprint_reader = FingerprintReader()

    # Other
    dao = None  # Data access object

    @staticmethod
    def get_instance():
        if IdentificationAgent.instance is None:
            IdentificationAgent.instance = IdentificationAgent()
            return IdentificationAgent.instance

        return IdentificationAgent.instance

    def set_dao(self, dao):
        self.dao = dao

    def identify(self, customer):
        self.fingerprint_reader.read(customer)
        biometric = self.fingerprint_reader.send()
        return self.dao.get_customer_by_biometric(biometric)

    def register_new_customer(self, customer):
        self.dao.save_new_customer(customer)
