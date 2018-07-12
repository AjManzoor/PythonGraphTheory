import networkx as nx
import matplotlib.pyplot as plt
import random
from time import time

# Object to store graph and solutions
class GraphSolution:
    def __init__(self, nNodes, nEdges):
        self.graph = self.yes_graph_generator(nNodes, nEdges)
        self.graspSolution = None
        self.graspCurrentSolution = None

    def Perc_Hamiltonian(self, solution):
        return (len(solution[1])) / len(solution[2])

    def yes_graph_generator(self, nn, ne):
        Graph = nx.DiGraph()
        edgelist = []

        for i in range(nn - 1):
            Graph.add_node(i)

        for i in range(nn - 1):
            edgelist.append([i, i + 1])
            Graph.add_edge(i, i + 1)

        Graph.add_edge((nn - 1), 0)
        edgelist.append([nn - 1, 0])

        i = 0
        while i < (ne - nn):
            n1 = random.randint(0, (nn - 1))
            n2 = random.randint(0, (nn - 1))
            if n1 != n2:
                if [n1, n2] not in edgelist:
                    Graph.add_edge(n1, n2)
                    edgelist.append([n1, n2])
                    i += 1
        return Graph

    def undirected_graph_generator(self, nn, ne):
        Graph = nx.Graph()
        edgelist = []

        for i in range(nn - 1):
            Graph.add_node(i)

        for i in range(nn - 1):
            edgelist.append([i, i + 1])
            Graph.add_edge(i, i + 1)

        Graph.add_edge((nn - 1), 0)
        edgelist.append([nn - 1, 0])

        i = 0
        while i < (ne - nn):
            n1 = random.randint(0, (nn - 1))
            n2 = random.randint(0, (nn - 1))
            if n1 != n2:
                if [n1, n2] not in edgelist:
                    Graph.add_edge(n1, n2)
                    edgelist.append([n1, n2])
                    i += 1
        return Graph

    def Most_Outgoing_Edges(self, edges=-1):
        # finds the node with the most outgoing edges
        # list to store list's of outgoing edges
        node_edges = []
        if edges == -1:
            for s in self.graph.nodes():
                # list to store outgoing edges from a node
                edgelist = []
                for i in self.graph[s]:
                    edgelist.append(i)
                node_edges.append(edgelist)
            return node_edges.index(max(node_edges, key=len))
        else:
            for s in edges:
                edgelist = []
                edgelist.append(s)
                for i in self.graph[s]:
                    edgelist.append(i)
                node_edges.append(edgelist)
            n = node_edges.index(max(node_edges, key=len))
            return node_edges[n][0]

    # Function to perform a randomized greedy search
    def random_greedy_search(self):
        # Generate random index for start node
        randIndex = random.randint(0, (len(self.graph.nodes()) - 1))

        stack = []
        for i in self.graph[randIndex]:
            stack.append(i)

        path = [randIndex]

        while stack:
            # Pop a random edge from the node
            node = stack.pop(random.randint(0, (len(stack) - 1)))
            if node not in path:
                # add to the path
                path.append(node)
                edges = []
                # looping through outgoing edges from the new node
                for i in self.graph[node]:
                    edges.append(i)
                # if the node has edges that can be visited
                if len(edges) != 0:
                    # replace the stack with the outgoing edges of the new node
                    stack = edges
                # if node is a dead end
                else:
                    # return the path
                    return [False, path, self.graph]
                    # if a cycle is found
            if node == randIndex:
                # return the path
                return [True, path, self.graph]
        # if the search can't find any unvisited nodes, return the path
        return [False, path, self.graph]

    # Function to perfom grasp operation on graph
    def grasp(self, maxIterations=100):
        # set solution to 0 so no cases are satisfied
        self.graspSolution = [False, [], [0]]
        for index in range(maxIterations):
            # generate random solution
            self.graspCurrentSolution = self.random_greedy_search()

            # perform local search on self
            self.localSearch()

            # check if local optimum from local search is greater then current solution
            if self.Perc_Hamiltonian(self.graspCurrentSolution) > self.Perc_Hamiltonian(self.graspSolution):
                self.graspSolution = self.graspCurrentSolution

    def localSearch(self):
        neighbourArray = self.generateNeighbourhood()

        for i in range(len(neighbourArray)):
            if self.Perc_Hamiltonian(neighbourArray[i]) > self.Perc_Hamiltonian(self.graspCurrentSolution):
                # new local optimum
                self.graspCurrentSolution = neighbourArray[i]
        return None

    def generateNeighbourhood(self):
        neighbourArray = []
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
                    n = self.Most_Outgoing_Edges(stack)
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
                            neighbourArray.append([False, neighbourPath, self.graph])
                    if n == self.graspCurrentSolution[1][0]:
                        neighbourArray.append([True, neighbourPath, self.graph])
            # decrement index
            lastIndex -= 1
        return neighbourArray

    def greedy_search(self):
        # node with most outgoing edges set as starting node
        S = self.Most_Outgoing_Edges()
        stack = []
        for i in self.graph[S]:
            # add destination node of each outgoing edge from start node to the stack
            stack.append(i)
        # starting edge is added to the path
        path = [S]
        while stack:
            # takes the next destination node as the one with the most outgoing edges
            n = self.Most_Outgoing_Edges(stack)
            stack.remove(n)
            # if node hasn't been visited
            if n not in path:
                # add to the path
                path.append(n)
                edges = []
                # looping through outgoing edges from the new node
                for i in self.graph[n]:
                    if i not in path or i == S:
                        edges.append(i)
                # if the node has edges that can be visited
                if len(edges) != 0:
                    # replace the stack with the outgoing edges of the new node
                    stack = edges
                    # if node is a dead end
                else:
                    # return the path
                    return [False, path, self.graph]
                    # if a cycle is found
            if n == S:
                # return the path
                return [True, path, self.graph]
        # if the search can't find any unvisited nodes, return the path
        return [False, path, self.graph]

    # Function to find if hamiltonian cycle exists in given paths
    def findHamiltonianCycle(self, nNodes, p):
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

    # Function to find all paths in a given graph
    def exhaustive_search(self):
        # start = timeit.default_timer()
        for s in self.graph.nodes():
            path = [s]
            stack = [s]
            edges = []
            for i in self.graph[s]:
                edges.append(i)
            stack = edges + stack
            while stack:
                pathedges = []
                for i in self.graph[path[len(path) - 1]]:
                    pathedges.append(i)
                n = stack.pop(0)
                if n not in pathedges:
                    path.pop()
                    stack = [n] + stack
                    break
                if n not in path or (n == s and len(path) == len(self.graph)):
                    path.append(n)
                    if self.findHamiltonianCycle(len(self.graph), path) == True:
                        # stop = timeit.default_timer()
                        # print (stop - start)
                        return "Hamiltonian Cycle Found -> " + str(path)
                    edges = []
                    for i in self.graph[n]:
                        edges.append(i)
                    stack = edges + stack
        # stop = timeit.default_timer()
        # print (stop - start)
        return "No Hamiltonian Cycle Found"

    def exhaustive_search_full(self):
        hamCyc = []
        for s in self.graph.nodes():
            path = [s]
            stack = [s]
            edges = []
            for i in self.graph[s]:
                edges.append(i)
            stack = edges + stack
            while stack:
                pathedges = []
                for i in self.graph[path[len(path) - 1]]:
                    pathedges.append(i)
                n = stack.pop(0)
                if n not in pathedges:
                    path.pop()
                    stack = [n] + stack
                    break
                if n not in path or (n == s and len(path) == len(self.graph)):
                    path.append(n)
                    if self.findHamiltonianCycle(len(self.graph), path) == True:
                        hamCyc.append(True)
                    edges = []
                    for i in self.graph[n]:
                        edges.append(i)
                    stack = edges + stack
        return sum(hamCyc)


# points_n = []
# points_t = []
# def time_exhaustive():
#     print("n\tExhaustive")
#     max_repeats = 1000
#     max_nodes = 5000
#     n = 100
#     t0 = t1 = 0
#     repeat = True
#     while repeat == True:
#         t0 = time()
#         for repeats in range(max_repeats):
#             graphSolution = GraphSolution(n, n*1.5)
#             graphSolution.exhaustive_search()
#         t1 = time()
#         print(str(n)+"\t"+str((t1-t0)/max_repeats))
#         points_n.append(n)
#         points_t.append((t1-t0)/max_repeats)
#         if n == max_nodes:
#             repeat = False
#         n += 100
# time_exhaustive()
#
# plt.plot(points_n, points_t, 'ro-')
# plt.show()

points_n = []
points_greedy = []
points_grasp = []

def test_approximation():
    print("nNodes\t% Greedy\t% Grasp")
    max_nodes = 1000
    max_repeats = 1
    n = 100
    repeat = True
    while repeat is True:
        grasp_average = []
        greedy_average = []
        for i in range(max_repeats):
            # Generate new object with random graph
            graphInstance = GraphSolution(n, n * 2)
            # Perform grasp allowing for 1000 iterations
            graphInstance.grasp()
            # Estimate how close to hamiltonian cycle solution is
            grasp = float(graphInstance.Perc_Hamiltonian(graphInstance.graspSolution))
            # Estimate hamiltonian cycle for greedy
            greedy = float(graphInstance.Perc_Hamiltonian(graphInstance.greedy_search()))

            grasp_average.append(grasp)
            greedy_average.append(greedy)

        # Print results
        greedy_average_calculated = '{:1.4f}'.format(sum(greedy_average)/max_repeats)
        grasp_average_calculated = '{:1.4f}'.format(sum(grasp_average)/max_repeats)

        print(str(n) + "\t\t" + str(greedy_average_calculated) + "\t\t" + str(grasp_average_calculated))
        points_n.append(n)
        points_greedy.append(greedy_average_calculated)
        points_grasp.append(grasp_average_calculated)
        if n == max_nodes:
            repeat = False
        n += 100

test_approximation()

plt.figure()
p1 = plt.plot(points_n, [float(i)for i in points_greedy], 'bo-', label="Greedy")
p2 = plt.plot(points_n, [float(i)for i in points_grasp], 'ro-', label="GRASP")
plt.legend(loc='best')
plt.show()
