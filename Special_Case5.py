import networkx as nx
import random as rand
import math
from Graph_Generator import yes_graph_generator, random_graph_generator, undirected_graph_generator


def special_5_check(G):
    degree = []
    nn = (G.number_of_nodes())
    for i in range(int(nn)):
        degree.append(G.degree(i))
    for j in range(int(degree[-1])):
        if degree[j] <= degree[j+1]:
            p = True
        else:
             return False
            
    if p == True:
        k = (math.ceil(int(nn)/2))
        z = int(G.degree[(nn)-1 ]) - int(k)
        y = int(nn)-int(k)
        if int(G.degree[k]) > int(k):
            return True
        elif z >= y:
            return True
    else:
        return False
