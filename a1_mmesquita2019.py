"""
    Authors: Michael Mesquita, Sean Abuhoff, Winston White
    Name: A1 Search Strategies
    Date: 6-8-2021
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
        # Displays a summary onto the screen describing what the program does.
        print(
            "Welcome to the Tic-Tac-Toe game. You will play as Player X against the computer Player O and compete to get three in a row on the board first. I warn you that it is almost impossible to win against the bot. Thanks to the MINMAX function, this gives Player O (the bot) an advantage making it almost unbeatable. Can you beat the bot? Lets find out.")

        # Initializing boardspaces that will be in the layout board
        # with numbers, showing the user where they can make moves.
        boardspaces = {1: '1', 2: '2', 3: '3',
                       4: '4', 5: '5', 6: '6',
                       7: '7', 8: '8', 9: '9'}


        # Function definition Layout with parameter boardspaces that will
        # display a board with numbers in them, showing where the user can make moves.
        def Layout(boardspaces):
            print('------- ' + '\n|' + boardspaces[1] + '|' + boardspaces[2] + '|' + boardspaces[3] + '|' + '\n--+-+--')
            print('|' + boardspaces[4] + '|' + boardspaces[5] + '|' + boardspaces[6] + '|' + '\n--+-+--')
            print('|' + boardspaces[7] + '|' + boardspaces[8] + '|' + boardspaces[9] + '|' + '\n------- ')


        # Function call to display board
        # with numbers in each space
        Layout(boardspaces)

        # Initializing the actual gameboard with all
        # the spaces (1-9) left initially blank.
        board = {1: ' ', 2: ' ', 3: ' ',
                 4: ' ', 5: ' ', 6: ' ',
                 7: ' ', 8: ' ', 9: ' '}


        # Function definition displayBoard with parameter board
        def displayBoard(board):
            print('------- ' + '\n|' + board[1] + '|' + board[2] + '|' + board[3] + '|' + '\n--+-+--')
            print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|' + '\n--+-+--')
            print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + '\n------- ')


        # Displays a blank gameboard
        # onto the screen.
        displayBoard(board)


        # Function Definition availableSpace
        # with parameter spacet to check and see
        # if the space is taken.
        def availableSpace(space):

            # When the space is blank.
            if (board[space] == ' '):

                # Return True.
                return True

            # Otherwise...
            else:

                # Returns False.
                return False


        # Function Definition tie to
        # determine if there is a tie.
        def Tie():

            # Counting loop going through every key in board.
            for key in board.keys():

                # When the key space is blank.
                if board[key] == ' ':
                    # Returns False.
                    return False
                    # Return True.
            return True


        # Function Definition win to check
        # if there are any winning scenarios.
        def win():

            # All the scenarios of how 3 in a row win can happen.

            # When the player makes three in a row with board spaces 1, 2, and 3.
            if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):

                # Return True.
                return True

            # When the player makes three in a row with board spaces 4, 5, and 6.
            elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):

                # Return True.
                return True

            # When the player makes three in a row with board spaces 7, 8, and 9.
            elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):

                # Return True.
                return True

            # When the player makes three in a row with board spaces 1, 4, and 7.
            elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):

                # Return True.
                return True

            # When the player makes three in a row with board spaces 2, 5, and 8.
            elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):

                # Return True.
                return True

            # When the player makes three in a row with board spaces 3, 6, and 9.
            elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):

                # Return True.
                return True

            # When the player makes three in a row with board spaces 1, 5, and 9.
            elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):

                # Return True.
                return True

            # When the player makes three in a row with board spaces 3, 5, and 7.
            elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):

                # Return True.
                return True

            # Otherwise...
            else:

                # Return False.
                return False


        # Function Definition whoWon to check
        # if there are any winning scenarios with
        # the most recent mark a player entered.
        def whoWon(mark):

            # When the player or bot places a mark to make three in a row with board spaces 1, 2, and 3.
            if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):

                # Return True.
                return True

            # When the player or bot places a mark to make three in a row with board spaces 4, 5, and 6.
            elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):

                # Return True.
                return True

            # When the player or bot places a mark to make three in a row with board spaces 7, 8, and 9.
            elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):

                # Return True.
                return True

            # When the player or bot places a mark to make three in a row with board spaces 1, 4, and 7.
            elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):

                # Return True.
                return True

            # When the player or bot places a mark to make three in a row with board spaces 2, 5, and 8.
            elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):

                # Return True.
                return True

            # When the player or bot places a mark to make three in a row with board spaces 3, 6, and 9.
            elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):

                # Return True.
                return True

            # When the player or bot places a mark to make three in a row with board spaces 1, 5, and 9.
            elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):

                # Return True.
                return True

            # When the player or bot places a mark to make three in a row with board spaces 3, 5, and 7.
            elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):

                # Return True.
                return True

            # Otherwise...
            else:

                # Return False.
                return False

                # Function Definition for makeMove


        # so that either the player or bot
        # can make and set their space.
        def makeMove(letter, space):

            # When there is a space available.
            if availableSpace(space):

                # Sets a space with the players or bots letter.
                board[space] = letter

                # Displays an updated gameboard with the most
                # recent move made by either the player or the bot.
                displayBoard(board)

                # When there is a tie.
                if (Tie()):

                    # Displays a message onto the screen
                    # saying no one won and the game is
                    # a tied.
                    print("It's a tie!")

                    # Displays a message onto the screen asking the user if they want to play another round.
                    response = input("Would you like to play another round?: ")

                    # A while loop for when there is a tie.
                    while Tie():

                        # When the user wants to keep playing.
                        if response == "yes":

                            # Displays a board with the numbers showing
                            # where players can make moves.
                            Layout(boardspaces)

                            # Clears the entire board for another round.
                            board[1] = board[2] = board[3] = board[4] = board[5] = board[6] = board[7] = board[8] = \
                            board[9] = ' '

                            # Displays a new blank board for the new round.
                            displayBoard(board)

                        # When the user is done playing.
                        elif response == "no":

                            # Displays a message onto the screen telling the user thanks for playing
                            # and hopes they come back to play some more.
                            print("Thanks for playing. Hope you play again soon.")

                            # Ending the app.
                            exit()

                        # Otherwise...
                        else:

                            # Telling the user that they need to enter a yes to continue playing or no to quit.
                            response = input("Enter either yes to play another round or no to quit: ")

                # When there is a winner.
                if win():

                    # When the computer wins.
                    if letter == 'O':

                        # Displays a message onto the screen telling
                        # the human player the opponent, the bot won.
                        print("Bot wins!")

                        # Displays a message onto the screen asking the user if they want to play another round.
                        response = input("Would you like to play another round?: ")

                        # A while loop for when there is a winner.
                        while win():

                            # When the user wants to keep playing.
                            if response == "yes":

                                # Displays a board with the numbers showing
                                # where players can make moves.
                                Layout(boardspaces)

                                # Clears the entire board for another round.
                                board[1] = board[2] = board[3] = board[4] = board[5] = board[6] = board[7] = board[8] = \
                                board[9] = ' '

                                # Displays a new blank board for the new round.
                                displayBoard(board)

                            # When the user is done playing.
                            elif response == "no":

                                # Displays a message onto the screen telling the user thanks for playing
                                # and hopes they come back to play some more.
                                print("Thanks for playing. Hope you play again soon.")

                                # Ending the app.
                                exit()

                            # Otherwise...
                            else:

                                # Telling the user that they need to enter a yes to continue playing or no to quit.
                                response = input("Enter either yes to play another round or no to quit: ")

                    # Otherwise...
                    else:

                        # Displays a message onto the screen
                        # telling the user they won.
                        print("Player wins!")

                        # Displays a message onto the screen asking the user if they want to play another round.
                        response = input("Would you like to play another round?: ")

                        # A while loop for when there is a winner.
                        while win():

                            # When the user wants to keep playing.
                            if response == "yes":

                                # Displays a board with the numbers showing
                                # where players can make moves.
                                Layout(boardspaces)

                                # Clears the entire board for another round.
                                board[1] = board[2] = board[3] = board[4] = board[5] = board[6] = board[7] = board[8] = \
                                board[9] = ' '

                                # Displays a new blank board for the new round.
                                displayBoard(board)

                            # When the user is done playing.
                            elif response == "no":

                                # Displays a message onto the screen telling the user thanks for playing
                                # and hopes they come back to play some more.
                                print("Thanks for playing. Hope you play again soon.")

                                # Ending the app.
                                exit()

                            # Otherwise...
                            else:

                                # Telling the user that they need to enter a yes to continue playing or no to quit.
                                response = input("Enter either yes to play another round or no to quit: ")
                # Return
                return

            # Otherwise...
            else:

                # Displays a message onto the screen telling the
                # user the space has already been marked.
                print("The space has already been marked!")

                # Allows the user to pick another space.
                space = int(input("Pick another space:"))

                # So the player can make and set
                # their move on the board.
                makeMove(letter, space)

                # Returns the move.
                return


        # Initializing player (the human player) with
        # their letter being X.
        player = 'X'

        # Initializing the computer player (the opponent)
        # with their letting being O.
        computer = 'O'


        # Function Definition for the player
        # to make their move in the game.
        def playersChoice():

            # Allows the human player to make a move, by entering a number 1-9.
            space = int(input("It's your turn Player X. Enter a space (1-9): "))

            # Sets the players move.
            makeMove(player, space)

            # Returns players choice.
            return


        # Function Definition for the computer
        # player to make its own move in the game.
        def computersChoice():

            # bestScore is -1000.
            bestScore = -1000

            # bestMove is 0.
            bestMove = 0

            # Counting loop going through every key in board.
            for key in board.keys():

                # When board[key] space is blank.
                if (board[key] == ' '):

                    # Initializing board[key] to computer.
                    board[key] = computer

                    # Initializing score to MINMAX function call
                    # with parameters board, 0 and False.
                    score = MINMAX(board, 0, False)

                    # Initializing board[key] to blank space.
                    board[key] = ' '

                    # When score is greater than the bestScore.
                    if (score > bestScore):
                        # Initializing bestScore to score.
                        bestScore = score

                        # Initializing bestMove to key.
                        bestMove = key

            # Calling makeMove function with
            # parameters computer and bestMove,
            makeMove(computer, bestMove)

            # Returns
            return


        # Function Definition MINMAX with parameters board, depth
        # and isMaximizing, which will make the computer player
        # unbeatable or extremely hard to beat and rarely win against.
        def MINMAX(board, depth, isMaximizing):

            # If the computer player wins...
            if whoWon(computer):
                return 100

            # If the human player wins...
            elif whoWon(player):
                return -100

            # Otherwise if it's a tie...
            elif Tie():
                return 0

            # When isMaximizing...
            if isMaximizing:

                # bestScore is -1000.
                bestScore = -1000

                # Counting loop going through every key in board.
                for key in board.keys():

                    # When board[key] space is blank.
                    if (board[key] == ' '):

                        # Initializing board[key] to computer.
                        board[key] = computer

                        # Initializing score to MINMAX function call
                        # with parameters board, 0 and False.
                        score = MINMAX(board, 0, False)

                        # Initializing board[key] to blank space.
                        board[key] = ' '

                        # When score is greater than the bestScore.
                        if (score > bestScore):
                            # Initializing bestScore to score.
                            bestScore = score

                # Returns the bestScore
                return bestScore

            # Otherwise...
            else:

                # bestScore is 800.
                bestScore = 800

                # Counting loop going through
                # every key in board.
                for key in board.keys():

                    # When board[key] space is blank.
                    if (board[key] == ' '):

                        # Initializing board[key] to player.
                        board[key] = player

                        # Initializing score to MINMAX function call
                        # with parameters board, 0 and True.
                        score = MINMAX(board, 0, True)

                        # Initializing board[key] to blank space.
                        board[key] = ' '

                        # When score is less than the bestScore.
                        if (score < bestScore):
                            # Initializing bestScore to score.
                            bestScore = score

                # Returns bestScore
                return bestScore


        # Creating a while loop
        # with no winner yet and
        # the game is still going.
        while not win():
            # Having the human player make the next move.
            playersChoice()

            # Having the computer player make a move
            # after the human player.
            computersChoice()
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

