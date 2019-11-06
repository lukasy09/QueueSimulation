from src.System.Agents.GeneratorAgent.Agent import GeneratorAgent
from src.System.Agents.ManagingAgent.SimulationMode import Traffic


class ManagingAgent:

    """Simulation constants"""
    simulation_time = 3600  # time unit e.g seconds, minutes etc.
    pool_size = 1000
    defaultTraffic = Traffic.MEDIUM
    customer_pool = []
    queues = []

    def __init__(self):
        self.gen = GeneratorAgent()
        pass

    # Creating customer pool, queues
    def setup_initial_state(self):
        self.customer_pool = self.gen.generate_population(self.pool_size)


    def run_simulation(self):
        pass
