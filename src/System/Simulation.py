
from System.Agents.ManagingAgent.agent import ManagingAgent
from System.Agents.ManagingAgent.simulation_mode import Traffic
from Utils.GaussianUtil import GaussianUtil
import time
from os import system
from datetime import datetime
from random import *

class Simulation:

    def __init__(self):
        pass

    def run(self):
        # Simulation parameters(if not using the default ones)
        traffic = Traffic.HIGH


        # Setting up initials
        manager = ManagingAgent(traffic=traffic)
        manager.setup_initial_state()  # Creating customer pool & queues

        customer_pool = manager.customer_pool # All available customers

        # Start
        current_time = 0  # Variable holds the current time of simulation
        appear_time = GaussianUtil.generate_integer_in_range(manager.customer_period_range[0], manager.customer_period_range[1] + 1)

        count = 0
        while current_time < manager.simulation_time:
            # Is new customer in our system?\
            now = datetime.now();
            system('clear')
            print(now.strftime("%d/%m/%Y %H:%M:%S"));
            for i in range(4):
                
                print('Queue ' + str(i) + ': ' + ('+' * randrange(0, 8)))
            time.sleep(1)
            if current_time == appear_time:
                appear_time = GaussianUtil.generate_integer_in_range(manager.customer_period_range[0] + current_time, manager.customer_period_range[1] + current_time + 1)

                count += 1

            current_time += 1

        print(count)