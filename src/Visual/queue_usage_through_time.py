import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

queues = []
labels = []
values = []
figures = []
axes = []
anims = []
pull_data = open("../data/queue_usage.log", "r").read()
data_array = pull_data.split('\n')
fig, axes = plt.subplots(2,2, figsize=(8,8))
fig

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

    counter = 0
    for i in range(len(axes)):
        for j in range(len(axes[i])):
            if (len(values) == 4):
                axes[i, j].clear()
                axes[i, j].plot(values[counter])
                # axes[i, j].set_xlabel("Time [s]")
                axes[i, j].set_ylabel("Number of customers")
                axes[i, j].set_title(labels[counter])
                counter +=1


anim = animation.FuncAnimation(fig, func=animate, interval=100)
plt.show()
