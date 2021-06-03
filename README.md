# CAP4630-A1-Search
Solving optimization problems using search algorithms.

Architect: Michael Mesquita

Developer: Sean Abuhoff

Reporter: Winston White



Implementations: 

The use of type annotations: Lists, Tuple, and DefaultDict

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



