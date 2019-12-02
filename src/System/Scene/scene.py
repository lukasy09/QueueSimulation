from System.Scene.node import Node

"""Representing the shop area"""


class Scene:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.graph = []


    def build(self):
        for i in range(self.height):
            nodes_in_row = []
            for j in range(0, self.width):
                node = Node(i, j)
                nodes_in_row.append(node)

            self.graph.append(nodes_in_row)