from System.Actors.Queue.queue import Queue
from System.Agents.GeneratorAgent.agent import GeneratorAgent
from System.Agents.ManagingAgent.queue_types import QueueType
from System.Agents.ManagingAgent.simulation_mode import Traffic
from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus
from System.Agents.IdentificationAgent.agent import IdentificationAgent
from Database.DAO.customer_dao import CustomerDao

"""Managing agent  - MA"""


class ManagingAgent:

    # Simulation constant
    simulation_time = 3600  # time unit e.g seconds, minutes etc.
    pool_size = 1000
    expected_shopping_time = 600
    defaultTraffic = Traffic.MEDIUM
    customer_period_range = None  # This parameter is is set during runtime

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

    # Simulation variables
    customer_pool = []
    system_customers = []
    virtual_queue = []
    queues = []

    # Defaults
    traffic = Traffic.MEDIUM

    # Agents
    identification_agent = IdentificationAgent()

    # Others aggregated objects
    dao = CustomerDao()

    def __init__(self, traffic=defaultTraffic):
        self.gen = GeneratorAgent(self.dao)
        self.traffic = traffic
        self.customer_period_range = self.customer_period_ranges[self.traffic]

        self.identification_agent.set_dao(self.dao)



    """Creating customer pool, queues"""
    def setup_initial_state(self):
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
    def import_to_system(self, index):
        new_customer = self.customer_pool[index]
        self.identification_agent.identify(new_customer)

        self.system_customers.append(new_customer)  # Adding to the system's list
        new_customer.set_simulation_status(CustomerSimulationStatus.IN)  # Setting the customer's simulation status
        del self.customer_pool[index]  # Removing from the customer pool

