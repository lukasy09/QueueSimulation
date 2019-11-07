from System.Actors.Queue.queue import Queue
from System.Agents.GeneratorAgent.agent import GeneratorAgent
from System.Agents.ManagingAgent.queue_types import QueueType
from System.Agents.ManagingAgent.simulation_mode import Traffic


class ManagingAgent:

    # Simulation constant
    simulation_time = 3600  # time unit e.g seconds, minutes etc.
    pool_size = 1000
    defaultTraffic = Traffic.MEDIUM

    # queue_type: count
    queues_config = {
        QueueType.NORMAL: 2,
        QueueType.PRIVILEGED: 1,
        QueueType.MOST_PRIVILEGED: 1
    }

    # Pseudo-random client generation periods
    customer_period = {
        Traffic.VERY_HIGH: (10, 60),
        Traffic.HIGH: (10, 100),
        Traffic.MEDIUM: (30, 180),
        Traffic.LOW: (30, 600),
        Traffic.VERY_LOW: (50, 800)
    }

    # """Simulation variables
    customer_pool = []
    queues = []
    traffic = Traffic.MEDIUM

    def __init__(self, traffic=defaultTraffic):
        self.gen = GeneratorAgent()
        self.traffic = traffic

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
