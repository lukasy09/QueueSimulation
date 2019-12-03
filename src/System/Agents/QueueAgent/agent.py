from System.Agents.QueueAgent.queue_types import QueueType



class QueueAgent:

    # queue identifier
    index = None

    # type of the related queue to the agent
    queue_type = QueueType.NORMAL  # NORMAL is the default one
    expected_waiting_time = 0

    def __init__(self, index):
        self.index = index
        self.queue = []

    def set_queue_type(self, queue_type):
        self.queue_type = queue_type

    def accept(self, customer):
        self.queue.append(customer)

    def remove_head(self):
        self.queue.remove(self.queue[0])

    def print_queue(self):
        for cus in self.queue:
            print(cus.next_node_time)
            print(cus.path)

    def __str__(self):
        return "QueueAgent: Index: {}, type: {}, number of people waiting: {}"\
                .format(self.index, self.queue_type, len(self.queue))