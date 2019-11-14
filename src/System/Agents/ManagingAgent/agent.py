from System.Actors.Queue.queue import Queue
from System.Agents.GeneratorAgent.agent import GeneratorAgent
from System.Agents.ManagingAgent.queue_types import QueueType
from System.Agents.ManagingAgent.simulation_mode import Traffic
from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus
from System.Agents.ManagingAgent.customer_monitoring_status import CustomerMonitoringStatus
from System.Agents.ManagingAgent.customer_status import CustomerStatus
from System.Agents.IdentificationAgent.agent import IdentificationAgent
from System.Agents.MonitoringAgent.agent import MonitoringAgent
from Database.DAO.customer_dao import CustomerDao

"""Managing agent  - MA"""


class ManagingAgent:

    # Simulation constant
    simulation_time = 3600  # time unit e.g seconds, minutes etc.
    pool_size = 1000   # The pool of customers.
    expected_shopping_time = 600
    defaultTraffic = Traffic.MEDIUM
    customer_period_range = None  # This parameter is is set during runtime
    monitoring_success_rate = 0.2  # Probability of monitoring success at a time t

    # queue_type: count
    queues_config = {
        QueueType.NORMAL: 2,
        QueueType.PRIVILEGED: 1,
        QueueType.MOST_PRIVILEGED: 1
    }

    # Pseudo-random client generation periods
    customer_period_ranges = {
        Traffic.VERY_HIGH: (10, 60),
        Traffic.HIGH: (10, 100),
        Traffic.MEDIUM: (30, 180),
        Traffic.LOW: (30, 600),
        Traffic.VERY_LOW: (50, 800)
    }

    shopping_time_distribution = (10 * 60, 250)  # N ~ (m, s), expected value is in seconds

    # Simulation variables
    customer_pool = []
    system_customers = []
    virtual_queue = []
    queues = []

    # Defaults
    traffic = Traffic.MEDIUM

    # Agents
    identification_agent = IdentificationAgent()
    monitoring_agents = []

    # Others aggregated objects
    dao = CustomerDao()

    def __init__(self, traffic=defaultTraffic):
        self.gen = GeneratorAgent(self.dao)
        self.traffic = traffic
        self.customer_period_range = self.customer_period_ranges[self.traffic]

        self.identification_agent.set_dao(self.dao)



    """Creating customer pool, queues"""
    def setup_environment(self):
        self.queues = self.init_queues()
        self.customer_pool = self.gen.generate_population(self.pool_size)


    """Initialising queues based on the config map"""
    def init_queues(self):
        queues = []
        config = self.queues_config.items()
        uniq_index = 0
        for item in config:
            queue_type = item[0]
            count = item[1]
            for i in range(count):
                queue = Queue(uniq_index, queue_type)
                queues.append(queue)
                uniq_index += 1
        return queues


    """Importing an unit(customer) to the system."""
    def import_to_system(self, new_customer, index):
        new_customer.set_simulation_status(CustomerSimulationStatus.IN)  # Setting the customer's simulation status

        customer_data = self.identification_agent.identify(new_customer)
        if customer_data is not None:  # The customer has been found, exists in the system
            new_customer.set_customer_status(customer_data[2])
            new_customer.set_is_new(bool(customer_data[3]))
        else:  # The customer is new
            new_customer.set_customer_status(CustomerStatus.NORMAL)
            self.identification_agent.register_new_customer(new_customer)

        self.system_customers.append(new_customer)  # Adding to the system's list
        del self.customer_pool[index]  # Removing from the customer pool


    def activate_monitoring_agent(self, observed_customer):
        monitoring_agent = MonitoringAgent(self.monitoring_success_rate)
        monitoring_agent.set_monitored(observed_customer)
        observed_customer.set_monitoring_status(CustomerMonitoringStatus.DURING_MONITORING)
        self.monitoring_agents.append(monitoring_agent)