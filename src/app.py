from System.simulation import Simulation
from SimulationDataCollector.collector import SimulationDataCollector
from csv_writer.writer import WriterCSV
from Logger.console_logger import ConsoleLogger
# writer = WriterCSV("../sim_config/result.csv")  # Processing the gained data and creating file resource

logger = ConsoleLogger()
simulation = Simulation(logger)

# Simulation invoke/start
simulation.run()
# Simulation end
