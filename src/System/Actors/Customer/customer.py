from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus

"""
    The class represents the system's main actor
"""


class Customer:

    # identification data stored in the main db
    index = None  # Informs about creation order of customers, unique.
    biometric = None  # Biometric data of a customer, unique
    customer_status = None  # Informs about the customer status(e.g is he/she a VIP or a regular customer)
    is_new = None  # Flag(Boolean) informing if the unit is known by the system before the simulation's start

    # Customer's properties set by the monitoring system
    age = None
    sex = None
    disable = None
    pregnant = None
    thermal = None

    # Simulation info
    status = CustomerSimulationStatus.BEFORE  # Default status, BEFORE entering the system
    shopping_remaining_time = None

    def __init__(self, identifier=None, biometric=None):
        self.index = identifier
        self.biometric = biometric

    def set_simulation_status(self, status):
        self.status = status

    def set_customer_status(self, status):
        self.customer_status = status

    def set_is_new(self, is_new):
        self.is_new = is_new

    def update_remaining_time(self):
        self.shopping_remaining_time -= 1

    def __str__(self):
        return "Customer:Index {},Biometric:{},Customer Status: {}, Simulation status: {}, Age:{}, Sex:{}, Disable:{}, Pregnant: {}, Thermal: {}".format(self.index,
                                                                                                                                                 self.biometric,
                                                                                                                                                 self.customer_status,
                                                                                                                                                 self.status,
                                                                                                                                                 self.age,
                                                                                                                                                 self.sex,
                                                                                                                                                 self.disable,
                                                                                                                                                 self.pregnant,
                                                                                                                                                 self.thermal)
