import networkx as nx
import matplotlib.pyplot as plt
import random as rand
from time import time
import timeit
from Graph_Generator import yes_graph_generator, random_graph_generator

# Function to find if hamiltonian cycle exists in given paths
def findHamiltonianCycle(nNodes, p):
    # check length is correct
    if len(p) == (nNodes + 1):
        # check start and end nodes are the same
        if p[0] == p[len(p) - 1]:
            # remove last item in list
            x = p[:-1]
            # check for duplicates
            if len(x) == len(set(x)):
                # return true if all conditions are met
                return True
    # return false if no conditions met by any of the paths
    return False

#Function to find all paths in a given graph
def Exhaustive_Search(G):
    #start = timeit.default_timer()
    for s in G.nodes():
        path = [s]
        stack = [s]
        edges = []
        for i in G[s]:
            edges.append(i)
        stack = edges + stack
        while stack:
            pathedges = []
            for i in G[path[len(path)-1]]:
                pathedges.append(i)
            n = stack.pop(0)
            if n not in pathedges:
                path.pop()
                stack = [n] + stack
                break
            if n not in path or (n == s and len(path) == len(G)):
                path.append(n)
                if findHamiltonianCycle(len(G), path) == True:
                    #stop = timeit.default_timer()
                    #print (stop - start)
                    return "Hamiltonian Cycle Found -> "+str(path)
                edges = []
                for i in G[n]:
                    edges.append(i)
                stack = edges + stack
    #stop = timeit.default_timer()
    #print (stop - start)
    return "No Hamiltonian Cycle Found"


def exhaustive_search_full(G):
    hamCyc = []
    for s in G.nodes():
        path = [s]
        stack = [s]
        edges = []
        for i in G[s]:
            edges.append(i)
        stack = edges + stack
        while stack:
            pathedges = []
            for i in G[path[len(path) - 1]]:
                pathedges.append(i)
            n = stack.pop(0)
            if n not in pathedges:
                path.pop()
                stack = [n] + stack
                break
            if n not in path or (n == s and len(path) == len(G)):
                path.append(n)
                if findHamiltonianCycle(len(G), path) == True:
                    hamCyc.append(True)
                edges = []
                for i in G[n]:
                    edges.append(i)
                stack = edges + stack
    return sum(hamCyc)

points_n = []
points_t = []
def Time_Exhaustive():
    print("n\tExhaustive")
    max_repeats = 1000
    max_nodes = 5000
    n = 100
    t0 = t1 = 0
    repeat = True
    while repeat == True:
        t0 = time()
        for repeats in range(max_repeats):
            G = yes_graph_generator(n, n*1.5)
            Exhaustive_Search(G)
        t1 = time()
        print(str(n)+"\t"+str((t1-t0)/max_repeats))
        points_n.append(n)
        points_t.append((t1-t0)/max_repeats)
        if n == max_nodes:
            repeat = False
        n += 100
Time_Exhaustive()

plt.plot(points_n, points_t, 'ro-')
plt.show()

#nn = 1000  # number of nodes on the graph
#ne = nn  # number of edges in the graph
#G = random_graph_generator(nn,ne)
#G = yes_graph_generator(nn, ne)
#pos = nx.spring_layout(G)

#print(Exhaustive_Search(G))
#nx.draw(G, with_labels=True)
#plt.show()
