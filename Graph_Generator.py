import networkx as nx
import matplotlib.pyplot as plt
import random as rand

def random_graph_generator(nn, ne):
    Graph = nx.gnm_random_graph(nn, ne, None, True)
    return Graph

def yes_graph_generator(nn, ne):
    Graph = nx.DiGraph()
    edgelist = []

    for i in range(nn - 1):
        Graph.add_node(i)

    for i in range(nn - 1):
        edgelist.append([i, i+1])
        Graph.add_edge(i, i+1)

    Graph.add_edge((nn - 1), 0)
    edgelist.append([nn-1, 0])

    i = 0
    while i < (ne - nn):
        n1 = rand.randint(0, (nn-1))
        n2 = rand.randint(0, (nn-1))
        if n1 != n2:
            if [n1, n2] not in edgelist:
                    Graph.add_edge(n1, n2)
                    edgelist.append([n1, n2])
                    i += 1 
    return Graph

def undirected_graph_generator(nn, ne):
    Graph = nx.Graph()
    edgelist = []

    for i in range(nn - 1):
        Graph.add_node(i)

    for i in range(nn - 1):
        edgelist.append([i, i+1])
        Graph.add_edge(i, i+1)

    Graph.add_edge((nn - 1), 0)
    edgelist.append([nn-1, 0])

    i = 0
    while i < (ne - nn):
        n1 = rand.randint(0, (nn-1))
        n2 = rand.randint(0, (nn-1))
        if n1 != n2:
            if [n1, n2] not in edgelist:
                    Graph.add_edge(n1, n2)
                    edgelist.append([n1, n2])
                    i += 1 
    return Graph
