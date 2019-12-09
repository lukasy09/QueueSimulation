from System.Agents.QueueAgent.queue_types import QueueType
from System.Actors.Customer.customer_simulation_status import CustomerSimulationStatus


class QueueAgent:

    # queue identifier
    index = None

    # type of the related queue to the agent
    queue_type = QueueType.NORMAL  # NORMAL is the default one
    expected_waiting_time = 0

    def __init__(self, index):
        self.index = index
        self.queue = []

    def set_queue_type(self, queue_type):
        self.queue_type = queue_type

    def accept(self, customer):
        self.queue.append(customer)

    def remove_head(self):
        self.queue.remove(self.queue[0])

    def print_queue(self):
        for cus in self.queue:
            print(cus.next_node_time)
            print(cus.path)

    def get_active_waiting_customers(self):
        count = 0
        for customer in self.queue:
            if customer.simulation_status == CustomerSimulationStatus.IN_QUEUE:
                count += 1
        return count

    def __str__(self):
        return "QueueAgent: Index: {}, type: {}, number of people waiting: {}"\
                .format(self.index, self.queue_type, self.get_active_waiting_customers())