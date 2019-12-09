class FileLogger:

    DATA_DESTINATION = ".//data/tracked_customer.log"

    def __init__(self):
        file = open(self.DATA_DESTINATION, "a+")
        file.truncate(0)
        file.write("0,0\n")
        file.close()

    def add_node(self, node):
        self.log_position(node[0], node[1])


    def log_position(self, x, y):
        row = "{},{}\n".format(str(x), str(y))
        file = open(self.DATA_DESTINATION, "a+")
        file.write(row)
        file.close()