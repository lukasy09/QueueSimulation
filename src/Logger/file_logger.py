import json


class FileLogger:

    TRACKED_DATA_DESTINATION = "./data/tracked_customer.log"
    OUTPUT_DATA_DESTINATIONS = "../out/output.json"


    def __init__(self, active=True):
        file = open(self.TRACKED_DATA_DESTINATION, "a+")
        file.truncate(0)
        file.write("0,0\n")
        file.close()

    def add_node(self, node):
        self.log_position(node[0], node[1])


    def log_position(self, x, y):
        row = "{},{}\n".format(str(x), str(y))
        file = open(self.TRACKED_DATA_DESTINATION, "a+")
        file.write(row)
        file.close()

    def log_json_output(self, data):
        with open(self.OUTPUT_DATA_DESTINATIONS, 'w+') as outfile:
            outfile.truncate(0)
            json.dump(data, outfile, indent=2)