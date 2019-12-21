from System.Actors.Customer.customer_simulation_status import CustomerSimulationStatus
from System.Actors.Customer.customer_status import CustomerStatus
from System.Agents.QueueAgent.queue_types import QueueType


class VirtualQueueAgent:

    # instance
    instance = None

    # virtual queue
    virtual_queue = []

    @staticmethod
    def get_instance():
        if VirtualQueueAgent.instance is None:
            VirtualQueueAgent.instance = VirtualQueueAgent()
            return VirtualQueueAgent.instance

        return VirtualQueueAgent.instance

    def accept_customer(self, customer):
        self.virtual_queue.append(customer)


    def assign_queue(self, customer):
        if self.instance is not None:
            if customer.customer_status == CustomerStatus.VIP:
                return QueueType.VIP
            elif customer.elderly or customer.disable or customer.pregnant:
                return QueueType.SPECIAL
            elif customer.thermal or customer.avg_speed > 0.085:
                return QueueType.THERMAL
            else:
                return QueueType.NORMAL


    def remove_customer(self, customer):
        for i, unit in enumerate(self.virtual_queue):
            if unit.index == customer.index:
                del self.virtual_queue[i]