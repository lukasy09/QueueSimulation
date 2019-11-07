from System.Agents.ManagingAgent.customer_status import CustomerStatus

"""
    The class represents the system's main actor
"""


class Customer:

    # identification data stored in the main db
    index = None  # Informs about creation order of customers, unique.
    biometric = None  # Biometric data of a customer, unique
    customer_status = None  # Informs about the customer status(e.g is he/she a VIP or a regular customer)
    # Customer's properties set by the monitoring system
    age = None
    sex = None
    disable = None
    pregnant = None
    hurry = None

    # Simulation info
    status = CustomerStatus.BEFORE  # Default status, BEFORE entering the system
    shopping_remaining_time = None

    def __init__(self, identifier=None, biometric=None):
        self.index = identifier
        self.biometric = biometric

    def set_status(self, status):
        self.status = status

    def decrement_remaining_time(self):
        self.shopping_remaining_time -= 1

    def __str__(self):
        return "Customer:Index {},Biometric:{}, Age:{}, Sex:{}, Disable:{}, Pregnant: {}, In hurry: {}".format(self.index,
                                                                                                               self.biometric,
                                                                                                               self.age,
                                                                                                               self.sex,
                                                                                                               self.disable,
                                                                                                               self.pregnant,
                                                                                                               self.hurry)
