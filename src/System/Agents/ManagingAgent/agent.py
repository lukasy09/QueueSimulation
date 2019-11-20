import math
from Database.DAO.customer_dao import CustomerDao
from System.Agents.GeneratorAgent.agent import GeneratorAgent
from System.Agents.ManagingAgent.queue_types import QueueType
from System.Agents.ManagingAgent.simulation_mode import Traffic
from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus
from System.Agents.ManagingAgent.customer_monitoring_status import CustomerMonitoringStatus
from System.Agents.ManagingAgent.customer_status import CustomerStatus
from System.Agents.IdentificationAgent.agent import IdentificationAgent
from System.Agents.MonitoringAgent.agent import MonitoringAgent
from System.Agents.VirtualQueueAgent.agent import VirtualQueueAgent
from System.Agents.QueueAgent.agent import QueueAgent
from Utils.GeneratorUtil import GeneratorUtil


"""Managing agent  - MA"""


class ManagingAgent:

    # Simulation constants
    simulation_time = 3600  # time unit e.g seconds, minutes etc.
    pool_size = 1000   # The pool of customers.
    defaultTraffic = Traffic.HIGH  # Default mode

    customer_period_range = None  # This parameter is is set during runtime
    monitoring_success_rate = 0.2  # Probability of monitoring success at a time t
    virtual_queue_await_time = 5  # Time after which virtual queue system recognizes new unit in the VQ area

    # Generating parameters distributions
    shopping_time_distribution = (10 * 60, 50)  # N ~ (m, s), expected value is in seconds
    age_distribution = (35.6, 18)
    temperature_distribution = (36.6, 0.2)
    service_service_time_distribution = (120, 20)


    # queue_type: count, there must at least one queue for each type
    queues_config = {
        QueueType.VIP: 1,
        QueueType.THERMAL: 1,
        QueueType.SPECIAL: 1,
        QueueType.NORMAL: 1
    }

    # Pseudo-random client generation periods
    customer_period_ranges = {
        Traffic.ULTIMATE: (1, 10),
        Traffic.VERY_HIGH: (10, 60),
        Traffic.HIGH: (10, 100),
        Traffic.MEDIUM: (30, 180),
        Traffic.LOW: (30, 600),
        Traffic.VERY_LOW: (50, 800)
    }

    # Simulation variables
    customer_pool = []      # Collection of customers that may take part in simulation
    system_customers = []   # Collection of all customers that came through the system
    removed_customers = []  # Collection of all customers that had left the system before the simulation  ended

    # Defaults
    traffic = Traffic.MEDIUM

    # Agents
    identification_agent = IdentificationAgent.get_instance()
    monitoring_agents = []
    virtual_queue_agent = VirtualQueueAgent.get_instance()
    queues_agents = []


    # Others aggregated objects
    dao = CustomerDao()

    def __init__(self, traffic=defaultTraffic):
        self.gen = GeneratorAgent(self.dao)
        self.traffic = traffic
        self.customer_period_range = self.customer_period_ranges[self.traffic]
        self.identification_agent.set_dao(self.dao)



    """Creating customer pool, queues"""
    def setup_environment(self):
        self.queues_agents = self.init_queues_agents()
        self.customer_pool = self.gen.generate_population(self.pool_size)

    """Initialising queues based on the config map"""
    def init_queues_agents(self):
        queues_agents = []
        config = self.queues_config.items()
        uniq_index = 0
        for item in config:
            queue_type = item[0]
            count = item[1]
            for i in range(count):
                queue_agent = QueueAgent(uniq_index)
                queue_agent.set_queue_type(queue_type)
                queues_agents.append(queue_agent)
                uniq_index += 1
        return queues_agents


    """Importing an unit(customer) to the system."""
    def import_to_system(self, new_customer, index):
        customer_data = self.identification_agent.identify(new_customer)
        if customer_data is not None:  # The customer has been found, exists in the system
            new_customer.set_customer_status(customer_data[2])
            new_customer.set_is_new(bool(customer_data[3]))
        else:  # The customer is new
            new_customer.set_customer_status(CustomerStatus.NORMAL)
            self.identification_agent.register_new_customer(new_customer)

        new_customer.set_simulation_status(CustomerSimulationStatus.IN)  # Setting the customer's simulation status
        self.system_customers.append(new_customer)  # Adding to the system's list
        del self.customer_pool[index]  # Removing from the customer pool


    """Activating an agent per an unit(customer). 
       Customers with these agents are in relation 1 to 1"""

    def activate_monitoring_agent(self, observed_customer):
        monitoring_agent = MonitoringAgent(self.monitoring_success_rate)
        monitoring_agent.set_monitored(observed_customer)
        observed_customer.set_monitoring_status(CustomerMonitoringStatus.DURING_MONITORING)
        self.monitoring_agents.append(monitoring_agent)



    """Passing the customer on to the VQ agent and deleting from the system list(shopping)"""
    def join_virtual_queue(self, customer):
        self.virtual_queue_agent.accept_customer(customer)
        # for i, unit in enumerate(self.system_customers):
        #     if unit.index == customer.index:
        #         del self.system_customers[i]
        customer.set_simulation_status(CustomerSimulationStatus.IN_VQ)


    """Delegating a customer to an assigned queue type.
       This method directs to the queue with lowest number of units"""
    def delegate_customer(self, customer, queue_type):
        matching_agents = []
        for queue_agent in self.queues_agents:
            if queue_agent.queue_type == queue_type:
                matching_agents.append(queue_agent)

        minimal_length = math.inf
        optimal_agent = None
        for matching_agent in matching_agents:
            if len(matching_agent.queue) == 0:
                matching_agent.accept(customer)
            else:
                if len(matching_agent.queue) < minimal_length:
                    minimal_length = len(matching_agent.queue)
                    optimal_agent = matching_agent

        if optimal_agent is not None:
            optimal_agent.accept(customer)

        self.virtual_queue_agent.remove_customer(customer)  # Removing from the VQ
        customer.set_service_time(GeneratorUtil.generate_service_time(self.service_service_time_distribution))
        customer.set_simulation_status(CustomerSimulationStatus.IN_QUEUE)  # Setting the customer's status
        customer.start_waiting()


    """Removing customer from the system. Adding the unit to the removed list"""
    def remove_customer(self, customer):
        customer.set_simulation_status(CustomerSimulationStatus.AFTER)
        self.removed_customers.append(customer)

    """Deactivating monitoring agent"""
    def deactivate_monitoring_agent(self, index):
        pass