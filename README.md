# AI Project 1 - Search Algorithms 
Author: Abbas Aliyev

## Introduction
In this project, I am going to implement and compare different search algorithms. The algorithms that I am going to implement are:
- Breadth-First Search (BFS)
- A* Search


## Problem
The problem that I am going to solve is the 8-puzzle problem. The 8-puzzle problem is a puzzle that is played on a 3x3 grid with 8 tiles. The tiles are numbered from 1 to 8 and there is one empty tile. The goal of the puzzle is to arrange the tiles in ascending order. The puzzle is solved when the tiles are arranged in the following order:
```
1 2 3
4 5 6
7 8 0
```
The 0 represents the empty tile.

Our code allows us to solve generalized n-puzzle problems. The user can specify the size of the puzzle and the initial state of the puzzle. The code will then solve the puzzle using the search algorithms that I implemented.

## Implementation
The implementation of the project is done in Python. The code is divided into 3 files:
- `main.py`: This file contains the main function that is used to run the program. It creates demo states, and runs the search algorithm.
- `GameState.py`: This file contains the implementation of the game state. The `GameState` is a class that contains the current state of the puzzle. It also contains the implementation of the wrapper of the `GameState` class: `GameStateNone`. The `GameStateNone` class is used to represent the state of the puzzle in a graph. The `GameStateNone` class contains the parent state, the action that was taken to reach the current state, the depth of the state, and the direction of the state from the parent state.
- `Search.py`: This file contains the implementation of the search algorithms. The search algorithms that are implemented are BFS and A* Search
- `Heuristic.py`: This file contains the implementation of the heuristic function that is used in the A* Search algorithm. The heuristic function that is used is the Manhattan distance.
- `Queue.py`: This file contains the implementation of the queue that is used in the BFS algorithm and the priority queue that is used in the A* Search algorithm. It also contains the implementation of metered queues that is used to measure the number of nodes that are expanded during the search.

## Running the Program
To run the program, you need to have Python installed on your computer. You can run the program by running the following command in the terminal:
```
python main.py
```
The program will run the search algorithms on the demo states and print the results to the terminal.

## Conclusion
In this project, I implemented and compared different search algorithms. I implemented the BFS and A* Search algorithms and used them to solve the 8-puzzle problem. I also implemented the Manhattan distance heuristic function and used it in the A* Search algorithm. I compared the performance of the search algorithms and found that A* Search is more efficient than BFS. The reason for this is that A* Search uses a heuristic function to guide the search, while BFS does not use any heuristic function. This makes A* Search more efficient than BFS. 
```
Target:
 1   2   3   4  
 5   6   7   8  
 9  10  11  12  
13  14  15   0  

Start:
 1   2   3   4  
 5   6  11   7  
10  13   8  12  
 9   0  14  15  

A* search algorithm
Solution: 12 moves
Time: 5.522000 ms
Enqueued: 78, In queue: 42, Expanded: 36
[0, 2, 1, 3, 3, 3, 0, 2, 0, 3, 1, 1]
['up', 'left', 'down', 'right', 'right', 'right', 'up', 'left', 'up', 'right', 'down', 'down']

Breadth-first search algorithm
Solution: 12 moves
Time: 1124.986000 ms
Enqueued: 15300, In queue: 8119, Expanded: 7181
[0, 2, 1, 3, 3, 3, 0, 2, 0, 3, 1, 1]
['up', 'left', 'down', 'right', 'right', 'right', 'up', 'left', 'up', 'right', 'down', 'down']
```