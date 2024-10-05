import heapq

import pandas as pd
import networkx as nx


def construct_graph(df):
    star_graph = nx.DiGraph()

    for index, row in df.iterrows():
        system = row['System'].lower()
        destinations = row[1:].dropna().str.lower()

        for destination in destinations:
            if destination:
                star_graph.add_edge(system, destination)
    return star_graph

def beam_search_longest_path(G, start_node=None, visited=None, beam_width=2):
    if visited is None:
        visited = set()

    if start_node is None:
        paths = [(0, [node]) for node in G.nodes if node not in visited]
    else:
        paths = [(0, [start_node])]

    longest_path = []

    while paths:
        # Keep only the top paths based on length (beam width)
        paths = heapq.nlargest(beam_width, paths, key=lambda x: x[0])

        new_paths = []
        for length, path in paths:
            last_node = path[-1]
            for neighbor in G.neighbors(last_node):
                if neighbor not in path and neighbor not in visited:  # Avoid cycles and revisits
                    new_path = path + [neighbor]
                    new_paths.append((len(new_path), new_path))
                    if len(new_path) > len(longest_path):
                        longest_path = new_path

        paths = new_paths

    return longest_path


if __name__ == '__main__':
    df = pd.read_csv('data/complete_starmap.csv')
    star_graph = construct_graph(df)

    with open('data/visited.txt') as visited_file:
        visited = set(star.strip().lower() for star in visited_file.readlines())

    path = beam_search_longest_path(star_graph, start_node='midthun'.lower(), visited=visited, beam_width=10)
    print(path)
    print(len(path))
