from System.simulation import Simulation
from SimulationDataCollector.collector import SimulationDataCollector
from Logger.console_logger import ConsoleLogger
from Logger.file_logger import FileLogger
from Loader.input_loader import SimulationInputLoader

# Objects cooperating with simulation
console_logger = ConsoleLogger()
file_logger = FileLogger()
collector = SimulationDataCollector()

simulation_config = SimulationInputLoader.get_config()  # Loading config

simulation = Simulation(simulation_config, console_logger, file_logger, collector)
# Simulation invoke/start
out = simulation.run()
# Simulation end
file_logger.log_json_output(out)