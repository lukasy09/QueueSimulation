class Queue:
    index = None
    type = None
    customers = []

    def __init__(self, index, queue_type):
        self.index = index
        self.type = queue_type

    def __str__(self):
        return "Index: {}, type: {}".format(self.index, self.type)
