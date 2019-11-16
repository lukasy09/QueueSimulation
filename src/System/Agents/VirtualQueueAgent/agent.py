from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus


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