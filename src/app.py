from System.simulation import Simulation
from SimulationDataCollector.collector import SimulationDataCollector
from csv_writer.writer import WriterCSV

collector = SimulationDataCollector()  # Collecting data from simulation
writer = WriterCSV("../results/result.csv")  # Processing the gained data and creating file resource

simulation = Simulation(collector)

# Simulation invoke/start
simulation.run()
# Simulation end

data = collector.collect_data()

writer.create_results(data)

