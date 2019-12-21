import xlwt
from xlwt import Workbook
import json
from datetime import datetime


class XLSReportGenerator:

    def __init__(self, in_path, out_path):
        self.wb = Workbook()
        self.sheets = []
        self.output_path = out_path
        self.input_path = in_path

    def add_sheet(self, name):
        sheet1 = self.wb.add_sheet(name)
        self.sheets.append(sheet1)

    def write_statistics(self, stats):
        for i, key in enumerate(stats.keys()):
            self.sheets[0].write(0, i, key)
            self.sheets[0].write(1, i, stats[key])

    def write_queues(self, queues):
        for i, queue in enumerate(queues):
            queue_col = i + 1
            self.sheets[1].write(0, queue_col, queue["type"])
            data_row = 1
            for j, key in enumerate(queue.keys()):
                if key not in ["type"]:
                    if i == 0:
                        self.sheets[1].write(data_row, 0, key)
                    self.sheets[1].write(data_row, queue_col, str(queue[key]))
                    data_row += 1

    def write_customers(self, customers):
        for i, customer in enumerate(customers):
            for j, key in enumerate(customer.keys()):
                if i == 0:
                    self.sheets[2].write(0, j, key)

                self.sheets[2].write(i+1, j, str(customer[key]))

    def build_report(self):
        with open(self.input_path, 'r') as input_filedata:
            # Parsing raw data from json
            data = json.load(input_filedata)
            # Creating sheets
            self.add_sheet('General statistics')
            self.add_sheet("Queues")
            self.add_sheet("Customers")

            # Writing data
            stats = data['statistics']
            self.write_statistics(stats)

            queues = data['queues']
            self.write_queues(queues)

            customers = data['customers']
            self.write_customers(customers)


        self.submit()

    def submit(self):
        final_path = "{}{}".format(self.output_path, self.generate_report_name())
        self.wb.save(final_path)

    def generate_report_name(self):
        now = datetime.now()
        return "report_{}.xls".format(str(now.strftime("%H-%M-%S")))


# gen = XLSReportGenerator("../../out/output.json", "./")
# gen.build_report()
