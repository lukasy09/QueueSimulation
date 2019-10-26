# Imports
from src.System.Agents.GeneratorAgent.agent import GeneratorAgent
from src.System.Agents.ManagingAgent.agent import ManagingAgent

# Run Simulation
manager = ManagingAgent()
gen = GeneratorAgent()

customer = gen.generate_customer()
print(customer)