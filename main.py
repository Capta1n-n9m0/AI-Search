from GameState import GameState

class BFS:
  def __init__(self, size):
    self.size = size
    self.visited = set()
    self.queue = []
  
  def solve(self, game):
    self.visited.add(game)
    self.queue.append(game)
    while len(self.queue) > 0:
      current = self.queue.pop(0)
      if current.is_solved():
        return current
      for i in range(4):
        new_game = current.copy()
        if new_game.move(i) == 1 and new_game not in self.visited:
          self.visited.add(new_game)
          self.queue.append(new_game)
    return None