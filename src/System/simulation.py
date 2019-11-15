from System.Agents.ManagingAgent.agent import ManagingAgent
from System.Agents.ManagingAgent.simulation_mode import Traffic
from System.Agents.ManagingAgent.customer_monitoring_status import CustomerMonitoringStatus
from Utils.GeneratorUtil import GeneratorUtil
import time
from os import system
from datetime import datetime
from random import *


class Simulation:

    def __init__(self):
        pass

    @staticmethod
    def run():
        # Simulation parameters(if not using the default ones)
        traffic = Traffic.HIGH

        # Setting up initials, creating simulation's environment
        manager = ManagingAgent(traffic=traffic)
        manager.setup_environment()  # Creating customer pool & queues with passed parameters
        # Start
        current_time = 0  # Variable holds the current time of simulation
        appear_time = GeneratorUtil.get_next_appear_time(manager.customer_period_range[0],
                                                         manager.customer_period_range[1], current_time)
        while current_time < manager.simulation_time:
            # Is new customer in our system?
            if current_time == appear_time:
                # Import - removing a customer from the pool & adding him/her to the system's customer list
                new_customer_index = GeneratorUtil.generate_integer_in_range(0, len(manager.customer_pool))
                new_customer = manager.customer_pool[new_customer_index]
                manager.import_to_system(new_customer, new_customer_index)
                # Settings customer's simulation parameters
                new_customer.set_shopping_remaining_time(
                    GeneratorUtil.generate_shopping_time(manager.shopping_time_distribution[0],
                                                         manager.shopping_time_distribution[1]))
                manager.activate_monitoring_agent(new_customer)

                # The time when the next unit is appearing in our system
                appear_time = GeneratorUtil.get_next_appear_time(manager.customer_period_range[0],
                                                                 manager.customer_period_range[1], current_time)

            # Monitoring
            for monitoring_agent in manager.monitoring_agents:
                if monitoring_agent.customer.monitoring_status == CustomerMonitoringStatus.DURING_MONITORING:
                    monitoring_agent.monitor_customer()
                else:
                    pass


            current_time += 1


        for c in manager.system_customers:
            print(c)
        # print(len(manager.system_customers))
        # print(len(manager.monitoring_agents))
