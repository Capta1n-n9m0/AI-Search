# AI Project 1 - Search Algorithms 
Author: Abbas Aliyev

## Introduction
In this project, I am going to implement and compare different search algorithms. The algorithms that I am going to implement are:
- Breadth-First Search (BFS)
- A* Search


## Problem
The problem I will solve is the 8-puzzle problem. The 8-puzzle problem is a puzzle that is played in a 3x3 grid in which there are 8 tiles. The tiles are numbered 1 through 8 and there is one empty tile. The objective of the puzzle is to place the tiles as given in the below example in an increasing order. The puzzle is considered solved by that tile layout:
```
1 2 3
4 5 6
7 8 0
```
The 0 represents the empty tile.

My code allows solving generalized n-puzzle problems. The user can specify the size of the puzzle and the initial state of the puzzle. The code will then solve the puzzle using the search algorithms that I implemented.

## Implementation
The project is programmed using Python, and the code is divided into 5 files:

- `main.py`: This file encapsulates the main function to be run when using the program. It initializes demo states and launches the search algorithm.
- `GameState.py`: It contains the implementation of the game state. The `GameState` is a class that contains the current state of the puzzle. It also contains the implementation of the wrapper of the class `GameState`: `GameStateNode`. The GameStateNode class is used to represent the state of the puzzle in a graph. The `GameStateNode` class contains the parent state, the action from the parent to the current state, the depth of the state, and the direction from the parent state.
- `Search.py`: It contains the implementation of the search algorithms. The implemented search algorithms are BFS and A* Search.
- `Heuristic.py`: This file contains the implementation of the heuristic function used for the A* Search algorithm. The heuristic function to be used is the Manhattan distance.
- `Queue.py`: Contains the implementation of the queue used in the BFS algorithm and the priority queue used in the A* Search algorithm. Moreover, it contains the implementation of metered queues to measure the count of nodes that get expanded during the search.

## Running the Program
To run the program, you need to have Python installed on your computer.
**Make sure you have Python 3.11 or later installed on your computer.**
1. You need to clone the repository to your computer. You can do this by running the following command in the terminal:
```
git clone https://github.com/Capta1n-n9m0/AI-Search.git
```
2. After you have cloned the repository, you need to navigate to the directory where the repository is located. You can do this by running the following command in the terminal:
```
cd AI-Search
```
3. After that you need to create a virtual environment. You can do this by running the following command in the terminal:
```
python -m venv venv
```
4. After you have created the virtual environment, you need to activate it. You can do this by running the following command in the terminal:
```
source venv/bin/activate
```
5. After you have activated the virtual environment, you need to install the required packages. You can do this by running the following command in the terminal:
```
pip install -r requirements.txt
```
6. After you have installed the required packages, you can run the program.
```
python main.py
```
The program will run the search algorithms on the demo states and print the results to the terminal.

## Conclusion
In this project, I developed and compared implementations of several different search algorithms: BFS and A* Search, applied to solve the 15-puzzle problem. I have also implemented the heuristic function in question, the Manhattan distance heuristic, for use in A* Search. The comparison of the two search algorithms shows that A* Search performs more effectively than BFS because A* Search uses a heuristic function to guide the search, while BFS does not use any heuristic function. This makes A* Search more efficient than BFS. The results of the comparison are as follows:
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