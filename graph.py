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

    def __eq__(self, other):
        return True if self.source == other.source and self.sink == other.sink and self.weight == other.weight else False


class Graph(object):
    def __init__(self):
        self.INFINITY = math.inf
        self.vertices = []

    def AddVertex(self, vertex):
        self.vertices.append(vertex)

    def AddEdge(self, source, sink):
        sour = None
        sin = None


    def BFS(self, source):
        pass