#%%
import networkx as nx
import osmnx
from tqdm import tqdm
import numpy as np

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
def get_graph_destinations(G, station, destinations, conversion_name_index, conversion_index_name):
    concatenate = {**station, **destinations}
    graph = np.zeros((len(concatenate), len(concatenate)))
    for origin_name in tqdm(concatenate):
        for destination_name in concatenate:
            if origin_name != destination_name:
                origine = osmnx.distance.nearest_nodes(G, X=concatenate[origin_name][0], Y=concatenate[origin_name][1])
                destination = osmnx.distance.nearest_nodes(G, X=concatenate[destination_name][0], Y=concatenate[destination_name][1])
                route = osmnx.shortest_path(G, origine, destination)
                edge_lengths = osmnx.utils_graph.get_route_edge_attributes(G2, route, attribute="length")
                graph[conversion_name_index[origin_name], conversion_name_index[destination_name]] = np.sum(edge_lengths)
    return graph   

# %%

graph = get_graph_destinations(G2, station, destinations)
