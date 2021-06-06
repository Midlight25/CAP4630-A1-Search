"""
    Authors: Michael Mesquita,
    Name: A1 Search Strategies
    Date: 31 May 2021
    Course: CAP 4630 - Dr. Marques
"""

# Importing the types needed for type annotation in this project.
from typing import Deque, List, Tuple, DefaultDict, Any

# To build the adjacency graph, we will use the defaultdict factory
# to turn our edges list into a dictionary where every city
# has it's neighbors and the cost to reach those neighbors.
from collections import defaultdict, deque


class Node:
    def __init__(self, name: str, parent: Any):
        self.name: str = name
        self.parent: Node = parent


def breadth_first_search(
        start: str,
        goal: str,
        graph: DefaultDict[str, List[Tuple[str, int]]]):
    """
        Breadth First Search
        Pre-Condition: The start and goal parameters are strings that contain
            valid city names found in DefaultDict
        Post-Condition: The first path found from start to goal and
            the cost of taking that path is printed to the console.
        Description: A path between start and goal is attempted to be found
            using a queue. If a path is found, a node network based on
            what path was taken to reach that node is used to identify
            a list of parents from goal to start. The cost of that path is
            also calculated from that node network.
    """

    # This list will contain the names of all nodes that have already been
    # visited by the function.
    visited: List[str] = []

    # This double-ended queue is used to hold all new nodes found during the
    # load-branches phase of the algorithm.
    queue: Deque[str] = deque()


if __name__ == "__main__":

    # This is the encoding of all the paths between the cities. The format is:
    # name of first city, name of second city, and finally the cost of path.
    # Would prefer that city names are in alphabetical order across
    # the list.
    EDGES: List[Tuple[str, str, int]] = [
        ("Arad", "Timisoara", 118),
        ("Arad", "Sibiu", 140),
        ("Arad", "Zerind", 75),
        ("Bucharest", "Fagaras", 211),
        ("Bucharest", "Giurgiu", 90),
        ("Bucharest", "Pitesti", 101),
        ("Bucharest", "Urziceni", 85),
        ("Craiova", "Dobreta", 120),
        ("Craiova", "Pitesti", 138),
        ("Craiova", "Rimnicu Vilcea", 120),
        ("Dobreta", "Mehadia", 75),
        ("Eforie", "Hirsova", 86),
        ("Fagaras", "Sibiu", 99),
        ("Hirsova", "Urziceni", 98),
        ("Iasi", "Neamt", 87),
        ("Iasi", "Vaslui", 92),
        ("Lugoj", "Mehadia", 70),
        ("Lugoj", "Timisoara", 111),
        ("Oradea", "Sibiu", 151),
        ("Oradea", "Zerind", 71),
        ("Pitesti", "Rimnicu Vilcea", 97),
        ("Rimnicu Vilcea", "Sibiu", 80),
        ("Urziceni", "Vaslui", 142),
    ]

    # Building the dictionary. You can look up a city's neighbors and the
    # cost to get there if you know the city's name.
    # EX: "Bucharest", [("Giurgiu", 90), ("Urziceni", 85)]
    adj_graph: DefaultDict[str,
                           List[Tuple[str, int]]] = defaultdict(list)

    # Iterating through each edge and pulling the city names and the path
    # cost.
    for first_city, second_city, cost in EDGES:

        # Add this path to the entry in the dictionary for both
        # cities.
        adj_graph[first_city].append((second_city, cost))
        adj_graph[second_city].append((first_city, cost))

    # Making bad change to code here
