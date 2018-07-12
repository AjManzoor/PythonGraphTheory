import networkx as nx
import matplotlib.pyplot as plt
import random as rand
import math
from Graph_Generator import yes_graph_generator, random_graph_generator

def special_1_generator(nn):
    Graph = nx.DiGraph()
    edgelist = []

    for i in range(nn-1):
        Graph.add_node(i)
    for i in range(nn - 1):
        edgelist.append([i, i+1])
        Graph.add_edge(i, i+1)
    Graph.add_edge((nn - 1), 0)

    #print("total edges "+str(Graph.number_of_edges()))
    #print("min degree " +str(math.ceil(nn/2)))

    for i in range(nn):
        #print("node "+str(i)+"-"+str(Graph.degree(i)))
        while Graph.degree(i) < math.ceil(nn/2):
            n1 = rand.randint(0,(nn-1))
            if i != n1:
                if [i,n1] not in edgelist:
                    Graph.add_edge(i,n1)
                    edgelist.append([i,n1])
                    
    '''for i in range(nn):
        print("node "+str(i)+"-"+str(Graph.degree(i)))'''
        
    return Graph

def special_1_check(G):
    check = []
    for i in range(int(G.number_of_nodes())):
        if G.degree(i) >= math.ceil(G.number_of_nodes()/2):
            check.append([i])
            
        if len(check) == G.number_of_nodes():
            return True
                
    if len(check) != G.number_of_nodes():
        return False
        
        
#Running check on guaranteed condition
#H = special_1_generator(15)
#print("Guaranteed condition:")
#special_1_check(H)

#Random condition
#nn = 30
#ne = nn*9
#G = random_graph_generator(nn,ne)
#nx.draw(G,with_labels = True)
#print("Random: ")
#print(special_1_check(G))
#plt.show()
# test = []
# for i in range(1000):
#     G = random_graph_generator(nn, ne)
#     sc1 = special_1_check(G)
#     test.append(sc1)
# o_count = test.count(True)
# print(o_count)
#print(G.degree)