# 8-maze-puzzle-vityarthi-project
This is a puzzle solver which uses different approaches like A* search which is an informed search technique that combines actual cost and estimated cost to reach the goal state. We provide the initial state that consist of 8 numbered tiles and one empty space (represented bu a 0) after providing the initial state the solvability of the problem will be checked and if it is solvable the code will transform it in the predefined goal state with the minimum number of moves.

The algorithm begins by taking an initial puzzle configuration from the user. It first checks whether the puzzle is solvable using inversion count logic.

If the puzzle is solvable, the A* algorithm is applied. The algorithm evaluates each possible move and selects the best one based on the function:f(n)=g(n)+h(n)
 where, 
      g(n) = cost from start node to current node
      h(n) = estimated cost to reach the goal state
this process cstops when the goal state is reached.

