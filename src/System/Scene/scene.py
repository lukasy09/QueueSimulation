from System.Scene.node import Node

"""Representing the shop area"""


class Scene:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.graph = []


    def create_nodes(self):
        for i in range(self.height):
            nodes_in_row = []
            for j in range(0, self.width):
                node = Node(i, j)
                nodes_in_row.append(node)
            self.graph.append(nodes_in_row)


    def build_connections(self):
        for i in range(len(self.graph)):
            graph_row = self.graph[i]
            for j in range(len(graph_row)):
                node = self.graph[i][j]
                if i == 0:  # The first ROW
                    if j == 0:  # Handling the FIRST ELEMENT in the FIRST ROW
                        node.connections.append(self.graph[i][j+1])
                        node.connections.append(self.graph[i+1][j+1])
                        node.connections.append(self.graph[i+1][j])
                        node.exit_pointer = self.graph[i+1][j+1]
                        node.is_start = True

                    elif j == self.width - 1:  # Handling the LAST ELEMENT in the FIRST ROW
                        node.connections.append(self.graph[i+1][j])
                        node.connections.append(self.graph[i+1][j-1])
                        node.connections.append(self.graph[i][j-1])
                        node.exit_pointer = self.graph[i + 1][j]

                    else:
                        node.connections.append(self.graph[i][j - 1])
                        node.connections.append(self.graph[i][j + 1])
                        node.connections.append(self.graph[i+1][j + 1])
                        node.connections.append(self.graph[i+1][j])
                        node.connections.append(self.graph[i+1][j-1])
                        node.exit_pointer = self.graph[i + 1][j + 1]

                elif i == self.height - 1:  # The last row
                    if j == 0:  # Handling the FIRST ELEMENT in the FIRST ROW
                        node.connections.append(self.graph[i - 1][j])
                        node.connections.append(self.graph[i - 1][j + 1])
                        node.connections.append(self.graph[i][j + 1])
                        node.exit_pointer = self.graph[i][j + 1]


                    elif j == self.width - 1:  # Handling the LAST ELEMENT in the LAST ROW -> END
                        node.is_exit = True


                    else:
                        node.connections.append(self.graph[i][j - 1])
                        node.connections.append(self.graph[i][j + 1])
                        node.connections.append(self.graph[i - 1][j - 1])
                        node.connections.append(self.graph[i - 1][j])
                        node.connections.append(self.graph[i - 1][j + 1])
                        node.exit_pointer = self.graph[i][j + 1]



                else:  # The middle rows

                    if j == 0:
                        node.connections.append(self.graph[i-1][j])
                        node.connections.append(self.graph[i-1][j+1])
                        node.connections.append(self.graph[i][j+1])
                        node.connections.append(self.graph[i+1][j+1])
                        node.connections.append(self.graph[i+1][j])
                        node.exit_pointer = self.graph[i + 1][j + 1]


                    elif j == self.width - 1:
                        node.connections.append(self.graph[i - 1][j])
                        node.connections.append(self.graph[i + 1][j])
                        node.connections.append(self.graph[i + 1][j - 1])
                        node.connections.append(self.graph[i][j - 1])
                        node.connections.append(self.graph[i-1][j - 1])
                        node.exit_pointer = self.graph[i + 1][j]


                    else:
                        node.connections.append(self.graph[i - 1][j])
                        node.connections.append(self.graph[i - 1][j+1])
                        node.connections.append(self.graph[i][j+1])
                        node.connections.append(self.graph[i + 1][j+1])
                        node.connections.append(self.graph[i + 1][j])
                        node.connections.append(self.graph[i + 1][j - 1])
                        node.connections.append(self.graph[i][j - 1])
                        node.connections.append(self.graph[i - 1][j - 1])
                        node.exit_pointer = self.graph[i + 1][j + 1]

