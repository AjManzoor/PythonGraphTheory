import networkx as nx
import matplotlib.pyplot as plt
import random as rand
from Graph_Generator import yes_graph_generator, random_graph_generator


def tournament_generator(nn):
    G = nx.DiGraph()

    for i in range(nn):
        G.add_node(i)

    for n in G.nodes():
        for m in G.nodes():
            if m != n and not G.has_edge(n,m) and not G.has_edge(m,n):
                G.add_edge(n, m)

    return G

    


def special_3_check(G, nn):
    edgelist = []
    if G.number_of_edges() == ((nn * (nn - 1))/2):
        for e in G.edges():
            if [e[0],e[1]] not in edgelist and [e[1],e[0]] not in edgelist:
                edgelist.append([e[0],e[1]])
            else:
                return False
        return True
    else:
        return False



