from GameState import GameState, GameStateNode, MOVE_NAMES, generate_target
from abc import ABC, abstractmethod
import numpy as np

class Search(ABC):
	@abstractmethod
	def solve(self, start: GameState):
		pass


class BFS(Search):
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
			if node == self.target:
				return node.get_path()
			node.create_children()
			for child in node.children:
				if child == self.target:
					return child.get_path()
				if not node.is_in_path(child.game):
					self.queue.append(child)
		return None


def main():
	t_str = "0 1 2 3 4 5 6 7 8".split(' ')
	s_str = "0 3 8 4 1 7 2 6 5".split(' ')
	target = GameState()
	target.fill(np.array(list(map(int, t_str))).reshape(3, 3))
	start = GameState()
	start.fill(np.array(list(map(int, s_str))).reshape(3, 3))
	
	print("Target:")
	target.print()
	print("Start:")
	start.print()
	
	bfs = BFS(target)
	path = bfs.solve(start)
	if path is None:
		print("No solution")
	else:
		print(f"Solution: {len(path)} moves")
		print(path)
		print([MOVE_NAMES[i] for i in path])


if __name__ == "__main__":
	main()
