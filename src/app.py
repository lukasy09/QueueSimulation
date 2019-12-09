from System.simulation import Simulation
from SimulationDataCollector.collector import SimulationDataCollector
from csv_writer.writer import WriterCSV
from Logger.console_logger import ConsoleLogger
from Logger.file_logger import FileLogger
# writer = WriterCSV("../sim_config/result.csv")  # Processing the gained data and creating file resource

console_logger = ConsoleLogger()
file_logger = FileLogger()
simulation = Simulation(console_logger, file_logger)

# Simulation invoke/start
simulation.run()
# Simulation end
