from System.Scene.node import Node
import random

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
                        node.is_start = True

                    elif j == self.width - 1:  # Handling the LAST ELEMENT in the FIRST ROW
                        node.connections.append(self.graph[i+1][j])
                        node.connections.append(self.graph[i+1][j-1])
                        node.connections.append(self.graph[i][j-1])

                    else:
                        node.connections.append(self.graph[i][j - 1])
                        node.connections.append(self.graph[i][j + 1])
                        node.connections.append(self.graph[i+1][j + 1])
                        node.connections.append(self.graph[i+1][j])
                        node.connections.append(self.graph[i+1][j-1])

                elif i == self.height - 1:  # The last row
                    if j == 0:  # Handling the FIRST ELEMENT in the FIRST ROW
                        node.connections.append(self.graph[i - 1][j])
                        node.connections.append(self.graph[i - 1][j + 1])
                        node.connections.append(self.graph[i][j + 1])


                    elif j == self.width - 1:  # Handling the LAST ELEMENT in the LAST ROW -> END
                        node.is_exit = True

                    else:
                        node.connections.append(self.graph[i][j - 1])
                        node.connections.append(self.graph[i][j + 1])
                        node.connections.append(self.graph[i - 1][j - 1])
                        node.connections.append(self.graph[i - 1][j])
                        node.connections.append(self.graph[i - 1][j + 1])



                else:  # The middle rows

                    if j == 0:
                        node.connections.append(self.graph[i-1][j])
                        node.connections.append(self.graph[i-1][j+1])
                        node.connections.append(self.graph[i][j+1])
                        node.connections.append(self.graph[i+1][j+1])
                        node.connections.append(self.graph[i+1][j])


                    elif j == self.width - 1:
                        node.connections.append(self.graph[i - 1][j])
                        node.connections.append(self.graph[i + 1][j])
                        node.connections.append(self.graph[i + 1][j - 1])
                        node.connections.append(self.graph[i][j - 1])
                        node.connections.append(self.graph[i-1][j - 1])


                    else:
                        node.connections.append(self.graph[i - 1][j])
                        node.connections.append(self.graph[i - 1][j+1])
                        node.connections.append(self.graph[i][j+1])
                        node.connections.append(self.graph[i + 1][j+1])
                        node.connections.append(self.graph[i + 1][j])
                        node.connections.append(self.graph[i + 1][j - 1])
                        node.connections.append(self.graph[i][j - 1])
                        node.connections.append(self.graph[i - 1][j - 1])

    def get_random_neighbor_cords(self, cords):
        node = self.graph[cords[0]][cords[1]]
        random_neighbor = random.choice(node.connections)
        return random_neighbor.row, random_neighbor.col

    def get_node(self, cords):
        return self.graph[cords[0]][cords[1]]
        
    def generate_path_to_escape_node(self, cords):
        current_cords = [cords[0], cords[1]]
        path_to_escape = []

        while current_cords[0] < (self.height - 1) or current_cords[1] < (self.width - 1):
            if current_cords[0] < (self.height - 1):
                current_cords[0] += 1
            if (self.width - 1) > current_cords[1]:
                current_cords[1] += 1

            path_to_escape.append((current_cords[0], current_cords[1]))
        
        return path_to_escape

    def get_exit_coords(self):
        return self.height - 1, self.width - 1

    def is_at_exit_node(self, position):
        exit_node_position = self.get_exit_coords()
        return exit_node_position[0] == position[0] and exit_node_position[1] == position[1]

    def __str__(self):
        out = ""
        for row in self.graph:
            for i in row:
                out += str(i) + "|"
            out += "\n"
        return out
