from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus
from System.Agents.ManagingAgent.customer_status import CustomerStatus
from System.Agents.ManagingAgent.customer_monitoring_status import CustomerMonitoringStatus

"""
    The class represents the system's main actor
"""


class Customer:
    # identification data stored in the main db
    index = None  # Informs about creation order of customers, unique(Integer).
    biometric = None  # Biometric data of a customer, unique hash
    customer_status = CustomerStatus.NORMAL  # Informs about the customer status(e.g is he/she a VIP or a regular customer)
    is_new = True  # Flag(Boolean) informing if the unit is known by the system before the simulation's start

    # Customer's properties set by the monitoring system based on the physical features
    elderly = False  # Boolean
    sex = None  # Enumeration
    disable = False  # Boolean
    pregnant = False  # Boolean
    thermal = False  # Boolean

    # Simulation/System info
    simulation_status = CustomerSimulationStatus.BEFORE  # Default status, BEFORE entering the system
    monitoring_status = CustomerMonitoringStatus.BEFORE_MONITORING
    shopping_remaining_time = None

    # @TODO Observers

    def __init__(self, identifier=None, biometric=None):
        self.index = identifier
        self.biometric = biometric

    """Mutation methods, setters and updates method(s)"""

    # Statuses and system identification knowledge


    def set_customer_status(self, status):
        self.customer_status = status

    def set_is_new(self, is_new):
        self.is_new = is_new

    def set_monitoring_status(self, status):
        self.monitoring_status = status

    def set_simulation_status(self, status):
        self.simulation_status = status


    # Simulation parameters - times


    def set_shopping_remaining_time(self, time):
        self.shopping_remaining_time = time

    def update_remaining_time(self):
        if self.shopping_remaining_time > 1:
            self.shopping_remaining_time -= 1


    # Own detected features


    def set_elderly(self, elderly):
        self.elderly = elderly

    def set_sex(self, sex):
        self.sex = sex

    def set_disable(self, disable):
        self.disable = disable

    def set_pregnant(self, pregnant):
        self.pregnant = pregnant

    def set_thermal(self, thermal):
        self.thermal = thermal


    """Customer's actions"""

    def enter_virtual_queue(self):
        pass

    """A log representation of a single customer"""

    def __str__(self):
        return "Customer:Index {},Biometric:{},Customer Status: {},\n Simulation status: {}, Monitoring status: {}, Elderly:{},\n Sex:{}, Disable:{}, Pregnant: {},\n Thermal: {}".format(
            self.index,
            self.biometric,
            self.customer_status,
            self.simulation_status,
            self.monitoring_status,
            self.elderly,
            self.sex,
            self.disable,
            self.pregnant,
            self.thermal)
