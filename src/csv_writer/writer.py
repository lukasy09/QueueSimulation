import csv


class WriterCSV:
    header = ["Parameter", "Queue number", "Value"]  # CSV header row
    parameters = ["Number of people waiting clients in queue:", "Number of clients serviced in queue:", "Average waiting time in queue:"]

    # Configuration
    output = None  # The path to the output file
    delimiter = ","  # Delimiter

    # Objects
    writer = None

    """On the input we receive all collected data from the simulation.
        On the output we expect to get simulations results exported to a *.csv file"""

    def __init__(self, output):
        self.output = output

    def create_results(self, data):
        queues = data[0]
        general = data[1]
        mean_data = data[2]
        waiting_customers = data[3]
        serviced_customers = data[4]

        with open(self.output, 'w', newline='') as output_file:
            self.writer = csv.writer(output_file, delimiter=self.delimiter,
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
            self.write_header(general["time"])  # Writing header to the file

            # Waiting clients
            for i, queue in enumerate(queues):
                index = queue[0]
                queue_type = queue[1]

                first_col = ""
                if i == 0:
                    first_col = self.parameters[0]

                row = [first_col, "{}-{}".format(index, queue_type), waiting_customers[queue_type]]
                self.writer.writerow(row)

            # Serviced clients
            for i, queue in enumerate(queues):
                index = queue[0]
                queue_type = queue[1]

                first_col = ""
                if i == 0:
                    first_col = self.parameters[1]

                row = [first_col, "{}-{}".format(index, queue_type), serviced_customers[queue_type]]
                self.writer.writerow(row)

            # Serviced clients
            for i, queue in enumerate(queues):
                index = queue[0]
                queue_type = queue[1]

                first_col = ""
                if i == 0:
                    first_col = self.parameters[2]

                row = [first_col, "{}-{}".format(index, queue_type), mean_data[queue_type]]
                self.writer.writerow(row)


    """Writing the first row"""
    def write_header(self, time):
        row = []
        for attribute in self.header:
            row.append(attribute)
        self.writer.writerow(row)
