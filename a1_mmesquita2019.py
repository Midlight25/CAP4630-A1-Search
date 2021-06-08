"""
    Authors: Michael Mesquita,
    Name: A1 Search Strategies
    Date: 31 May 2021
    Course: CAP 4630 - Dr. Marques
"""

# Importing the types needed for type annotation in this project.
from typing import Deque, List, Tuple, DefaultDict, Optional

# To build the adjacency graph, we will use the defaultdict factory
# to turn our edges list into a dictionary where every city
# has it's neighbors and the cost to reach those neighbors.
from collections import defaultdict, deque

# Aliasing the type for the adj_graph, used for functions later.
Adj_Graph = DefaultDict[str, DefaultDict[str, int]]


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
                 parent: Optional['CityNode'] = None):
        self.name: str = name
        self.parent: Optional[CityNode] = parent


def breadth_first_search(start: str, goal: str, graph: Adj_Graph
                         ) -> Optional[CityNode]:
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

        # Select the cities, from the neighbors, that have
        # yet to be visited.
        destinations: List[str] = [destination
                                   for destination in graph[current_node.name]
                                   if destination not in visited]

        for destination in destinations:
            # Add new destinations to the queue for processing
            # later.
            queue.append(CityNode(destination, current_node))

    # If we can't find a path from start to goal, then we return
    # none.
    return None


def depth_first_search(start: str, goal: str, graph: Adj_Graph
                       ) -> Optional[CityNode]:
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

    # This double-queue stack is used to hold all new nodes found during the
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

        # Select from the neigbors, the cities that have
        # yet to be visited.
        destinations: List[str] = [destination
                                   for destination in graph[current_node.name]
                                   if destination not in visited]

        # If the current city is not our goal, then we look at it's
        # neighbors
        for destination in destinations:
            # Add new destinations to the stack for processing
            # later.
            stack.append(CityNode(destination, current_node))

    # If we can't find a path from start to goal, then we return
    # none.
    return None


def a_star_search(start: str, goal: str, graph: Adj_Graph
                  ) -> Optional[CityNode]:
    """
        A* Search
        Pre-Condition: Start and Goal are city names found in graph
        Post-Condition: If a valid path to the goal from start is found, a
            node from a reverse linked-list will be returned called CityNode.
            If no such path is found, then None is returned.
        Description: Uses the A* algorithm, a stack, and an adjacency graph
            to return the optimal path between two destinations, both using
            the least number of moves and the lowest cost/distance.
    """

    # Storing the names of cities that we've visited already.
    visited: List[str] = []

    # Making a stack to store cities that we've discovered and the
    # total distance from "start"
    stack: Deque[Tuple[CityNode, int]] = deque()

    # Adding the start location with a total distance of zero
    stack.append((CityNode(start), 0))

    while stack:

        # Get a new city and distance to that city from the stack.
        # This city should have the lowest distance out of
        # all the cities yet to be visited.
        current_node, distance = stack.pop()
        visited.append(current_node.name)

        if current_node.name == goal:
            return current_node

        # Select from the neighbors, the cities that have
        # yet to be visited.
        destinations: List[str] = [destination
                                   for destination in graph[current_node.name]
                                   if destination not in visited]

        for destination in destinations:

            # Append the destination to the stack, along with the total
            # distance to reach it based on the distances
            # of it's parents
            stack.append((CityNode(destination, current_node),
                          graph[current_node.name][destination] + distance))

        # Sort the stack based on total distances, the cities with
        # the lowest total distances are placed at the top of
        # the stack to be popped next
        stack = deque(sorted(stack, key=lambda x: -x[1]))

    return None


def compute_path(start_node: CityNode, graph: Adj_Graph) -> None:
    """
        Compute Path
        Pre-Condition: Given a valid CityNode instance that has a good link
        to another CityNode as it's parent.
        Post-Condition: The path from the start-node to the top of
            this reverse linked-list is printed to the console.
    """

    # Load the current node into local memory, so that we can modify this
    # variable later.
    current_node: CityNode = start_node

    # If there is a parent to this node, then we can run the backtracking
    # code. If this node has no parent, then there is no path to
    # backtrack.
    if current_node.parent is not None:

        # Set up holding variables for the output, we build the output string
        # using this list. Because we're backtracking, the order of strings
        # needs to be reversed in the end.
        output_string_list: List[str] = []
        total_cost: int = 0

        # This will loop and stop at the second to last node in this
        # list.
        while current_node.parent is not None:

            # Because the entire expression is too big to fit in the next
            # three statements.
            distance = graph[current_node.name][current_node.parent.name]

            output_string_list.append(f"[{current_node.name}]")
            output_string_list.append(f"({distance})")
            total_cost += distance

            current_node = current_node.parent

        # Add final node to output string. Since we're at the destination
        # there's no new cost to record.
        output_string_list.append(f"[{current_node.name}]")

        # Compile output string by reversing the list and joining
        # together with arrows in between.
        output_string: str = ' -> '.join(reversed(output_string_list))

        print("!!! Path Found !!!", end='\n\n')
        print("Printing path to destination:")
        print(f"\t{output_string}")
        print(f"Total Distance: {total_cost} units.", end='\n\n')

    # If there is no parent to start_node, then there is no path to
    # compute.
    else:
        print("X-- No Path Available --X", end='\n\n')
        print("For this source and destination pair:",
              "there is no path and no cost, you are already there.")


def print_title() -> None:
    """
        Print Title
        Pre-Condition: Nothing
        Post-Condition: Nothing
        Description: Prints a vanity ASCII banner to the console. Because I'm
            extra like that.
    """
    print("   ___           _                          __    ___  ___")
    print("  / _ | ___ ___ (_)__ ____  __ _  ___ ___  / /_  / _ |<  /")
    print(
        " / __ |(_-<(_-</ / _ `/ _ \\/  ' \\/ -_) _ \\/ __/ / __ |/ /")
    print("/_/ |_/___/___/_/\\_, /_//_/_/_/_/\\__/_//_/\\__/ /_/ |_/_/")
    print("   ____         /___/   __     ___   __              _ __  __")
    print(
        "  / __/__ ___ _________/ /    / _ | / /__ ____  ____(_) /_/ / ",
        "__ _  ___")
    print(
        " _\\ \\/ -_) _ `/ __/ __/ _ \\  / __ |/ / _ `/ _ \\/ __/ / __/",
        "_ \\/  ' \\(_-<")
    print("/___/\\__/\\_,_/_/  \\__/_//_/ /_/ |_/_/\\_,",
          "/\\___/_/ /_/\\__/_//_/_/_/_/___/")
    print("                                    /___/", end='\n\n\n')


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
    # EX: {"Bucharest": {"Giurgiu": 90, "Urziceni": 85}}
    adj_graph: Adj_Graph = defaultdict(lambda: defaultdict(int))

    # Iterating through each edge and pulling the city names and the path
    # cost.
    for first_city, second_city, cost in EDGES:

        # Add this path to the entry in the dictionary for both
        # cities.
        adj_graph[first_city][second_city] = cost
        adj_graph[second_city][first_city] = cost

    print_title()

    # Starting welcoming dialog
    print("Welcome to the Search Algorithms assignment.",
          "Where would you like to go first?", end='\n\n')

    # Print Parts Menu
    print('Part 1: Shortest Route')
    print(
        "\tUse three different algorithms to find the shortest distance",
        "between two cities in a network. Use Breadth-First-Search,",
        "Depth-First-Search, or A* algorithms to find the most optimal path.",
        end='\n\n')
    print("Part 2: Adversarial Search")
    print(
        '\tPlay a tic-tac-toe game against a computer opponent using the',
        'MINMAX algorithm to make decisions about how to play the game.',
        end='\n\n')

    # Getting user selection on what part to visit.
    print(
        "Please select which part you wish to visit: [1] or [2].",
        "The default option is [1], all unrecognized input will select",
        "[1] by default.")

    # First user selection on part 1 or part 2
    user_top_menu: str = input("> ")
    print("")

    # The non-default option, Part 2: Tic-Tac-Toe game.
    if user_top_menu[0] == '2':
        # Start the CLI for part 2
        pass

    # Default Option for unrecognized input is #1, so doing that for every
    # other user input besides '2'
    else:

        # Instantiating the variables we're using here.
        running: bool = True            # Controls the main loop
        selection_made: bool = False    # Controls input validation loop
        algorithm: str = ""             # User selection for algorithm
        departure: str = ""             # User selection for city parameter
        go_again: str = ""              # User selection for main loop exit

        # Print the user welcome message and instructions once.
        # Not going to print this every single loop.
        print('starting part 1...', end='\n\n')
        print("Part 1: Shortest Route")
        print(
            "Given a network map of cities in Romania and the cost",
            "to move between cities, use an algorithm to find",
            "the most optimal path between a city of your choice",
            "and the city of Bucharest.",
            end='\n\n')

        # Start main control loop.
        while running:
            print(
                "Please select the algorithm that you wish to run:",
                end='\n\n')

            # Reseting selection_made in case that this is the n+1
            # loop.
            selection_made = False

            # Start algorithm selection user input validation loop.
            while not selection_made:
                print("[B]: Breadth-First-Search")
                print("[D]: Depth-First-Search")
                print("[A]: A* Algorithm Search")

                algorithm = input("> ")
                algorithm = algorithm.upper()
                print()

                if algorithm[0] not in ['B', 'D', 'A']:
                    print("I'm sorry, this is not a valid selection.")
                    print(
                        "Please choose from one of the algorithms below:",
                        end='\n\n')
                else:
                    selection_made = True

            print(
                "Please type the name of the city of your departure:")

            # Reset this bool for next user input validation loop
            selection_made = False

            # Start city-of-departure selection input validation loop.
            while not selection_made:
                departure = input("> ")
                departure = departure.title()
                print("")

                # Remember that the default iterator on a dictionary is
                # a List[str] of that dict's keys.
                if departure not in adj_graph:
                    print(
                        f"I'm sorry, but {departure} is not a",
                        "valid destination.")
                    print(
                        "Please type in your destination:")
                else:
                    selection_made = True

            # Perform Breadth-First-Search Algorithm
            if algorithm[0] == 'B':
                print(
                    f'Searching for best path between {departure}',
                    'and Bucharest using "BFS"')

                result_node: Optional[CityNode] = breadth_first_search(
                    departure, "Bucharest", adj_graph)

                if result_node is not None:
                    compute_path(result_node, adj_graph)

                # In the unlikely event that the user has managed to
                # completely bypass all of my checks against entering
                # a city that is not in the Adjacency Graph.
                else:
                    # THIS SHOULD NEVER RUN
                    print("X>> No Path Found <<X", end='\n\n')

            # Perform Depth-First-Search Algorithm
            elif algorithm[0] == 'D':
                print(
                    f"Searching for best path between {departure}",
                    'and Bucharest using "DFS"')

                result_node: Optional[CityNode] = depth_first_search(
                    departure, "Bucharest", adj_graph)

                if result_node is not None:
                    compute_path(result_node, adj_graph)

                # Read the comment in BFS
                else:
                    print("X>> No Path Found <<X", end='\n\n')

            # Perform A* Algorithm
            elif algorithm[0] == 'A':
                print(
                    f"Searching for best path between {departure}",
                    'and Bucharest using "A*"')

                result_node: Optional[CityNode] = a_star_search(
                    departure, "Bucharest", adj_graph)

                if result_node is not None:
                    compute_path(result_node, adj_graph)

                # See the comment in BFS
                else:
                    print("X>> No Path Found <<X", end='\n\n')

            # Not doing a user validation loop, no is the default
            # option here.
            print("Would you like to calculate another route? [y/N]",
                  "(No is the default option.)")

            go_again = input("> ")
            print()

            # If an only if a user explicitly asked to go again, does the
            # loop restart here.
            if go_again.upper() != 'Y':
                print("Goodbye!")
                running = False
