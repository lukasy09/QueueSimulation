from System.Agents.ManagingAgent.agent import ManagingAgent
from System.Agents.ManagingAgent.simulation_mode import Traffic
from System.Actors.Customer.customer_monitoring_status import CustomerMonitoringStatus
from System.Actors.Customer.customer_simulation_status import CustomerSimulationStatus
from Utils.GeneratorUtil import GeneratorUtil
import time
import os
from datetime import datetime
from random import *
import logging
import logging.handlers

"""The class runs the simulation."""


class Simulation:

    # Simulation output messages
    SETUP_ENV_STR = "Setting up simulation environment..."
    STARTING_STR = "Starting for "


    def __init__(self, console_logger, file_logger, collector):
        # Simulation parameters
        self.simulation_time = 2400  # time unit e.g seconds, minutes etc.
        self.traffic = Traffic.VERY_HIGH  # Simulation mode
        self.pool_size = 1000  # The pool of customers.
        self.scene_size = 6, 4  # The scene size m,n where m is number of rows(height) and the n is refers to the width(columns)`
        self.speed_factor = 500  # Parametrizing the simulation speed

        self.console_logger = console_logger  # Console logger
        self.file_logger = file_logger  # File logger
        self.collector = collector  # Collector, aggreagating simulation's data

        self.tracked_customer_index = 0  # The tracked customer index in system_customer list
        self.tracked_customer = None  # Tracked customer's object
        self.path_changed = False  # Holding if the tracked customer has changed the position


    def run(self):
        # Setting up initials, Managing Agent, creating simulation's environment
        manager = ManagingAgent(traffic=self.traffic, time=self.simulation_time, pool_size=self.pool_size, scene_size=self.scene_size)

        self.console_logger.log_message(self.SETUP_ENV_STR)
        # self.console_logger.clean()
        manager.setup_environment()  # Creating customer pool & queues with passed parameters
        self.console_logger.log_with_await(self.STARTING_STR, 3)

        # Start
        current_time = 0  # Variable holds the current time of simulation
        appear_time = GeneratorUtil.get_next_appear_time(manager.customer_period_range[0],
                                                         manager.customer_period_range[1], current_time)
        while current_time <= manager.simulation_time:
            # Is new customer in our system?
            if current_time == appear_time:
                # Import - removing a customer from the pool & adding him/her to the system's customer list
                new_customer_index = GeneratorUtil.generate_integer_in_range(0, len(manager.customer_pool))
                new_customer = manager.customer_pool[new_customer_index]
                manager.import_to_system(new_customer, new_customer_index)

                # Settings customer's simulation parameters
                new_customer.set_path(GeneratorUtil.generate_path(manager.scene))

                path_time = GeneratorUtil.generate_next_nodetime(manager.node_time_distribution[0],
                                                                 manager.node_time_distribution[1],
                                                                 manager.node_time_distribution[2])
                new_customer.set_next_node_time(path_time)
                new_customer.append_path_time(path_time)
                new_customer.start_shopping()

                # Activating customer's monitoring agent
                manager.activate_monitoring_agent(new_customer)

                # The time when the next unit is appearing in our system
                appear_time = GeneratorUtil.get_next_appear_time(manager.customer_period_range[0],
                                                                 manager.customer_period_range[1], current_time)

            # Monitoring customer behaviour
            for monitoring_agent in manager.monitoring_agents:
                if monitoring_agent.customer.monitoring_status == CustomerMonitoringStatus.DURING_MONITORING:
                    monitoring_agent.monitor_customer()

            # Customer's behaviour in system
            for i, customer in enumerate(manager.system_customers):

                # Handling logs for tracked customer
                if i == self.tracked_customer_index:
                    if self.tracked_customer is None:
                        self.tracked_customer = manager.system_customers[self.tracked_customer_index]
                    if self.path_changed and self.tracked_customer.simulation_status == CustomerSimulationStatus.IN:
                        self.path_changed = False
                        # self.tracked_customer.display_tracked_path()  # Displaying tracked customer's current path


                # Customers in system, shopping
                if customer.simulation_status == CustomerSimulationStatus.IN \
                        and customer.monitoring_status == CustomerMonitoringStatus.AFTER_MONITORING \
                        and manager.scene.is_at_exit_node(customer.get_current_node()):  # Customer entering VQ's area

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

                # Customers doing shopping, walking through the graph
                else:
                    if customer.next_node_time > 0:
                        customer.update_next_node_time()
                    else:
                        node_index = len(customer.tracked_path)
                        if node_index < len(customer.path):
                            customer.append_transition(customer.path[node_index])
                            path_time = GeneratorUtil.generate_next_nodetime(manager.node_time_distribution[0], manager.node_time_distribution[1], manager.node_time_distribution[2])
                            customer.set_next_node_time(path_time)
                            customer.append_path_time(path_time)
                            customer.update_total_time(path_time)

                            if i == self.tracked_customer_index:
                                self.path_changed = True
                                self.file_logger.add_node(customer.path[node_index])

            # Customers waiting in queues
            self.console_logger.clean()
            self.file_logger.clean_histogram_file()
            self.console_logger.log_message("Time:"+str(current_time) + " [s] ")
            for queue_agent in manager.queues_agents:
                customers_queue = queue_agent.queue  # Queue (list)
                active_customers = queue_agent.get_active_waiting_customers()
                queue_agent.append_active_waiting_customers(active_customers)
                self.console_logger.log_queue(queue_agent.queue_type, active_customers)  # Logging to the console
                self.file_logger.log_histogram_data(queue_agent.queue_type, active_customers)  # Logging to the file being under listening

                for customer in customers_queue:
                    if customer.simulation_status == CustomerSimulationStatus.IN_QUEUE:
                        customer.set_is_first(True)  # Setting is_first flag in each queue
                        break                        # There can be only one customer in a queue with the flag set on the true

                for i in range(len(customers_queue)):
                    customer = customers_queue[i]
                    if customer.simulation_status == CustomerSimulationStatus.IN_QUEUE and customer.is_first and customer.service_time == 0:
                            manager.remove_customer(customer)  # Removing from the system and the simulation, setting status
                            customer.set_is_first(False)
                    else:
                        if customer.simulation_status == CustomerSimulationStatus.IN_QUEUE:
                                if customer.is_first:
                                    customer.update_service_time()
                                else:
                                    customer.update_waiting_time()

            time.sleep(1/self.speed_factor)
            current_time += 1

        self.collector.set_data_source(manager)
        out = self.collector.collect_simulation_data()
        return out
