import json


class SimulationInputLoader:

    CONFIG_PATH = "../in/config.json"  # Relative path from app.py

    @classmethod
    def get_config(cls):
        with open(cls.CONFIG_PATH, 'r') as config_file:
            return json.load(config_file)