import networkx as nx
graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]
{'country': 'England',
 'latitude': '51.507222',
 'longitude': '-0.1275',
 'pos': '80,21!',
 'xlabel': 'City of London',
 'year': 0}