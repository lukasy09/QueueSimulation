import json


class FileLogger:

    TRACKED_DATA_DESTINATION = "./data/tracked_customer.log"
    HISTOGRAM_DATA_DESTINATION = "./data/histogram.log"
    QUEUES_DATA_DESTINATION = "./data/queue_usage.log"
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

    def log_histogram_data(self, type_, value):
        row = "{}:{}\n".format(str(type_), str(value))
        file = open(self.HISTOGRAM_DATA_DESTINATION, "a+")
        file.write(row)
        file.close()

    def log_json_output(self, data):
        with open(self.OUTPUT_DATA_DESTINATIONS, 'w+') as outfile:
            outfile.truncate(0)
            json.dump(data, outfile, indent=2)

    def log_queues_history(self, data):
        queue_type = data["type"]
        values = data["values"]
        with open(self.QUEUES_DATA_DESTINATION, 'a+') as file:
            file.write("{}:".format(queue_type))
            for i, val in enumerate(values):
                file.write("{}".format(int(val)))
                if i != len(values) - 1:
                    file.write(",")
            file.write("\n")

    def clean_histogram_file(self):
        self.truncate(self.HISTOGRAM_DATA_DESTINATION)

    def clean_queues_file(self):
        self.truncate(self.QUEUES_DATA_DESTINATION)

    def truncate(self, path):
        file = open(path, "w+")
        file.truncate(0)