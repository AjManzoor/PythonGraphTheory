import networkx as nx
import matplotlib.pyplot as plt

from Graph_Generator import yes_graph_generator, random_graph_generator

def Perc_Hamiltonian(c):
    return ((len(c[1]))*100)/len(c[2])

def Most_Outgoing_Edges(G, edges=-1):
    #finds the node with the most outgoing edges
    #list to store list's of outgoing edges
    node_edges=[]
    if edges == -1:
        for s in G.nodes():
            #list to store outgoing edges from a node
            edgelist=[]
            for i in G[s]:
                edgelist.append(i)
            node_edges.append(edgelist)
        return node_edges.index(max(node_edges,key=len))
    else:
        for s in edges:
            edgelist=[]
            edgelist.append(s)
            for i in G[s]:
                edgelist.append(i)
            node_edges.append(edgelist)
        n = node_edges.index(max(node_edges,key=len))
        return node_edges[n][0]
        
def Greedy_Search(G):
    #node with most outgoing edges set as starting node
    S = Most_Outgoing_Edges(G)
    stack=[]
    for i in G[S]:
        #add destination node of each outgoing edge from start node to the stack
        stack.append(i)
    #starting edge is added to the path
    path = [S] 
    while stack:
        #takes the next destination node as the one with the most outgoing edges
        n = Most_Outgoing_Edges(G,stack)
        stack.remove(n)
        #if node hasn't been visited
        if n not in path: 
            #add to the path
            path.append(n) 
            edges = []
            #looping through outgoing edges from the new node
            for i in G[n]:
                if i not in path or i == S:
                    edges.append(i)
            #if the node has edges that can be visited
            if len(edges) != 0: 
                #replace the stack with the outgoing edges of the new node
                stack = edges 
            #if node is a dead end
            else: 
                #return the path
                return [False, path, G] 
        #if a cycle is found
        if n == S: 
            #return the path
            return [True, path, G]
    #if the search can't find any unvisited nodes, return the path
    return [False, path, G] 

points_n = []
points_a = []
def Greedy_Approximation():
    print("n\tApproximation")
    max_repeats = 1000
    max_nodes = 1000
    n = 100
    repeat = True
    approx = []
    while repeat == True:
        for repeats in range(max_repeats):
            G = random_graph_generator(n, n*2)
            a = Perc_Hamiltonian(Greedy_Search(G))
            approx.append(a)
        approx_final = sum(approx)
        approx = []
        print(str(n)+"\t"+str((approx_final/max_repeats)))
        points_n.append(n)
        points_a.append(approx_final/max_repeats)
        if n == max_nodes:
            repeat = False
        n += 100
    #nx.draw(G, with_labels=True)
    #plt.show()
Greedy_Approximation()
plt.plot(points_n, points_a, 'ro-')
plt.show()

#nn = 20
#ne = nn*3
#G = random_graph_generator(nn,ne)
#nx.draw(G, with_labels=True)
#print(Perc_Hamiltonian(Greedy_Search(G)))
#greedy = Greedy_Search(G)
#print(greedy[0], greedy[1])
# plt.show()
