# Imports
from System.Agents.ManagingAgent.agent import ManagingAgent
from System.Agents.ManagingAgent.simulation_mode import Traffic
from Utils.GaussianUtil import GaussianUtil

# Simulation parameters(if not using the default ones)
traffic = Traffic.HIGH

#GaussianUtil
gaussianUtil = GaussianUtil();

# Setting up initials
manager = ManagingAgent(traffic=traffic)
manager.setup_initial_state()  # Creating customer pool & queues

customer_pool = manager.customer_pool # All available customers

# Start
time = 0  # Variable holds the current time of simulation
appear_time = gaussianUtil.generate_integer_in_range(manager.customer_period_range[0], manager.customer_period_range[1] + 1)

count = 0
while time < manager.simulation_time:
    # Is new customer in our system?
    if time == appear_time:
        appear_time = gaussianUtil.generate_integer_in_range(manager.customer_period_range[0] + time,manager.customer_period_range[1] + time + 1)

        count += 1

    time += 1

print(count)