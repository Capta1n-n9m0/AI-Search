from queue import PriorityQueue
from GameState import GameState, GameStateNode, MOVE_NAMES
from abc import ABC, abstractmethod
from Heuristics import Heuristics


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


class AStar(Search):
	target: GameState
	heuristics: Heuristics
	queue: PriorityQueue[tuple[int, GameStateNode]]
	
	def __init__(self, target: GameState, heuristics: Heuristics):
		self.target = target
		self.heuristics = heuristics
	
	def solve(self, start: GameState):
		self.queue = PriorityQueue()
		start_node = GameStateNode(start)
		self.queue.put((0, start_node))
		while not self.queue.empty():
			_, node = self.queue.get()
			if node.game == self.target:
				return node.get_path()
			if node.is_in_path(self.target):
				continue
			node.create_children()
			for child in node.children:
				if not node.is_in_path(child.game):
					self.queue.put((self.heuristics(child.game) + child.depth, child))
		return None


def main():
	target = GameState().create(3)
	start = GameState().create(3).shuffle(20)
	
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
