from System.Actors.Customer.customer_simulation_status import CustomerSimulationStatus
from System.Actors.Customer.customer_status import CustomerStatus
from System.Actors.Customer.customer_monitoring_status import CustomerMonitoringStatus

"""
    The class represents the system's main actor
"""


class Customer:

    def __init__(self, identifier=None, biometric=None):
        self.index = identifier  # Informs about creation order of customers, unique(Integer).
        self.biometric = biometric  # Biometric data of a customer, unique hash

        self.customer_status = CustomerStatus.NORMAL  # Informs about the customer status(e.g is he/she a VIP or a REGULAR customer or a NORMAL)
        self.is_new = True  # Flag(Boolean) informing if the unit is known by the system before the simulation's start

        # Customer's properties set by the monitoring system based on the physical features
        self.elderly = False  # Boolean
        self.sex = None  # Enumeration
        self.disable = False  # Boolean
        self.pregnant = False  # Boolean
        self.thermal = False  # Boolean

        # Simulation/System info
        self.simulation_status = CustomerSimulationStatus.BEFORE  # Default status, BEFORE entering the system
        self.monitoring_status = CustomerMonitoringStatus.BEFORE_MONITORING  # Enumeration

        self.appear_time = None
        self.virtual_queue_remaining_time = None  # Integer
        self.in_virtual_queue_area = False  # Boolean

        # Graph
        self.path = []  # The destination path
        self.tracked_path = []  # The path that was(in reality) passed by the customer
        self.next_node_time = 0
        self.times = []  # Walktime through nodes
        self.total_time = 0  # Total shopping time, that is a sum of all 'times'
        self.avg_speed = 0

        # Queues
        self.waiting_time = None  # Number, time spent in queue waiting for service
        self.service_time = None
        self.is_first = False  # Flag informing if the customer is first in queue

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

    def set_appear_time(self, time):
        self.appear_time = time
    # Simulation parameters - times

    def set_next_node_time(self, time):
        self.next_node_time = time

    def set_virtual_queue_remaining_time(self, time):
        self.virtual_queue_remaining_time = time

    def update_virtual_queue_remaining_time(self):
        if self.virtual_queue_remaining_time > 0:
            self.virtual_queue_remaining_time -= 1

    def start_waiting(self):
        self.waiting_time = 0

    def update_waiting_time(self):
        self.waiting_time += 1

    def set_service_time(self, time):
        self.service_time = time

    def update_service_time(self):
        self.service_time -= 1

    def set_is_first(self, is_first):
        self.is_first = is_first

    def update_next_node_time(self):
        self.next_node_time -= 1

    def update_total_time(self, time):
        self.total_time += time

    def set_avg_speed(self, speed):
        self.avg_speed = speed

    # Graph parameters

    def set_path(self, path):
        self.path = path

    def start_shopping(self):
        self.tracked_path = [self.path[0]]  # Setting the first node
        self.total_time = 0
        self.times = []

    def append_transition(self, node):
        self.tracked_path.append(node)

    def append_path_time(self, time):
        self.times.append(time)

    def get_current_node(self):
        return self.tracked_path[len(self.tracked_path) - 1]

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

    def enter_virtual_queue_area(self, await_time):
        self.in_virtual_queue_area = True
        self.set_virtual_queue_remaining_time(await_time)
        self.set_simulation_status(CustomerSimulationStatus.IN_VQ)


    def leave_virtual_queue_area(self):
        self.in_virtual_queue_area = False

    def display_tracked_path(self):
        path_str = "Tracked path: "
        for i in range(len(self.tracked_path)):
            node = str(self.tracked_path[i])
            path_str += node
            if not i == len(self.tracked_path) -1:
                path_str += " -> "
        print(path_str)
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