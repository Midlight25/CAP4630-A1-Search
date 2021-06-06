# CAP4630-A1-Search
Solving optimization problems using search algorithms.

Architect: Michael Mesquita

Developer: Sean Abuhoff

Reporter: Winston White



Implementations: 

The use of type annotations: Lists, Tuple, DefaultDict, Deque, Optional

DefaultDict is used to create the adjency graph by 
converting the edges list into a dictionary with each city's
neighbors and the total miles cost of reaching them.

Tuples are implemented to display the paths of each city
with the following format:
Name of first city, name of neighboring city, and path cost
Ex: Fagaras, Sibiu, 99

Tuples are then converted into lists which are encoded into EDGES.
EDGES is then iterated through each edge, extracting city names
and path costs. 

Deque, or double-ended queue, is utitlized to hold all new nodes 
discovered during the load-branches phase of the BFS algorithm.
(Double-ended stack is used for DFS algorithm following the same 
procedure).

Optional is used to tell the type checker if an object of a specified type is required; otherwise, None is required. 

BFS Algorithm:
Finding the shortest path between the starting and end nodes using a queue. 
Once a path is found a node network, based on which paths
were taken to reach a node, is utilized to determine a list of parent nodes 
from end to start. We also implemented a way to prevent cycles from occurring,
in order to produce the correct results for this algorithm.
Finally, if a path is not found bewteen start to end, then 
the function does not return any value.


DFS Algorithm:
Similar procedure as BFS Algorithm; only implementing a stack rather than a queue. 
