import networkx as nx
import os
import re
import string
import math
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from random import getrandbits
import collections
from networkx.algorithms import community
import pickle
import webwebpy
def read_data(path):
    G = nx.Graph()
    with open(path, 'r') as f:
        lines = f.readlines()
    maxNode = 6300
    '''
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
        edge = lines[i].split('\t')
        if int(edge[0])> maxNode:
            maxNode = int(edge[0])
        if int(edge[1])> maxNode:
            maxNode = int(edge[1])
    print(maxNode)
    '''
    for i in range(maxNode+1):
        G.add_node(i)
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n')
        edge = lines[i].split('\t')
        G.add_edge(int(edge[0]),int(edge[1]))
    return G

def plot(data, xlabel, ylabel):
    num_bins = 100
    figsize = 11,7
    fig, ax1 = plt.subplots(figsize=figsize)
    plt.xlabel(xlabel) #label x
    plt.ylabel(ylabel) #label y
    plt.hist(data, num_bins, facecolor='blue', alpha=0.5)
    plt.show()

G = read_data("Gnutella p2p.txt")
#G = nx.planted_partition_graph(2, 10, 0.8, 0.01, seed=42)
print("finish reading")
n = nx.number_of_nodes(G)
'''
figsize = 11,7
plt.subplots(figsize=figsize)
nx.draw(G, with_labels=False, font_weight='bold')
plt.show()
'''
'''
#degree centrality
degreeCentrality = nx.degree_centrality(G)
sortedDegCentr = sorted(degreeCentrality.items(),key=lambda item:item[1], reverse=True)
data1 = []
for i in range(n):
    data1.append(sortedDegCentr[i][1])
print("finish1")

#betweenness centrality
betweennessCentrality = nx.betweenness_centrality(G, None, False, None, True, None)
sortedBetwCentr = sorted(betweennessCentrality.items(),key=lambda item:item[1], reverse=True)
print("finish2")
data2 = []
for i in range(n):
    data2.append(sortedBetwCentr[i][1])
print("finish2")

data3 = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence

print("finish3")
plot(data1, "Degree Centrality", "Number of Nodes")
#plot(data2, "Betweenness Centrality", "Number of Nodes")
plot(data3, "Degree", "Number of Nodes")
'''
#detect comunity
'''
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
com1 = sorted(map(sorted, next_level_communities))
print(com1)
'''

#com2 = list(community.greedy_modularity_communities(G))
#print(com2)

#pickle.dump(com2, open( 'com' + '.p', "wb" ) )

com = pickle.load( open( "com.p", "rb" ) )
print(len(com))
for i in range(len(com)):
    froze = iter(com[i])
    f_list = list(froze)
    print(len(f_list))
