# Code taken and slightly-modified from GeeksforGeeks

import sys

class Graph():

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]
    
    def printSol(self, dist):
        print("Vertex source distance")
        for node in range(self.vertices):
            print(node, dist[node])
    def minDistance(self, dis, shortestPath):
        min = sys.maxsize
        for v in range(self.vertices):
            if dis[v] < min and shortestPath[v] == False:
                min = dis[v]
                min_index = v
        return min_index
    def dijkstras(self, source):
        dist = [sys.maxsize] * self.vertices
        dist[source] = 0
        shortestPath = [False] * self.vertices

        for c in range(self.vertices):
            u = self.minDistance(dist, shortestPath)
            shortestPath[u] = True
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and shortestPath[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSol(dist)


# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
g.dijkstras(0)