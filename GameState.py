import numpy as np

MIN_PUZZLE_SIZE = 3
MAX_PUZZLE_SIZE = 25

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

MOVE_NAMES = ['up', 'down', 'left', 'right']


class GameState:
  size: int
  board: np.ndarray
  empty: tuple
  
  def __init__(self):
    self.size = 0
    self.board = np.array([])
    self.empty = (0, 0)
  
  def fill(self, board, empty=None):
    self.board = np.array(board)
    self.empty = empty
    if empty is None:
      self.empty = np.where(self.board == 0)
      if len(self.empty) == 0:
        raise ValueError('Board has no empty cell')
      self.empty = (self.empty[0], self.empty[1])
    self.size = self.board.shape[0]
  
  def create(self, size):
    self.size = size
    self.board = np.arange(1, size * size + 1).reshape(size, size)
    self.empty = (size - 1, size - 1)
    self.board[self.empty] = 0
  
  def shuffle(self, moves=1000):
    for i in range(moves):
      self.move(np.random.randint(4))
  
  def move(self, direction):
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
  
  def is_solved(self):
    target = np.arange(1, self.size * self.size + 1).reshape(self.size, self.size)
    target[self.size - 1, self.size - 1] = 0
    return self.board == target
  
  def print(self):
    for i in range(self.size):
      for j in range(self.size):
        print(f"{self.board[i, j]:^3}", end=' ')
      print()
    print()
  
  def copy(self):
    new_game = GameState()
    new_game.fill(self.board.copy())
    return new_game
  
  def __eq__(self, other):
    return np.array_equal(self.board, other.board)
  
  def __hash__(self):
    return hash(self.board.tobytes())
  
  def __str__(self):
    return str(self.board)
  
  def __repr__(self):
    return str(self.board)


class GameStateNode:
  game: GameState
  parent: "GameStateNode"
  children: list["GameStateNode"]
  direction: int
  depth: int
  
  def __init__(self, game: GameState, parent: "GameStateNode" = None, direction=None, depth=0):
    self.game = game
    self.parent = parent
    self.direction = direction
    self.children = []
    self.depth = depth
  
  def get_path(self):
    if self.parent is None:
      return []
    return self.parent.get_path() + [self.direction]
  
  def create_children(self):
    if self.children:
      return
    self.children = []
    for i in range(4):
      new_game = self.game.copy()
      if new_game.move(i):
        self.children.append(GameStateNode(new_game, self, i, self.depth + 1))
        
  def is_in_path(self, game: GameState):
    if self.parent is None:
      return self.game == game
    return self.game == game or self.parent.is_in_path(game)
  
  def __eq__(self, other):
    return self.game == other.game
  
  def __hash__(self):
    return hash(self.game)
  
  def __str__(self):
    return str(self.game)
  
  def __repr__(self):
    return str(self.game)


def display_path(path, game):
  print('Start:')
  game.print()
  for i in path:
    print(MOVE_NAMES[i])
    game.move(i)
    game.print()
  
  
def generate_target(size):
  target = GameState()
  target.fill(np.arange(1, size * size + 1).reshape(size, size))
  target.board[size - 1, size - 1] = 0
  return target


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


