from System.Agents.ManagingAgent.agent import ManagingAgent
from System.Agents.ManagingAgent.simulation_mode import Traffic
from System.Agents.ManagingAgent.customer_monitoring_status import CustomerMonitoringStatus
from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus
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

            # Monitoring customer behaviour
            for monitoring_agent in manager.monitoring_agents:
                if monitoring_agent.customer.monitoring_status == CustomerMonitoringStatus.DURING_MONITORING:
                    monitoring_agent.monitor_customer()

            # Customer's behaviour in system
            for customer in manager.system_customers:

                # Customers in system, shopping
                if customer.simulation_status == CustomerSimulationStatus.IN \
                        and customer.monitoring_status == CustomerMonitoringStatus.AFTER_MONITORING \
                        and customer.shopping_remaining_time == 0:  # Customer entering VQ's area

                    if not customer.in_virtual_queue_area:  # If the customer wasn't in VQ's area before
                        customer.enter_virtual_queue_area(manager.virtual_queue_await_time)
                    else:
                        if customer.virtual_queue_remaining_time == 0:  # A customer is waiting long enough for queue assignment
                            manager.join_virtual_queue(customer)

                    customer.update_virtual_queue_remaining_time()  # waiting for queue assignment

                # Customers in virtual queue
                elif customer.simulation_status == CustomerSimulationStatus.IN_VQ:
                    assigned_queue_type = manager.virtual_queue_agent.assign_queue(customer)  # Assigning queue type by the customer's state
                    manager.delegate_customer(customer, assigned_queue_type)  # Sending the customer to the right queue

                # Customers in system who are not in any special state (doing shopping etc.)
                else:
                    customer.update_shopping_remaining_time()  # Decrementing

            # Customers waiting in queues
            for queue_agent in manager.queues_agents:
                customers_queue = queue_agent.queue  # Queue (list)

                for customer in customers_queue:
                    if customer.simulation_status == CustomerSimulationStatus.IN_QUEUE:
                        customer.set_is_first(True)  # Setting is_first flag in each queue
                        break

                for i in range(len(customers_queue)):
                    customer = customers_queue[i]
                    if customer.simulation_status == CustomerSimulationStatus.IN_QUEUE and customer.service_time == 0 and customer.is_first:
                            manager.remove_customer(customer)  # Removing from the system and the simulation, setting status
                            customer.set_is_first(False)
                    else:
                            customer.update_service_time()
                            customer.update_waiting_time()


            current_time += 1

        # print(len(manager.monitoring_agents), "<- Number of monitoring agents/all customers in simulation")
        print(len(manager.system_customers), "<- Number of customers still in system")
        c = 0
        for customer in manager.system_customers:
            if customer.simulation_status == CustomerSimulationStatus.IN:
                c += 1
        print(c, "<- Number of customers in shopping")
        print(len(manager.virtual_queue_agent.virtual_queue), "<- Customers in VQ")
        print(len(manager.removed_customers), "<- Removed customers")
        count = 0
        for i in range(len(manager.queues_agents)):
            queue_agent = manager.queues_agents[i]
            for unit in queue_agent.queue:
                if unit.simulation_status == CustomerSimulationStatus.IN_QUEUE:
                    count += 1
        print(count, "<- Customers in all queues")
