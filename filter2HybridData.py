#!/usr/bin/python

import sys
sys.path.append("/Users/jasmine/python/python-graph/core")
from pygraph.classes.graph import graph
from strip2HybridData import *

#input is graph/bait name, return core graph edges
def filter2HybridDataEdgesAnd(graphName):

    edges = strip2HybridDataEdges()
    newEdges = []
    ap = []

    data = open("ProcessedAPData.txt", 'r')

    for line in data:
        line = line.rstrip()
        lineS = line.split("\t")
        if lineS[0] == graphName:
            ap.append(lineS[1])

    for edge in edges:
        #check node 1
        checkNode1 = False
        for name in edge[0]:
            if name in ap:
                checkNode1 = True
                break

        #check node 2
        checkNode2 = False
        for name in edge[1]:
            if name in ap:
                checkNode2 = True
                break

        if checkNode1 and checkNode2:
            newEdges.append([edge[0][0], edge[1][0]])

    data.close()

    return newEdges

#input is graph/bait name, return extended graph edges
def filter2HybridDataEdgesOr(graphName):

    edges = strip2HybridDataEdges()
    newEdges = []
    ap = []

    data = open("ProcessedAPData.txt", 'r')

    for line in data:
        line = line.rstrip()
        lineS = line.split("\t")
        if lineS[0] == graphName:
            ap.append(lineS[1])

    for edge in edges:
        #check node 1
        checkNode1 = False
        for name in edge[0]:
            if name in ap:
                checkNode1 = True
                break

        #check node 2
        checkNode2 = False
        for name in edge[1]:
            if name in ap:
                checkNode2 = True
                break

        if checkNode1 or checkNode2:
            newEdges.append([edge[0][0], edge[1][0]])

    data.close()

    return newEdges

#input is graph/bait name, return all nodes appearing in AP data
def allAPDataNodes(graphName):
    ap = []
    data = open("ProcessedAPData.txt", 'r')
    for line in data:
        line = line.rstrip()
        lineS = line.split("\t")
        if lineS[0] == graphName:
            ap.append(lineS[1])
    return ap

#input is graph/bait name, return graph nodes
def filter2HybridDataNodes(graphName):

    nodes = strip2HybridDataNodes()
    newNodes = []
    ap = []

    data = open("ProcessedAPData.txt", 'r')

    for line in data:
        line = line.rstrip()
        lineS = line.split("\t")
        if lineS[0] == graphName:
            ap.append(lineS[1])

    for node in nodes:
        if node in ap:
            newNodes.append(node)

    data.close()

    return newNodes

#make graph from graph/bait name and core vs. extended
def makeOverlayGraph(graphName, l_strict):
    if l_strict:
        return makeOverlayGraphAnd(graphName)
    return makeOverlayGraphOr(graphName)

#make core graph from graph/bait name
def makeOverlayGraphAnd(graphName):
    return makeGraphFromLists(filter2HybridDataEdgesAnd(graphName), filter2HybridDataNodes(graphName))

#make extended graph from graph/bait name
def makeOverlayGraphOr(graphName):
    return makeGraphFromLists(filter2HybridDataEdgesOr(graphName), filter2HybridDataNodes(graphName))

#build graph from lists of edges, nodes
def makeGraphFromLists(edges, nodes):
    gr = graph()

    for node in nodes:
        if not gr.has_node(node):
            gr.add_nodes([node])

    for edge in edges:
        if not gr.has_node(edge[0]):
            gr.add_nodes([edge[0]])
        if not gr.has_node(edge[1]):
            gr.add_nodes([edge[1]])
        if not gr.has_edge((edge[0],edge[1])):
            gr.add_edge((edge[0],edge[1]))

    for node in gr.nodes():
        if gr.has_edge((node, node)):
            gr.del_edge((node, node))
        if len(gr.neighbors(node)) == 0:
            gr.del_node(node)

    return gr

#print graphs in format requested by Suzanne
def printSuzanneFormat(gr, graphName):
    out = open(graphName+'.txt', 'w')
    for node in gr.nodes():
        out.write(node)
        out.write("\n")
    out.write("ENDV\n")
    for node in gr.nodes():
        out.write(node)
        out.write(" ")
        for node1 in gr.neighbors(node):
            out.write(node1)
            out.write(" ")
        out.write("*\n")
    out.write("ENDE\n")
    out.close()


