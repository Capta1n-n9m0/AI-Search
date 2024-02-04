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
    self.board = board
    self.empty = empty
    if empty is None:
      self.empty = np.where(board == 0)
      if len(self.empty[0]) == 0:
        raise ValueError('Board has no empty cell')
      self.empty = (self.empty[0][0], self.empty[1][0])
    self.size = board.shape[0]
  
  def create(self, size):
    self.size = size
    self.board = np.arange(1, size * size + 1).reshape(size, size)
    self.empty = (size - 1, size - 1)
    self.board[self.empty] = 0
    self.shuffle()
  
  def shuffle(self):
    for i in range(1000):
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
  
  def is_target(self, target):
    return np.array_equal(self.board, target)
  
  def is_solved(self):
    target = np.arange(1, self.size * self.size).reshape(self.size, self.size)
    target[self.size - 1, self.size - 1] = 0
    return self.is_target(target)
  
  def print(self):
    for i in range(self.size):
      for j in range(self.size):
        print(self.board[i, j], end=' ')
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

class GameStateNode:
  game: GameState
  parent: "GameStateNode"
  children: list["GameStateNode"]
  direction: int
  
  def __init__(self, game, parent, direction):
    self.game = game
    self.parent = parent
    self.direction = direction
  
  def get_path(self):
    if self.parent is None:
      return [self.direction]
    return self.parent.get_path() + [self.direction]
  
  def create_children(self):
    self.children = []
    for i in range(4):
      new_game = self.game.copy()
      if new_game.move(i):
        self.children.append(GameStateNode(new_game, self, i))
        
  def is_in_path(self, game):
    if self.parent is None:
      return self.game == game
    return self.game == game or self.parent.is_in_path(game)
  
  def __eq__(self, other):
    return self.game == other.game
  
  def __hash__(self):
    return hash(self.game)


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


