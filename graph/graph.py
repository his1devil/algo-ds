#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现邻接表
"""
class Vertex(object):
    """
    保存各个vertex的连接信息字典
    """
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

    def getConnecteds(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, start, end, weight=0):
        if start not in self.vertList:
            self.addVertex(start)
        if end not in self.vertList:
            self.addVertex(end)
        self.vertList[start].addNeighbor(self.vertList[end], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.verList.values())
