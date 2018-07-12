import networkx as nx
import matplotlib.pyplot as plt
import random as rand
import math
from Graph_Generator import yes_graph_generator, random_graph_generator

def special_2_generator(nn):
    Graph = nx.DiGraph()
    edgelist = []

    for i in range(nn-1):
        Graph.add_node(i)
    for i in range(nn - 1):
        edgelist.append([i, i+1])
        Graph.add_edge(i, i+1)
    Graph.add_edge((nn - 1), 0)
    
    edgecheck = str(Graph.number_of_edges())
    #print("edges before "+ edgecheck)
    minimum = str(math.ceil(nn**2-3*nn+6)/2)
    #print("min degree " + minimum)

    while int(edgecheck) < float(minimum):
        n1 = rand.randint(0,(nn-1))
        n2 = rand.randint(0,(nn-1))
        if [n1, n2] not in edgelist:
            Graph.add_edge(n1, n2)
            edgelist.append([n1, n2])
            edgecheck = str(Graph.number_of_edges())
            minimum = str(math.ceil(nn**2-3*nn+6)/2)

    #print("edges after "+str(Graph.number_of_edges()))
        
    return Graph

def special_2_check(G):
    if int(G.number_of_edges()) >= (math.ceil(int(G.number_of_nodes())**2-3*int(G.number_of_nodes())+6)/2):
        return True
    else:
        return False
     
# H = special_2_generator(20)
# print("Guaranteed condition:")
# print ("Number of Edges:" + str(H.number_of_edges()))
# special_2_check(H)

# #Random condition
#nn = 20
#ne = nn*8.8
#G = random_graph_generator(nn, ne)
# G = yes_graph_generator(nn,ne)
# nx.draw(G,with_labels = True)
# print("Random: ")
# print ("Number of Edges:" + str(G.number_of_edges()))
#print(special_2_check(G))
# plt.show()

# test = []
# for i in range(1000):
#     G = yes_graph_generator(nn, ne)
#     sc2 = special_2_check(G)
#     test.append(sc2)
# o_count = test.count(True)
# print(o_count)
