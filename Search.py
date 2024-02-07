from GameState import GameState, GameStateNode
from abc import ABC, abstractmethod
from Heuristics import Heuristics
from IQueue import PriorityQueue, IQueue, IMetered


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
	queue: IQueue[tuple[int, GameStateNode]] | IMetered
	
	def __init__(self, target: GameState, heuristics: Heuristics, queue: IQueue[tuple[int, GameStateNode]] = PriorityQueue()):
		self.target = target
		self.heuristics = heuristics
		self.queue = queue
	
	def solve(self, start: GameState):
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
	
	def get_metrics(self):
		if not isinstance(self.queue, IMetered):
			return None
		return self.queue.get_count(), len(self.queue), self.queue.get_count() - len(self.queue)
	
