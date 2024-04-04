import osmnx as ox
import networkx as nx
import folium


def read_graph(city: str, tolerance: float, buffer: float = None):
    G_raw = ox.graph_from_place(city,
                            network_type='drive',
                            buffer_dist=buffer)
    G = ox.project_graph(G_raw)
    G = ox.consolidate_intersections(G, tolerance=tolerance)
    return G


location = "Krowodrza, Kraków"

G = read_graph(location, tolerance=20, buffer=0)


ox.plot_graph(G)

nodes, streets = ox.graph_to_gdfs(G)

print(nodes.head())

m = folium.Map(location=ox.geocode(location))

m.show_in_browser()
