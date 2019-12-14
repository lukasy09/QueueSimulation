import matplotlib.pyplot as plt
import matplotlib.animation as animation

queues = []
labels = []
values = []
figures = []
axes = []
anims = []
pull_data = open("../data/queue_usage.log", "r").read()
data_array = pull_data.split('\n')


def animate(j):
    pull_data = open("../data/queue_usage.log", "r").read()
    data_array = pull_data.split('\n')
    values = []
    for i, el in enumerate(data_array):
        if el.find(":") > 0:
            split = el.split(":")
            label = split[0]
            labels.append(label)
            value = split[1].split(",")
            new_val = []
            for val in value:
                new_val.append(int(val))
            values.append(new_val)

    for i, figure in enumerate(axes):
        if len(values) == len(axes):
            axes[i].clear()
            axes[i].plot(values[i])
            axes[i].set_xlabel("Time [s]")
            axes[i].set_ylabel("Number of customers")
            axes[i].set_title(labels[i])


for i in range(len(data_array)):
    el = data_array[i]
    if el.find(":") > 0:
        fig = plt.figure(i + 1)
        figures.append(fig)

for i in range(len(figures)):
    anim = animation.FuncAnimation(figures[i], animate, interval=2000)
    anims.append(anim)
    ax = figures[i].add_subplot(111)
    axes.append(ax)
plt.show()
