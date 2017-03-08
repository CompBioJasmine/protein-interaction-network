#!/usr/bin/python

import sys
sys.path.append("/Users/jasmine/python/python-graph/core")
from pygraph.classes.graph import graph
from filter2HybridData import *
from hypergeometric import *

#returns a graph of entire protein interaction network (from BioGRID, or for
#any list of edges and nodes)
def makeUniverseGraph():
    newEdges = []
    newNodes = []
    edges = strip2HybridDataEdges()
    nodes = strip2HybridDataNodes()
    for edge in edges:
        newEdges.append([edge[0][0], edge[1][0]])
    for node in nodes:
        if node[0] not in newNodes:
            newNodes.append(node[0])
    return makeGraphFromLists(newEdges, newNodes)

#inputs are core graph and extended graph, returns edges that connect them
def makeConnectingEdgeList(grA, grO):
    newEdges = []
    A_edges = grA.edges()
    O_edges = grO.edges()
    for O_edge in O_edges:
        if O_edge not in A_edges:
            newEdges.append(O_edge)

    return newEdges

#inputs are core graph and extended graph, returns nodes that have a connecting
#edge but are not in the core graph
def connectingNodes(grA, grO):
    newNodes = []
    A_nodes = grA.nodes()
    O_nodes = grO.nodes()
    for node in O_nodes:
        if node not in A_nodes:
            newNodes.append(node)

    return newNodes

#inputs are core graph and extended graph, returns intersection
def findIntersection(gr, node1, node2):
    list1 = gr.neighbors(node1)
    list2 = gr.neighbors(node2)
    intersection = 0
    for node in list1:
        if node in list2:
            intersection = intersection + 1
    return intersection


