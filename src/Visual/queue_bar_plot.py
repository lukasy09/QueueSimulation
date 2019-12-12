import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation


# noinspection PyShadowingNames
class VisualBarPlot:

    DATA_SOURCE = "../data/histogram.log"

    def __init__(self):
        self.figure = plt.figure()
        self.ax1 = self.figure.add_subplot(1, 1, 1)


    def track_histogram_changes(self):
        ani = animation.FuncAnimation(self.figure, self.listen, interval=100)
        plt.show()

    def listen(self, i):
        labels, values = self.read_data()
        self.ax1.clear()
        indexes = np.arange(len(labels))
        plt.bar(indexes, values, color=(0.2, 0.4, 0.6, 0.6))
        plt.xlabel('Queues', fontsize=15)
        plt.ylabel('Count', fontsize=15)
        plt.xticks(indexes, labels, fontsize=15, rotation=10)
        plt.title('Queue usage through time')

    def read_data(self):
        pull_data = open(self.DATA_SOURCE, "r").read()
        data_array = pull_data.split('\n')
        labels = []
        values = []
        for el in data_array:
            if el.find(":") > 0:
                split = el.split(":")
                label = split[0]
                value = int(split[1])
                labels.append(label)
                values.append(value)

        return labels, values


q = VisualBarPlot()
q.track_histogram_changes()