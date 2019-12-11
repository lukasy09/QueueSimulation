import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation
plt.ioff()


class VisualGraph:

    DATA_SOURCE = "../data/tracked_customer.log"

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)

    def visualise_scene(self):
        color = ""
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 and j == 0:
                    color = "red"
                elif i == self.height-1 and j == self.width - 1:
                    color = "black"
                else:
                    color = "blue"
                self.ax1.scatter(i, j, s=80, color=color)
        plt.grid(True)


    def track_path(self):
        ani = animation.FuncAnimation(self.fig, self.listen, interval=1000)
        plt.show()

    def listen(self, i):
        xar, yar = self.read_data()
        self.ax1.clear()
        self.visualise_scene()
        self.ax1.plot(xar, yar)

        last_x = len(xar)-1
        last_y = len(yar)-1

        if last_x != self.width-1 or last_y != self.height-1:
            self.ax1.scatter(xar[last_x], yar[last_y], s=80, color="yellow")

    def read_data(self):
        pull_data = open(self.DATA_SOURCE, "r").read()
        data_array = pull_data.split('\n')
        xar = []
        yar = []
        for eachLine in data_array:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xar.append(int(x))
                yar.append(int(y))
        return xar, yar


# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
#
# def animate(i):
#     pullData = open("../data/tracked_customer.log","r").read()
#     dataArray = pullData.split('\n')
#     xar = []
#     yar = []
#     for eachLine in dataArray:
#         if len(eachLine)>1:
#             x,y = eachLine.split(',')
#             xar.append(int(x))
#             yar.append(int(y))
#     ax1.clear()
#     ax1.plot(xar,yar)
# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()



graph = VisualGraph(6, 4)
graph.track_path()
# # path = [0, 1, 2]
# # path_2 = [0, 0, 1]
# # g.visualise_path(path, path_2)
# # path = [0, 1, 2, 1]
# # path_2 = [0, 0, 1, 1]
# # g.visualise_path(path, path_2)
# # # plt.plot(path, path_2)
# # # plt.show()