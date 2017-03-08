#!/usr/bin/python
import re

#Strip data to aliases and altids, create list of edges
def strip2HybridDataEdges():
    edges = []
    
    data = open("human2hybrid.txt", 'r')
    out = open("strippedhuman2hybrid.txt", 'w')

    for line in data:
        list1 = []
        list2 = []
        lineS = line.split("\t")

        # add the altids

        altid1 = lineS[2].split("|")
        for altid in altid1:
            altid1r = re.match("entrez gene/locuslink:(.+)", altid)
            list1.append(altid1r.group(1))

        altid2 = lineS[3].split("|")
        for altid in altid2:
            altid2r = re.match("entrez gene/locuslink:(.+)", altid)
            list2.append(altid2r.group(1))

        # add the aliases
    
        aliases1 = lineS[4].split("|")
        for alias in aliases1:
            aliases1r = re.match("entrez gene/locuslink:(.+)\\(", alias)
            if aliases1r is not None:
                list1.append(aliases1r.group(1))
        
        aliases2 = lineS[5].split("|")
        for alias in aliases2:
            aliases2r = re.match("entrez gene/locuslink:(.+)\\(", alias)
            if aliases2r is not None:
                list2.append(aliases2r.group(1))

        # store lists in edges array
        edges.append([list1, list2])

        # print results to a file

        for s in list1:
            out.write(s + "\t")
        out.write("\n")

        for s in list2:
            out.write(s + "\t")
        out.write("\n")
        
    data.close()
    out.close()

    return edges

#Strip data to aliases and altids, create list of nodes
def strip2HybridDataNodes():
    nodes = []

    data = open("human2hybrid.txt", 'r')

    for line in data:
        list1 = []
        list2 = []
        lineS = line.split("\t")

        # add the altids

        altid1 = lineS[2].split("|")
        for altid in altid1:
            altid1r = re.match("entrez gene/locuslink:(.+)", altid)
            list1.append(altid1r.group(1))

        altid2 = lineS[3].split("|")
        for altid in altid2:
            altid2r = re.match("entrez gene/locuslink:(.+)", altid)
            list2.append(altid2r.group(1))

        # add the aliases
    
        aliases1 = lineS[4].split("|")
        for alias in aliases1:
            aliases1r = re.match("entrez gene/locuslink:(.+)\\(", alias)
            if aliases1r is not None:
                list1.append(aliases1r.group(1))
        
        aliases2 = lineS[5].split("|")
        for alias in aliases2:
            aliases2r = re.match("entrez gene/locuslink:(.+)\\(", alias)
            if aliases2r is not None:
                list2.append(aliases2r.group(1))

        # store lists in nodes array
        nodes.append(list1)
        nodes.append(list2)

    data.close()
    
    return nodes
