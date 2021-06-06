# CAP4630-A1-Search

Solving optimization problems using search algorithms.

Architect: Michael Mesquita

Developer: Sean Abuhoff/Michael Mesquita

Reporter: Winston White

## Implementations

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

Optional is used to tell the type checker that can object can be either a specific type or None.

BFS Algorithm:
Finding the shortest path between the starting and end nodes using a queue.
Once a path is found a node network, based on which paths
were taken to reach a node, is utilized to determine a list of parent nodes
from end to start. We also implemented a way to prevent cycles from occurring,
in order to produce the correct results for this algorithm.
Finally, if a path is not found bewteen start to end, then
the function returns nothing.

DFS Algorithm:
Similar procedure as BFS Algorithm; only implementing a stack rather than a queue. 

A* Algorithm:
Implementing a stack to find the shortest route between two points with
the fewest number of moves and lowest path costs.

## Who Did What

Michael Mesquita initially worked as the "Developer" until he passed
that role to Sean; as such, Michael took the role as Architect. Michael's idea
for this program was to implement a data structure for each algorithm.
However, once we ran into some issues(such as how to first start implementing
the program), Michael decided to switch back to Developer and help Sean.
After some time, they realized that both the BFS and DFS algorithms does not
utilize path costs, so the implementation for both of those functions did not take
too long. A*, on the other hand, took quite some time since it does count for path costs.
Because of this, Michael was the only one to implement the function for that algorithm.
I, the reporter, was going through each iteration of the programming, detailing
what each part of the code does. I also provided useful links 
to my teammates whenever they were stuck on a problem.



