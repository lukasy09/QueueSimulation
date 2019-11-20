from System.Agents.ManagingAgent.customer_simulation_status import CustomerSimulationStatus


class SimulationDataCollector:

    def __init__(self):
        self.manager = None

    def set_data_source(self, manager):
        self.manager = manager

    def collect_data(self):
        queue_data = self.extract_queue_data()
        print(queue_data)



    def extract_queue_data(self):
        manager = self.manager

        queues_mean_waiting_time = dict()
        for i in range(len(manager.queues_agents)):
            queue_agent = manager.queues_agents[i]
            queue_waiting_time_sum = 0
            queue_customer_number = len(queue_agent.queue)  # The number of all customers that came through a given queue in whole simulation time
            for unit in queue_agent.queue:
                queue_waiting_time_sum += unit.waiting_time

            queues_mean_waiting_time["{} {}".format(queue_agent.queue_type, queue_agent.index)] = round(queue_waiting_time_sum/queue_customer_number)

        return queues_mean_waiting_time


    def log_final_state(self):
        manager = self.manager
        self.collect_data()

        # print(len(manager.system_customers), "<- Number of customers still in system")
        # c = 0
        # for customer in manager.system_customers:
        #     if customer.simulation_status == CustomerSimulationStatus.IN:
        #         c += 1
        # print(c, "<- Number of customers in shopping")
        # print(len(manager.virtual_queue_agent.virtual_queue), "<- Customers in VQ")
        # print(len(manager.removed_customers), "<- Removed customers")

