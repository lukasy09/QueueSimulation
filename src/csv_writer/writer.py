import csv


class WriterCSV:
    header = ["Parameter", "Queue number", "Simulation time"]  # CSV header row

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
        general = data[0]

        with open(self.output, 'w', newline='') as output_file:
            self.writer = csv.writer(output_file, delimiter=self.delimiter,
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)

            self.write_header(general["time"])  # Writing header to the file


    """Writing the first row"""
    def write_header(self, time):
        row = []
        for attribute in self.header:
            if attribute == self.header[2]:
                attribute += " {}".format(str(time))
            row.append(attribute)
        self.writer.writerow(row)
