import math

class Edge(object):
    def __init__(self, source, sink, w = 0):
        self.source = source
        self.sink = sink
        self.weight = w


    def __str__(self):
        return "{0} -> {1} : {2}".format(self.source, self.sink, self.weight)

    def __lt__(self, other):
        return (self.weight > other.weight) - (self.weight < other.weight)


class Vertex(object):
    def __init__(self):
        self.edges = []
        self.parent = None

    def AddEdge(self, vertex, w = 0):
        self.edges.append(Edge(self, vertex, w))


class Graph(object):
    def __init__(self):
        self.INFINITY = math.inf
        self.vertices = []

    def AddVertex(self, vertex):
        self.vertices.append(vertex)

    def AddEdge(self, source, sink):
        pass

    def BFS(self, source):
        pass