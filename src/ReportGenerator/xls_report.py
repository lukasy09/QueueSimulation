import xlwt
from xlwt import Workbook
import json


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
                if key not in ["type" ,"queue", "active_customers_per_time"]:
                    if i == 0:
                        self.sheets[1].write(data_row, 0, key)
                    self.sheets[1].write(data_row, queue_col, str(queue[key]))
                    data_row += 1

    def build_report(self):
        with open(self.input_path, 'r') as input_filedata:
            # Parsing raw data from json
            data = json.load(input_filedata)
            # Creating sheets
            self.add_sheet('General statistics')
            self.add_sheet("Queues")

            # Writing data
            stats = data['statistics']
            self.write_statistics(stats)
            queues = data['queues']
            self.write_queues(queues)
        self.submit()


    def submit(self):
        self.wb.save(self.output_path)


gen = XLSReportGenerator("../../out/output.json", "./a.xls")
gen.build_report()
