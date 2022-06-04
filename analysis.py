# encoding:utf-8

from collections import Counter

from scipy.io import mmread
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import numpy as np
import community
import copy
import powerlaw
# read data
g = nx.Graph(np.matrix(mmread('soc-dolphins.mtx').todense()))

# file = open('aves-weaver-social-16.edges')                                                                                                                    
# g = nx.Graph()                                                                                                                                                
# for row in file:                                                                                                                                              
#         g.add_edge(row.split()[0],row.split()[1])
def avgPathLength():
    return nx.average_shortest_path_length(g)
#print(avgPathLength())

def diameter():
    return nx.diameter(g)
# print(diameter())

def drawShortestPath():
    d=dict(nx.all_pairs_shortest_path_length(g))
    all_length = [d[i][j] for i in d for j in d[i] if i<j]
    avg= sum(all_length)/len(all_length)
    acc= Counter(all_length)
    plt.bar(acc.keys(),acc.values(),align='center')
    plt.savefig('shortest_path.png')
    plt.show()
    plt.clf()
# drawShortestPath()

def clustering_coefficient():
    return nx.average_clustering(g)
# print(clustering_coefficient())

def plot_degree_dist():
    x = [i[1] for i in g.degree]
    acc = Counter(x)
    plt.bar(acc.keys(),acc.values(),align='center')
    plt.savefig('degree_distribution.png')
    plt.show()
    plt.clf()
# plot_degree_dist()

def degreeCorrelation():
    return nx.degree_pearson_correlation_coefficient(g)
# print(degreeCorrelation())
def degree_centrality():
    d= [round(nx.degree_centrality(g)[i], 2) for i in nx.degree_centrality(g)]
    node_colors= []
    for i in d:
        if(i>0.175):
            node_colors.append('steelblue')
        else:
            node_colors.append('skyblue')
    mapping = dict(zip(g.nodes(), d))

    pos = nx.kamada_kawai_layout(g)
    nx.draw(g, pos, with_labels=True, font_size= 8,node_size=300,node_color=node_colors,labels= mapping) 
    plt.savefig('degree_centrality.png')
    plt.show()
    plt.clf()
degree_centrality()
def betweeness():
    d= [round(nx.betweenness_centrality(g)[i], 2) for i in nx.betweenness_centrality(g)]
    node_colors= []
    for i in d:
        if(i>0.2):
            node_colors.append('steelblue')
        else:
            node_colors.append('skyblue')
    mapping = dict(zip(g.nodes(), d))

    pos = nx.kamada_kawai_layout(g)
    nx.draw(g, pos, with_labels=True, font_size= 8, node_size=300,node_color=node_colors,labels= mapping) 
    plt.savefig('betweeness.png')
    plt.show()
    plt.clf()
betweeness()
def eigen():
    d= [round(nx.eigenvector_centrality(g)[i], 2) for i in nx.eigenvector_centrality(g)]
    node_colors= []
    for i in d:
        if(i>0.25):
            node_colors.append('steelblue')
        else:
            node_colors.append('skyblue')
    mapping = dict(zip(g.nodes(), d))

    pos = nx.kamada_kawai_layout(g)
    nx.draw(g, pos, with_labels=True,font_size= 8, node_size=300,node_color=node_colors,labels= mapping) 
    plt.savefig('eigen.png')
    plt.show()
    plt.clf()
eigen()
def closeness():
    
    d= [round(nx.closeness_centrality(g)[i], 2) for i in nx.closeness_centrality(g)]
    node_colors= []
    for i in d:
        if(i>0.35):
            node_colors.append('steelblue')
        else:
            node_colors.append('skyblue')
    mapping = dict(zip(g.nodes(), d))

    pos = nx.kamada_kawai_layout(g)
    nx.draw(g, pos, with_labels=True,font_size=8, node_size=300,node_color=node_colors,labels= mapping) 
    plt.savefig('close.png')
    plt.show()
    plt.clf()
closeness()
def modularity():
    # d= nx.modularity(g, g.nodes, weight='weight', resolution=1)
    # Find modularity
    # Plot, color nodes using community structure
   part = community.best_partition(g)
   mod = community.modularity(part,g)
   values = [part.get(node) for node in g.nodes()]
   nx.draw_spring(g, cmap=plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
   plt.show()
   plt.clf()
# modularity()
# # # 绘制图
# # nx.draw(graph, with_labels=True)

# # # 保存图
# # plt.savefig('./ren/graph/Dolphin.png')

# # # 展示图
# # plt.show()