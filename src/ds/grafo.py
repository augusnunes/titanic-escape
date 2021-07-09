import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.


class Grafo:
    def __init__(self, names, edges):
        self.names = np.array(names)
        self.edges = np.array(edges)
    
    def procura_vizinho(self, node):
        return self.edges[node,:], self.names[self.edges[node,:]]