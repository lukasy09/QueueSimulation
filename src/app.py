# Imports
from System.Agents.ManagingAgent.agent import ManagingAgent
from System.Agents.ManagingAgent.simulation_mode import Traffic

# Run Simulation

# Simulation parameters(if not using the default ones)
traffic = Traffic.HIGH

# Setting up initials
manager = ManagingAgent(traffic=traffic)
manager.setup_initial_state()  # Creating customer pool & queues

customer_pool = manager.customer_pool

# Start
time = 0  # Variable holds the current time of simulation


# while time < manager.simulation_time:
#     # Is new customer in our system?
#
#     break
#
#
#     time += 1