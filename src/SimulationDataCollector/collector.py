from System.Actors.Customer.customer_simulation_status import CustomerSimulationStatus
from System.Agents.QueueAgent.queue_types import QueueType
from System.Actors.Customer.customer_status import CustomerStatus
import json


class SimulationDataCollector:

    def __init__(self):
        self.manager = None

    def set_data_source(self, manager):
        self.manager = manager

    def collect_simulation_data(self):
        manager = self.manager
        out = {}
        queues = []


        for queue_agent in manager.queues_agents:
            indexes = []
            for customer in queue_agent.queue:
                indexes.append(customer.index)

            obj = {
                "index": queue_agent.index,
                "type": queue_agent.queue_type,
                "total": len(queue_agent.queue),
                "waiting_at_the_end": queue_agent.get_active_waiting_customers(),
                "queue": indexes,
                "mean_waiting_time": self.get_mean_waiting_time(queue_agent.index),
                "active_customers_per_time": queue_agent.queue_count_through_time
            }

            queues.append(obj)

        customers = []
        total_customers = len(manager.system_customers)
        vip = 0
        elderly = 0
        males = 0
        females = 0
        disable = 0
        pregnant = 0
        thermal = 0

        for customer in manager.system_customers:

            if customer.customer_status == CustomerStatus.VIP:
                vip += 1
            if customer.elderly:
                elderly += 1
            if customer.sex == 'M':
                males += 1
            else:
                females += 1

            if customer.disable:
                disable += 1
            if customer.pregnant:
                pregnant += 1
            if customer.thermal:
                thermal += 1

            tracked_path = customer.tracked_path
            obj = {
                "index": customer.index,
                "biometric": str(customer.biometric),
                "is_new": customer.is_new,
                "elderly": customer.elderly,
                "sex": customer.sex,
                "disable": customer.disable,
                "pregnant": customer.pregnant,
                "thermal": customer.thermal,
                "appear_time": customer.appear_time,
                "tracked_path": customer.tracked_path,
                "times": customer.times,
                'total_shopping_time': customer.total_time,
                'waiting_time': customer.waiting_time,
            }
            customers.append(obj)

        stats = {
            "all": total_customers,
            "vip": vip,
            "elderly": elderly,
            "males": males,
            "females": females,
            "disable": disable,
            "pregnant": pregnant,
            "thermal": thermal
        }

        out["statistics"] = stats
        out["queues"] = queues
        out["customers"] = customers
        return out

    def get_mean_waiting_time(self, queue_index):
        manager = self.manager
        count = 0
        length = None
        for queue_agent in manager.queues_agents:
            if queue_agent.index == queue_index:

                for customer in queue_agent.queue:
                    count += customer.waiting_time
                length = len(queue_agent.queue)
        assert length > 0
        return count/length


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
                queues_mean_waiting_time[str(queue_agent.queue_type)] = round(
                    queue_waiting_time_sum / queue_customer_number)

        return queues_mean_waiting_time

    """Collecting data about customers that currently are or were in any queue"""

    def collect_queue_status_customers(self, status):
        manager = self.manager
        serviced_customers = {}
        total = 0
        for queue in manager.queues_agents:
            count = 0
            for customer in queue.queue:
                if customer.simulation_status == status:
                    count += 1
                    total += 1

            serviced_customers[str(queue.queue_type)] = count
        serviced_customers["total"] = total
        return serviced_customers


    def collect_statistics(self, customer):
        vip = False
        if customer.customer_status == CustomerStatus.VIP:
            vip = True

        return {
            "vip": vip,
            "elderly": customer.elderly,

        }


