from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus
from System.Agents.ManagingAgent.queue_types import QueueType


class SimulationDataCollector:

    def __init__(self):
        self.manager = None

    def set_data_source(self, manager):
        self.manager = manager

    def collect_data(self):
        general = self.collect_general_data()
        mean_time_data = self.compute_mean_waiting_time()
        # shopping_customers = self.collect_system_status_customers(CustomerSimulationStatus.IN)
        # vq_customers = self.collect_queue_status_customers(CustomerSimulationStatus.IN_VQ)
        waiting_customers = self.collect_queue_status_customers(CustomerSimulationStatus.IN_QUEUE)
        serviced_customers = self.collect_queue_status_customers(CustomerSimulationStatus.AFTER)

        return general, mean_time_data, waiting_customers, serviced_customers

    """Collecting general simulation data"""
    def collect_general_data(self):
        manager = self.manager
        general = {
            "time": manager.simulation_time,
            "total": len(manager.system_customers)
        }
        return general



    """Computing customers' mean waiting time per each queue"""
    def compute_mean_waiting_time(self):
        manager = self.manager
        queues_mean_waiting_time = dict()
        for i in range(len(manager.queues_agents)):
            queue_agent = manager.queues_agents[i]
            queue_waiting_time_sum = 0
            queue_customer_number = len(queue_agent.queue)  # The number of all customers that came through a given queue in whole simulation time
            for unit in queue_agent.queue:
                queue_waiting_time_sum += unit.waiting_time

            if queue_customer_number > 0:
                queues_mean_waiting_time["{}:{}".format(queue_agent.queue_type, queue_agent.index)] = round(queue_waiting_time_sum/queue_customer_number)

        return queues_mean_waiting_time


    """Collecting data about customers that currently are or were in any queue"""
    def collect_queue_status_customers(self, status):
        manager= self.manager
        serviced_customers = {}
        total = 0
        for queue in manager.queues_agents:
            count = 0
            for customer in queue.queue:
                if customer.simulation_status == status:
                    count += 1
                    total += 1

            serviced_customers["{}:{}".format(queue.queue_type, queue.index)] = count
        serviced_customers["total"] = total
        return serviced_customers


    def collect_system_status_customers(self, status):
        manager = self.manager
        count = 0
        for customer in manager.system_customers:
            if customer.simulation_status == status:
                count += 1

        return status, count



    def log_final_state(self):
        manager = self.manager
        self.collect_data()
        #
        print(len(manager.system_customers), "<- Number of customers that were in system")
        c = 0
        for customer in manager.system_customers:
            if customer.simulation_status == CustomerSimulationStatus.IN:
                c += 1
        print(c, "<- Number of customers in shopping")
        print(len(manager.virtual_queue_agent.virtual_queue), "<- Customers in VQ")
        c = 0
        for customer in manager.system_customers:
            if customer.simulation_status == CustomerSimulationStatus.IN_QUEUE:
                c += 1
        print(c, "<- In queue customers")
        print(len(manager.removed_customers), "<- Removed customers")


