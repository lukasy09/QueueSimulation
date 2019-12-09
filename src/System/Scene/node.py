"""Representing a single node in the scene graph"""


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.connections = []  # All possible ways to leave the node
        self.is_exit = False
        self.is_start = False



    def __str__(self):
        return "Node: ({}, {})".format(self.row, self.col)