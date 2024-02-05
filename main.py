from GameState import GameState, GameStateNode, MOVE_NAMES


class BFS:
  target: GameStateNode
  start: GameStateNode
  queue: list[GameStateNode]
  
  def __init__(self, target: GameState):
    self.target = GameStateNode(target)
    self.queue = []
  
  def solve(self, start: GameState):
    self.start = GameStateNode(start)
    self.queue.append(self.start)
    while len(self.queue) > 0:
      node = self.queue.pop(0)
      node.create_children()
      for child in node.children:
        if child == self.target:
          return child.get_path()
        if not self.target.is_in_path(child.game):
          self.queue.append(child)
    return None
      
  
def main():
  target = GameState()
  target.fill([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
  start = GameState()
  start.create(3)
  
  print("Target:")
  target.print()
  print("Start:")
  start.print()
  
  bfs = BFS(target)
  path = bfs.solve(start)
  if path is None:
    print("No solution")
  else:
    print(path)
    print([MOVE_NAMES[i] for i in path])
  
  
if __name__ == "__main__":
  main()
    