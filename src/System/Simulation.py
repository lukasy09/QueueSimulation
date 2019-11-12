from System.Agents.ManagingAgent.agent import ManagingAgent
from System.Agents.ManagingAgent.simulation_mode import Traffic
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


        # Setting up initials
        manager = ManagingAgent(traffic=traffic)
        manager.setup_initial_state()  # Creating customer pool & queues

        # Start
        current_time = 0  # Variable holds the current time of simulation
        appear_time = GeneratorUtil.get_next_appear_time(manager.customer_period_range[0], manager.customer_period_range[1], current_time)

        while current_time < manager.simulation_time:
            # Is new customer in our system?
            if current_time == appear_time:
                # Removing a customer from the pool & adding him/her to the system's customer list
                new_customer_index = GeneratorUtil.generate_integer_in_range(0, len(manager.customer_pool))
                manager.import_to_system(new_customer_index)

                #
                appear_time = GeneratorUtil.get_next_appear_time(manager.customer_period_range[0], manager.customer_period_range[1], current_time)

            current_time += 1
        print(len(manager.customer_pool))
        print(len(manager.system_customers))