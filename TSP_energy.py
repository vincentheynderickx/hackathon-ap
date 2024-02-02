#%%
import networkx as nx
import osmnx
from tqdm import tqdm
import numpy as np
import energie
import create_graph_osdm
import sys
import matplotlib.pyplot as plt

#%%

station = {'SOGARIS' : (2.36815, 48.74991)} 
destinations = {'Mines Paris' : (2.33969, 48.84563),
                 'Observatoire de Paris' : (2.33650, 48.83730), 
                 'Marie du 14e' : (2.32698, 48.83320), 
                 'Gare Montparnasse TGV' : (2.32159, 48.84117), 
                 'Mairie du 15e' : (2.29991, 48.84126)}

conversion_index_name = {0: "SOGARIS", 1: "Mines Paris", 2: "Observatoire de Paris", 3: "Marie du 14e", 4: "Gare Montparnasse TGV", 5: "Mairie du 15e"}

conversion_name_index = {"SOGARIS": 0, "Mines Paris": 1, "Observatoire de Paris": 2, "Marie du 14e": 3, "Gare Montparnasse TGV": 4, "Mairie du 15e": 5}

#%%

G2 = osmnx.graph_from_address(address="60 boulevard Saint-Michel, Paris, France", 
                              dist=15000,
                              dist_type="network",
                              network_type="drive",) 

#%%

G2_energie = G2.copy()

for u, v, data in G2_energie.edges(data=True):
    data['length'] = energie.energie(data['length'])

#%%
    
print(G2_energie.edges(data=True))

#%%
 
create_graph_osdm.get_graph_destinations(G=G2_energie)

#%%

matrice, routes = create_graph_osdm.get_graph_destinations(G=G2_energie)

def tsp(graph):
    n = len(graph)
    
    # Memoization table
    memo = {}

    # Helper function to compute the optimal tour starting from node 0
    def tsp_helper(mask, current):
        if (mask, current) in memo:
            return memo[(mask, current)]

        # If all nodes have been visited, return the distance to the starting node
        if mask == (1 << n) - 1:
            return graph[current][0], [0]

        # Try all possible next nodes and find the minimum distance
        min_distance = float('inf')
        optimal_path = []

        for next_node in range(1, n):
            if (mask >> next_node) & 1 == 0:
                distance, path = tsp_helper(mask | (1 << next_node), next_node)
                distance += graph[current][next_node]

                if distance < min_distance:
                    min_distance = distance
                    optimal_path = [current] + path

        memo[(mask, current)] = (min_distance, optimal_path)
        return min_distance, optimal_path

    # Start from node 0
    distance, optimal_path = tsp_helper(1, 0)
    
    return distance, optimal_path
    

distance, path_num = tsp(matrice)

all_destinations = {**create_graph_osdm.station, **create_graph_osdm.destinations}

path = [create_graph_osdm.conversion_index_name[i] for i in path_num]

routes = [routes[(path[i], path[i+1])] for i in range(len(path)-1)]

"""for route in routes:
    osmnx.plot_graph_route(create_graph_osdm.G2, route, route_linewidth=6, node_size=0, bgcolor='k')"""


final = []

for route in routes:
    final += route[1:]

    
osmnx.plot_graph_route(create_graph_osdm.G2, final, route_linewidth=6, node_size=0, bgcolor='k')
