import numpy as np
import numpy.typing as npt

MIN_PUZZLE_SIZE = 3
MAX_PUZZLE_SIZE = 25

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

MOVE_NAMES = ['up', 'down', 'left', 'right']


# GameState class represents the state of the puzzle
class GameState:
  size: int
  # 2D array representing the board
  board: npt.NDArray
  empty: tuple
  possible_moves: list[bool]
  
  def __init__(self):
    self.size = 0
  
  # Fill the game state with the given board and empty cell
  def fill(self, board: list[list] | npt.NDArray, empty: tuple[int, int] = None):
    self.board = np.array(board)
    self.empty = empty
    if empty is None:
      self.empty = np.where(self.board == 0)
      if len(self.empty) == 0:
        raise ValueError('Board has no empty cell')
      self.empty = (self.empty[0], self.empty[1])
    self.size = self.board.shape[0]
    return self
  
  # Create a new game state with the given size
  def create(self, size: int):
    self.size = size
    self.board = np.arange(1, size * size + 1).reshape(size, size)
    self.empty = (size - 1, size - 1)
    self.board[self.empty] = 0
    return self
  
  # Shuffle the game state with the given number of moves
  def shuffle(self, moves: int = 20):
    i = 0
    previous = -1
    while i < moves:
      direction = np.random.randint(4)
      if DIR_UP == previous and direction == DIR_DOWN:
        continue
      if DIR_DOWN == previous and direction == DIR_UP:
        continue
      if DIR_LEFT == previous and direction == DIR_RIGHT:
        continue
      if DIR_RIGHT == previous and direction == DIR_LEFT:
        continue
      if self.move(direction):
        previous = direction
        i += 1
    
    return self
  
  def possible_moves(self):
    return [
      self.empty[0] > 0,
      self.empty[0] < self.size - 1,
      self.empty[1] > 0,
      self.empty[1] < self.size - 1
    ]
  
  # Move the empty cell in the given direction
  def move(self, direction: int):
    if direction == DIR_UP:
      if self.empty[0] == 0:
        return False
      self.board[self.empty], self.board[self.empty[0] - 1, self.empty[1]] = self.board[
        self.empty[0] - 1, self.empty[1]], self.board[self.empty]
      self.empty = (self.empty[0] - 1, self.empty[1])
    elif direction == DIR_DOWN:
      if self.empty[0] == self.size - 1:
        return False
      self.board[self.empty], self.board[self.empty[0] + 1, self.empty[1]] = self.board[
        self.empty[0] + 1, self.empty[1]], self.board[self.empty]
      self.empty = (self.empty[0] + 1, self.empty[1])
    elif direction == DIR_LEFT:
      if self.empty[1] == 0:
        return False
      self.board[self.empty], self.board[self.empty[0], self.empty[1] - 1] = self.board[
        self.empty[0], self.empty[1] - 1], self.board[self.empty]
      self.empty = (self.empty[0], self.empty[1] - 1)
    elif direction == DIR_RIGHT:
      if self.empty[1] == self.size - 1:
        return False
      self.board[self.empty], self.board[self.empty[0], self.empty[1] + 1] = self.board[
        self.empty[0], self.empty[1] + 1], self.board[self.empty]
      self.empty = (self.empty[0], self.empty[1] + 1)
    return True
  
  # Check if the puzzle is solved
  def is_solved(self):
    target = np.arange(1, self.size * self.size + 1).reshape(self.size, self.size)
    target[self.size - 1, self.size - 1] = 0
    return self.board == target
  
  # Print the game state
  def print(self):
    for i in range(self.size):
      for j in range(self.size):
        print(f"{self.board[i, j]:^3}", end=' ')
      print()
    print()
  
  # Create a copy of the game state
  def copy(self):
    new_game = GameState()
    new_game.fill(self.board.copy())
    return new_game
  
  # Compare the game state with another game state
  def __eq__(self, other: "GameState"):
    return np.array_equal(self.board, other.board)
  
  # Get the hash of the game state
  def __hash__(self):
    return hash(self.board.tobytes())
  
  # Convert the game state to a string
  def __str__(self):
    return str(self.board)
  
  # Convert the game state to a string
  def __repr__(self):
    return str(self.board)

# GameStateNode class is a wrapper for the game state that is used in the tree search algorithms
class GameStateNode:
  game: GameState
  parent: "GameStateNode"
  children: list["GameStateNode"]
  direction: int
  depth: int
  
  # Create a new game state node with the given game state, parent, direction, and depth
  def __init__(self, game: GameState, parent: "GameStateNode" = None, direction: int = None, depth: int = 0):
    self.game = game
    self.parent = parent
    self.direction = direction
    self.children = []
    self.depth = depth
  
  # Get the path from the root to the current node
  def get_path(self):
    if self.parent is None:
      return []
    return self.parent.get_path() + [self.direction]
  
  # Create the children of the current node
  def create_children(self):
    if self.children:
      return
    self.children = []
    
    possible_moves = self.game.possible_moves()
    for i in range(4):
      if possible_moves[i]:
        new_game = self.game.copy()
        new_game.move(i)
        self.children.append(GameStateNode(new_game, self, i, self.depth + 1))
  
  # Check if the given game state is in the path from the root to the current node
  def is_in_path(self, game: GameState):
    return self.game == game or (self.parent is not None and self.parent.is_in_path(game))
  
  # Compare the game state node with another game state node
  def __eq__(self, other: "GameStateNode"):
    return self.game == other.game
  
  # Get the hash of the game state node
  def __hash__(self):
    return hash(self.game)
  
  # Convert the game state node to a string
  def __str__(self):
    return str(self.game)
  
  # Convert the game state node to a string
  def __repr__(self):
    return str(self.game)
  
  # Compare the game state node with another game state node
  # This is used in the priority queue to not throw an error when comparing nodes
  def __lt__(self, other: "GameStateNode"):
    return 0

# Print the path to the solution with the given game state
def display_path(path: list[int], game: GameState):
  print('Start:')
  game.print()
  for i in path:
    print(MOVE_NAMES[i])
    game.move(i)
    game.print()

# Main function that lets the user play the puzzle
def main():
  size = int(input('Enter the size of the puzzle (3-25): '))
  if size < MIN_PUZZLE_SIZE or size > MAX_PUZZLE_SIZE:
    print('Invalid size')
    return
  
  game = GameState()
  game.create(size)
  game.print()
  
  while not game.is_solved():
    direction = int(input('Enter direction (0-up, 1-down, 2-left, 3-right): '))
    game.move(direction)
    game.print()
  
  print('Puzzle solved!')


if __name__ == '__main__':
  main()
