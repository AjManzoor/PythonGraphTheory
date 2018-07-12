import networkx as nx
import matplotlib.pyplot as plt
import random as rand
import math

from Graph_Generator import yes_graph_generator, random_graph_generator, undirected_graph_generator
from Special_Case1 import special_1_check
from Special_Case2 import special_2_check
from Special_Case3 import special_3_check
from Special_Case4 import special_4_check
from Special_Case5 import special_5_check


case_one_n = []
case_one_o = []

def Special_Case1_Occurance():
    max_repeats = 1000
    max_nodes = 10
    n = 2
    repeat = True
    case1 = []
    while repeat == True:
        for repeats in range(max_repeats):
            G = random_graph_generator(n, n*3)
            sc1 = special_1_check(G)
            case1.append(sc1)
        case1_occur = case1.count(True)
        case1 = []
        print(str(n)+"\t"+str(case1_occur/max_repeats))
        if n == max_nodes:
            repeat = False
        n += 1

def Special_Case2_Occurance():
    max_repeats = 1000
    max_nodes = 10
    n = 2
    repeat = True
    case2 = []
    while repeat == True:
        for repeats in range(max_repeats):
            G = random_graph_generator(n, n*3)
            sc2 = special_2_check(G)
            case2.append(sc2)
        case2_occur = case2.count(True)
        case2 = []
        print(str(n)+"\t"+str(case2_occur/max_repeats))
        if n == max_nodes:
            repeat = False
        n += 1

def Special_Case3_Occurance():
    max_repeats = 1000
    max_nodes = 10
    n = 2
    repeat = True
    case3 = []
    while repeat == True:
        for repeats in range(max_repeats):
            G = random_graph_generator(n, (n*(n-1))/2)
            sc3 = special_3_check(G, n)
            case3.append(sc3)
        case3_occur = case3.count(True)
        case3 = []
        print(str(n)+"\t"+str(case3_occur/max_repeats))
        if n == max_nodes:
            repeat = False
        n += 1

def Special_Case4_Occurance():
    max_repeats = 1000
    max_nodes = 10
    n = 2
    repeat = True
    case4 = []
    while repeat == True:
        for repeats in range(max_repeats):
            G = random_graph_generator(n, n*3)
            sc4 = special_4_check(G)
            case4.append(sc4)
        case4_occur = case4.count(True)
        case4 = []
        print(str(n)+"\t"+str(case4_occur/max_repeats))
        if n == max_nodes:
            repeat = False
        n += 1

def Special_Case5_Occurance():
    max_repeats = 1000
    max_nodes = 35
    n = 25
    repeat = True
    case5 = []
    while repeat == True:
        for repeats in range(max_repeats):
            G = undirected_graph_generator(n, n*3)
            sc5 = special_5_check(G)
            case5.append(sc5)
        case5_occur = case5.count(True)
        case5 = []
        print(str(n)+"\t"+str(case5_occur/max_repeats))
        if n == max_nodes:
            repeat = False
        n += 1

        
#Special_Case1_Occurance()
#Special_Case2_Occurance()
#Special_Case3_Occurance()
#Special_Case4_Occurance()
Special_Case5_Occurance()
