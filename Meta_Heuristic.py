import networkx as nx
import matplotlib.pyplot as plt
import random

from Graph_Generator import random_graph_generator

# Object to store graph and solutions
class GraphSolution:
    def __init__(self, nNodes, nEdges):
        self.graph = random_graph_generator(nNodes, nEdges)
        self.solution = None
        self.graspCurrentSolution = None
        self.neighbourArray = []

    # Function to perfom grasp operation on graph
    def grasp(self, maxIterations=100):
        # set solution to 0 so no cases are satisfied
        self.solution = [False, [], [0]]
        for index in range(maxIterations):
            # generate random solution
            self.graspCurrentSolution = random_greedy_search(self.graph)

            # perform local search on self
            self.localSearch()

            # check if local optimum from local search is greater then current solution
            if Perc_Hamiltonian(self.graspCurrentSolution) > Perc_Hamiltonian(self.solution):
                self.solution = self.graspCurrentSolution

    def localSearch(self):
        self.generateNeighbourhood()

        for i in range(len(self.neighbourArray)):
            if Perc_Hamiltonian(self.neighbourArray[i]) > Perc_Hamiltonian(self.graspCurrentSolution):
                # new local optimum
                self.graspCurrentSolution = self.neighbourArray[i]
        # reset neighbourArray for next time
        self.neighbourArray = []
        return None

    def generateNeighbourhood(self):
        # get index of first node of interest
        lastIndex = len(self.graspCurrentSolution[1]) - 1
        while lastIndex >= 0:
            node = self.graspCurrentSolution[1][lastIndex -1]

            if lastIndex > 1:
                neighbourPath = self.graspCurrentSolution[1][0:lastIndex]

                stack = []
                test = self.graph[node]
                for i in test:
                    if i != self.graspCurrentSolution[1][lastIndex]:
                        stack.append(i)

                while stack:
                    n = Most_Outgoing_Edges(self.graph, stack)
                    stack.remove(n)
                    if n not in neighbourPath:
                        neighbourPath.append(n)
                        edges = []
                        for i in self.graph[n]:
                            if i not in neighbourPath or i == self.graspCurrentSolution[1][0]:
                                edges.append(i)
                        if len(edges) != 0:
                            stack = edges
                        else:
                            self.neighbourArray.append([False, neighbourPath, self.graph])
                    if n == self.graspCurrentSolution[1][0]:
                        self.neighbourArray.append([True, neighbourPath, self.graph])
            # decrement index
            lastIndex -= 1
        return None

def Perc_Hamiltonian(c):
    if c[0] is True:
        return 100
    else:
        return ((len(c[1])) * 100) / len(c[2])

def Most_Outgoing_Edges(G, edges=-1):
    # finds the node with the most outgoing edges
    # list to store list's of outgoing edges
    node_edges = []
    if edges == -1:
        for s in G.nodes():
            # list to store outgoing edges from a node
            edgelist = []
            for i in G[s]:
                edgelist.append(i)
            node_edges.append(edgelist)
        return node_edges.index(max(node_edges, key=len))
    else:
        for s in edges:
            edgelist = []
            edgelist.append(s)
            for i in G[s]:
                edgelist.append(i)
            node_edges.append(edgelist)
        n = node_edges.index(max(node_edges, key=len))
        return node_edges[n][0]


# Function to perform a randomized greedy search
def random_greedy_search(Graph):
    # Generate random index for start node
    randIndex = random.randint(0, (len(Graph.nodes()) - 1))

    stack = []
    for i in Graph[randIndex]:
        stack.append(i)

    path = [Graph[randIndex]]

    while stack:
        # Pop a random edge from the node
        node = stack.pop(random.randint(0, (len(stack) - 1)))
        if node not in path:
            # add to the path
            path.append(node)
            edges = []
            # looping through outgoing edges from the new node
            for i in Graph[node]:
                edges.append(i)
            # if the node has edges that can be visited
            if len(edges) != 0:
                # replace the stack with the outgoing edges of the new node
                stack = edges
            # if node is a dead end
            else:
                # return the path
                return [False, path, Graph]
                # if a cycle is found
        if node == Graph[randIndex]:
            # return the path
            return [True, path, Graph]
    # if the search can't find any unvisited nodes, return the path
    return [False, path, Graph]


points_n = []
points_a = []


def Grasp_Approximation():
    print("n\tApproximation")
    max_nodes = 1000
    n = 100
    repeat = True
    while repeat is True:
        # Generate new object with random graph
        graphGrasp = GraphSolution(n, n * 3)
        # Perform grasp allowing for 1000 iterations
        graphGrasp.grasp(1000)
        # Estimate how close to hamiltonian cycle solution is
        a = Perc_Hamiltonian(graphGrasp.solution)
        # Print results
        print(str(n) + "\t" + str(a))
        points_n.append(n)
        points_a.append(a)
        if n == max_nodes:
            repeat = False
        n += 100

Grasp_Approximation()

plt.plot(points_n, points_a, 'ro-')
plt.show()
