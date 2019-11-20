from System.simulation import Simulation
from SimulationDataCollector.collector import SimulationDataCollector


collector = SimulationDataCollector()

simulation = Simulation(collector)

# Simulation invoke/start
simulation.run()
# Simulation end

collector.log_final_state()

