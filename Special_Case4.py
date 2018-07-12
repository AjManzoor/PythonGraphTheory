import networkx as nx
import matplotlib.pyplot as plt
import random as rand
import math
from Graph_Generator import yes_graph_generator, random_graph_generator

def special_4_check(G):
    a = rand.randint(0, int(G.number_of_nodes()-1))
    b = rand.randint(0, int(G.number_of_nodes()-1))
    #print (a,b)
    if a==b:
        special_4_check(G)
        
    if a not in G.neighbors(b) and int(G.degree(a)) + int(G.degree(b)) >= int(G.number_of_nodes()):
        return True
    else:
        return False

#Random condition
##nn = 20
##ne = nn*5
##G = random_graph_generator(nn,ne)
##nx.draw(G,with_labels = True)
##print(special_4_check(G))

##test = []
##for i in range(1000):
##    G = yes_graph_generator(nn,ne)
##    sc4 = special_4_check(G)
##    test.append(sc4)
##    o_count = test.count(True)
##print(o_count)
