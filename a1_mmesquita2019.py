"""
    Authors: Michael Mesquita,
    Name: A1 Search Strategies
    Date: 31 May 2021
    Course: CAP 4630 - Dr. Marques
"""

# Importing the types needed for type annotation in this project.
from typing import Deque, List, Tuple, DefaultDict, Union

# To build the adjacency graph, we will use the defaultdict factory
# to turn our edges list into a dictionary where every city
# has it's neighbors and the cost to reach those neighbors.
from collections import defaultdict, deque


class CityNode:
    """
        This class stores instances of cities and where you came from to
        get to them. There are only two data members: "name" which stores the
        string name of the city, and "parent" which stores a pointer to the
        node of the city's 'parent' or where you traversed to get to
        that city.
    """

    def __init__(self,
                 name: str,
                 parent: Union['CityNode',
                               None] = None):
        self.name: str = name
        self.parent: Union[CityNode, None] = parent


def breadth_first_search(
        start: str,
        goal: str,
        graph: DefaultDict[str, List[Tuple[str, int]]]
) -> Union[CityNode, None]:
    """
        Breadth First Search
        Pre-Condition: The start and goal parameters are strings that contain
            valid city names found in DefaultDict
        Post-Condition: A reverse link-list node is returned with a link
            to the node that was used to visit that city. If no path
            between start and goal is found, nothing is returned.
        Description: A path between start and goal is attempted to be found
            using a queue. If a path is found, a node network based on
            what path was taken to reach that node is used to identify
            a list of parents from goal to start.
    """

    # This list will contain the names of all nodes that have already been
    # visited by the function.
    visited: List[str] = []

    # This double-ended queue is used to hold all new nodes found during the
    # load-branches phase of the algorithm.
    queue: Deque[CityNode] = deque()

    # Create the first node for the starting city and load it into the
    # queue.
    queue.append(CityNode(start))

    # As soon as we run out of items in the queue, this loop ends.
    while queue:

        # Pop the node at the front of the queue. This is the city that
        # we're now processing.
        current_node: CityNode = queue.popleft()
        visited.append(current_node.name)

        # If this city is our goal, then we return this node with all it's
        # parents
        if current_node.name == goal:
            return current_node

        # If the current city is not our goal, then we look at it's neighbors
        # Remember that every destination is a tuple. [name, cost]
        for destination in graph[current_node.name]:

            # Prevent cycles by checking the name of the destination
            # against the names in visited.
            if destination[0] not in visited:

                # Add new destinations to the queue for processing
                # later.
                queue.append(CityNode(destination[0], current_node))

    # If we can't find a path from start to goal, then we return
    # none.
    return None


def depth_first_search(
    start: str,
    goal: str,
    graph: DefaultDict[str, List[Tuple[str, int]]]
) -> Union[CityNode, None]:
    """
        Depth First Search
        Pre-Condition: The start and goal parameters are strings that contain
            valid city names found in DefaultDict
        Post-Condition: A reverse link-list node is returned with a link
            to the node that was used to visit that city. If no path
            between start and goal is found, nothing is returned.
        Description: A path between start and goal is attempted to be found
            using a stack. If a path is found, a node network based on
            what path was taken to reach that node is used to identify
            a list of parents from goal to start.
    """
    # This list will contain the names of all nodes that have already been
    # visited by the function.
    visited: List[str] = []

    # This double-ended stack is used to hold all new nodes found during the
    # load-branches phase of the algorithm.
    stack: Deque[CityNode] = deque()

    # Create the first node for the starting city and load it into the
    # stack.
    stack.append(CityNode(start))

    # As soon as we run out of items in the stack, this loop ends.
    while stack:

        current_node: CityNode = stack.pop()
        visited.append(current_node.name)

        # If this city is our goal, then we return this node with all it's
        # parents
        if current_node.name == goal:
            return current_node

        # If the current city is not our goal, then we look at it's neighbors
        # Remember that every destination is a tuple. [name, cost]
        for destination in graph[current_node.name]:

            # Prevent cycles by checking the name of the destination
            # against the names in visited.
            if destination[0] not in visited:

                # Add new destinations to the stack for processing
                # later.
                stack.append(CityNode(destination[0], current_node))

    # If we can't find a path from start to goal, then we return
    # none.
    return None


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
