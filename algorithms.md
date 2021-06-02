# Algorithms for this Project

Designed by Michael Mesquita

## Breadth-First Search

### Overview

Moving down the search tree, one level at a time. Must cover all nodes in a given depth together before moving to the next depth.

### Algorithm

1. Import starting node, goal node, an empty list for storing visited points, and the graph.
2. Enqueue the starting node and add it to the list of visited points.
3. If queue is not empty, pop the node, furthermore known as "current node". (At first run of this line, queue should not be empty because starting node is still here.)
4. If queue is empty, GOTO 10
5. If "current node" is goal, GOTO 9
6. Get list of neighbors from the current node.
7. If neighbor is not in visited points list
   1. Set neighbor's parent as current node
   2. Enqueue neighbor node.
8. If there are no more neighbors to process, GOTO 4.
9. Return path to goal traversing through parents of nodes
   1. Record cost of path at the same time.
10. Return "no path found" error message.

### Notes

- You'll have to implement this one with a queue.
- You'll also probably need some kind of node Data Structure, or a way to record how you got to this specific node that you can
  traverse backwards to report the path of each data structure.
