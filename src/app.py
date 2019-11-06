# Imports
from src.System.Agents.ManagingAgent.agent import ManagingAgent

# Run Simulation

# Setting up initials
manager = ManagingAgent()
manager.setup_initial_state()

customer_pool = manager.customer_pool

time = 0
while time < manager.simulation_time:
    # Is new customer in our system?


    time += 1